#include <pthread.h>
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
// Inline (copy) ring, as runtime/program_support.c's chan_*_copy, plus a bounded
// spin on the predicate before parking. SPIN = pause iterations, YIELDS = sched_yield rounds.
typedef struct { pthread_mutex_t m; pthread_cond_t ne, nf; unsigned char* b; int cap, head, len, closed, esz; } Ch;
static int SPIN, YIELDS;
static void ch_init(Ch* c,int cap,int esz){ memset(c,0,sizeof *c); pthread_mutex_init(&c->m,0); pthread_cond_init(&c->ne,0); pthread_cond_init(&c->nf,0); c->cap=cap; c->esz=esz; c->b=calloc(cap,esz); }
static inline void relax(void){
#if defined(__aarch64__)
  __asm__ volatile("yield");
#else
  __builtin_ia32_pause();
#endif
}
// Wait (lock held) until pred false; spin outside the lock first.
#define LD(x) __atomic_load_n(&(x), __ATOMIC_RELAXED)
static void wait_full(Ch* c){ // sender: wait while len==cap && !closed
  if (c->len==c->cap && !c->closed && (SPIN||YIELDS)) {
    pthread_mutex_unlock(&c->m);
    for(int i=0;i<SPIN && LD(c->len)==c->cap && !LD(c->closed);i++) relax();
    for(int i=0;i<YIELDS && LD(c->len)==c->cap && !LD(c->closed);i++) sched_yield();
    pthread_mutex_lock(&c->m);
  }
  while(c->len==c->cap&&!c->closed) pthread_cond_wait(&c->nf,&c->m);
}
static void wait_empty(Ch* c){
  if (c->len==0 && !c->closed && (SPIN||YIELDS)) {
    pthread_mutex_unlock(&c->m);
    for(int i=0;i<SPIN && LD(c->len)==0 && !LD(c->closed);i++) relax();
    for(int i=0;i<YIELDS && LD(c->len)==0 && !LD(c->closed);i++) sched_yield();
    pthread_mutex_lock(&c->m);
  }
  while(c->len==0&&!c->closed) pthread_cond_wait(&c->ne,&c->m);
}
static int send(Ch* c,const void* src){ pthread_mutex_lock(&c->m); wait_full(c); if(c->closed){pthread_mutex_unlock(&c->m);return 0;}
  int t=c->head+c->len; if(t>=c->cap)t-=c->cap; memcpy(c->b+t*c->esz,src,c->esz); __atomic_store_n(&c->len,c->len+1,__ATOMIC_RELAXED); pthread_cond_signal(&c->ne); pthread_mutex_unlock(&c->m); return 1; }
static int recv(Ch* c,void* dst){ pthread_mutex_lock(&c->m); wait_empty(c); if(!c->len){pthread_mutex_unlock(&c->m);return 0;}
  memcpy(dst,c->b+c->head*c->esz,c->esz); if(++c->head==c->cap)c->head=0; __atomic_store_n(&c->len,c->len-1,__ATOMIC_RELAXED); pthread_cond_signal(&c->nf); pthread_mutex_unlock(&c->m); return 1; }
static void ch_close(Ch* c){ pthread_mutex_lock(&c->m); __atomic_store_n(&c->closed,1,__ATOMIC_RELAXED); pthread_cond_broadcast(&c->ne); pthread_cond_broadcast(&c->nf); pthread_mutex_unlock(&c->m); }
static Ch c1,c2; static int N; typedef struct { int val; } Msg;
static void* s1(void* a){ for(int i=0;i<N;i++){ Msg m={ (int)(((long long)(i%50000)*25173+13849)%65521) }; send(&c1,&m);} ch_close(&c1); return 0; }
static void* s2(void* a){ for(;;){ Msg t; if(!recv(&c1,&t)) break; Msg m={ (int)(((long long)t.val*17+31)%1000000007) }; send(&c2,&m);} ch_close(&c2); return 0; }
int main(int argc,char**argv){ SPIN=atoi(argv[1]); YIELDS=atoi(argv[2]); N=atoi(argv[3]);
  struct timespec a,b; clock_gettime(CLOCK_MONOTONIC,&a); ch_init(&c1,64,4); ch_init(&c2,64,4);
  pthread_t t1,t2; pthread_create(&t1,0,s1,0); pthread_create(&t2,0,s2,0); long long ck=0;
  for(;;){ Msg t; if(!recv(&c2,&t)) break; ck=(ck*31+t.val)%1000000007; }
  pthread_join(t1,0); pthread_join(t2,0); clock_gettime(CLOCK_MONOTONIC,&b);
  printf("%lld %.1f\n", ck, (b.tv_sec-a.tv_sec)*1e3+(b.tv_nsec-a.tv_nsec)/1e6); }

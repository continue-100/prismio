# Graph Report - prismio  (2026-09-30)

## Corpus Check
- 310 files · ~707,717 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 4380 nodes · 7933 edges · 310 communities (301 shown, 9 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 570 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `69720ef8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- malloc
- fn compile_source(path, output_file, run_after_build) -> Int
- g6_bench.c
- ir_symbols.c
- free
- lang_runtime.c
- SECURITY.md
- Borrow Checking
- Prismio — Compiler Audit
- use_globals() function
- g2_bench_arena.c
- bench.py
- ir_intern
- setup_llvm.py
- arena_would_serve
- cyc_hdr
- While Loops
- 1. Language core
- Function Overloading
- main
- main
- generate_embedded_sources.py
- llvm-api-backend.c
- Enum Types
- main
- layout.py
- diagnostics.c
- test_runner.py
- check_source_lists.py
- main() function (test_09_strings)
- compile(input_size)
- bad_value() function (neg_01_type_mismatch)
- Prismio — Compiler Status
- Prismio — Bootstrap & Runtime-Linking Architecture Audit
- World
- main
- Struct (Custom Data Type) Declarations
- aif_tier_of
- main() function (test_07_booleans)
- main() function (test_02_if_else)
- main
- fibonacci(n) function
- main() function (test_11_returns)
- aif_support.c
- main
- Prismio Toolchain Architecture Refactor — Session Handoff
- add_binding
- embedded_sources.h
- g2_bench.c
- strcmp
- strlen
- The G2 / G6 benchmark set
- noop.c
- g5_tuned.rs
- g5_idiomatic.rs
- bench.py
- World
- g3.swift
- g4.swift
- strncpy
- g4_idiomatic.rs
- g3_tuned.rs
- g3_idiomatic.rs
- Building Prismio on macOS (and Linux)
- Cross-language results — Prismio vs Rust vs Swift
- g4_tuned.rs
- find_llvm_paths_ex
- g1_arena.rs
- struct Counter
- struct Res
- g2_cull_probe.c
- aif_str
- Code style
- bootstrap.sh
- verify_separation.sh
- Engine
- package.sh script
- Tier 2 — required by specified AIF features
- bootstrap.ps1
- die
- verify_separation.ps1
- Invoke-Step
- install.ps1
- refresh_seed.ps1
- AIF — Workload Declaration, Cost Model, and Layout Search
- AIF — Design Rationale
- RESULTS-L0-tiers.md
- 5 · A staged path
- 1 · AIF core — genuinely ours
- AIF — The FFI Boundary
- malloc
- AIF — The T4 Cycle Collector
- AIF — Measurement and Falsification Plan
- PIR — Prism Semantic IR
- struct_entry
- AIF — Level 0 Results
- .sites_of
- AIF — Adaptive Inference Framework
- AIF — Cross-Language Comparison Suite
- AIF — Evaluation as a General-Purpose Memory Model
- AIF — Adaptive Inference Framework
- 8.4 Views — slices and element references
- aif.py
- nominal_find
- 5 · Annotations
- AIF — Layout Results (A1)
- AIF — The Inference Engine
- 4 · Transfer rules
- 5 · The fixed-point algorithm
- 7 · Specialisation strategy and dedup
- AIF — Engine/Game Boundary Results (A2)
- AIF Prototype
- rt_prof_slot
- 2 · Fact domains
- 8 · Annotations as axioms and constraints
- 11 · Conformance boundary
- 3 · The tier ladder
- Model
- .solve
- AIF Evidence
- 6 · Ownership contexts
- 2 · The objects of the model
- 4 · Tier derivation
- 7 · Two-speed compilation
- g1_boxed.rs
- AIF Corpus
- 6 · The tier manifest
- Profile
- namelist_contains
- NEXT-SESSION.md
- g5.swift
- aif_manifest_diff.py
- g1_idiomatic.rs
- g2_arena.rs
- g7_idiomatic.rs
- g7_owned.rs
- g1_tuned.rs
- g2_boxed.rs
- RESULTS — the string/parse axis
- g2_idiomatic.rs
- g2_tuned.rs
- Frames
- Arena placement: what `region` serves, and what stops the rest
- v0.1 concurrency — the blocking typed `Channel<T>`, and g9's fifth arm
- 13. Performance
- tokenra
- Boxed `List` replacement ownership
- RESULTS — the string/parse axis
- g7bench.py
- optlevel.py
- aif_tier_of
- Prismio IDE protocol
- Session of 2026-08-13 — `workload` lands; two of LAYOUT 6's dimensions are not blocked on what the brief said
- aif_verify_alloc
- LAYOUT 6's candidate space, measured against what this compiler can emit
- The cross-language suite — Prismio vs Rust vs Swift
- arena_census.py
- HANDOFF.md
- run_data_view_gate_test
- build_from_toolchain_sources
- Session of 2026-08-08 (measurement) — the first cross-language numbers, and the optimiser was never on
- 0.1.0
- v0.1 release candidate — the complete local gate
- ir_snapshot.py
- Releasing Prismio
- g2r_time.py
- release_gate.sh
- Session of 2026-08-17 (second) — §8's forced candidate lands, and the IR differential turns out to have a concurrency hole
- The prompt for the next session
- Session of 2026-08-08 (measurement) — the first cross-language numbers, and the optimiser was never on
- fn_mnemonic_diff.py
- ir_intern
- ir_slot_diff.py
- 10 · Boundaries
- aif_place_arenas
- struct_entry
- block_done
- release.sh
- One flat-List guard per loop, and the tuned-g4 regression it repairs
- g3.swift
- cleanup_files
- run_command
- manifest_records
- 5 · The accepted tradeoffs, reported anyway
- A `spawn`ed call's owned temporary argument now has an owner
- run_check_command_test
- test_runner.py
- 4. Language and module layout
- run_suite.py
- call_edge_push
- fn resolve_imports(module, base_dir) -> ASTNode
- run_aif_layout_test
- run_aif_struct_field_test
- find_binding
- run_aif_stack_slot_test
- add_binding
- noise floor that decided it
- The argument-position release no longer turns on the return's kind
- Known issues
- Ownership survives a second return
- list_new_cap
- Inlining the flat push: rejected, and why the obvious gate does not save it
- fn compile_source(path, output_file, run_after_build) -> Int
- Appendix — M2's closing state, 2026-08-23
- 13. Performance
- Getting Started
- file_exists
- prismio_llvm.h
- Gap 1: sound owner facts at calls, `spawn`, and FFI
- HANDOFF.md
- The generated release loops on its tail self field
- M2.1a — recursive releases for self-referential types (fork (a))
- Worker-ready implementation tasks
- Gap 4: channel runtime ignores endpoint topology
- Concepts
- LLVM IR and final assembly audit
- Gap 6: functional-update reuse is not represented
- Gap 7: temporary allocation extents are still coarse
- std.math: Float's functions, and the three Float codegen bugs under them
- struct_entry
- The two standing rules
- rt_prof_slot
- Source-level and type representation inventory
- Current baseline
- aif_ledger_init
- Ownership, lifetime, and AIF
- Target architecture
- Particle
- Ownership survives a second return
- `list_new` allocates nothing until the first push
- Performance: what is open, and how to measure it
- aif_records
- 2 · Later
- M4.1 — first-class `Slice<T>`
- Prompt 2 (residual) — the hot/cold split, and only that
- arena_emit_range
- list_set
- bracket_place
- M4.4 — generic/container layout specialization
- Boxed `List` replacement ownership
- AIF Evidence
- 13. Performance
- Gap 10: runtime curation has an incomplete dependency closure
- The String surface: operators, properties, iteration
- 3 · Ownership, and the three ways to get it wrong
- An owned call result consumed directly as an argument now has an owner
- A binding that escapes through a callee's return was freed under its caller
- A payload-free enum variant allocated uninitialised memory
- `list_new` allocates nothing until the first push
- E1: the push check belongs in the preheader, and the profile it was said to need does not exist
- run_ums_test
- 6. Naming
- min/max/abs, and the call that used to cost 1.79x
- Target architecture
- sanitizer_smoke.sh
- nominal_find
- Ownership survives a second return
- 3. Before changing code
- 3. Before changing code
- aif_fn_lookup
- prismio_task_spawn
- M4.3b — DataView element reads
- M4.3b — DataView element reads
- run_negative_test
- fs_metadata
- compiler_probe_executable
- The hot element accessor was never curated
- AIF — Engine/Game Boundary Results (A2)
- M4.3c — mutable DataView round trip
- Boxed `List` replacement ownership
- M5.1 — allocator evaluation
- `Int` width — the decision, and the three measurements that made it
- MEM-006: the whole-buffer copy is one `llvm.memmove`, and the benchmark it was aimed at is not a copy benchmark
- measure.py
- MEM-033: the cycle collector stops locking when there is nothing to lock against
- Single-probe updates and direct entry lookup
- `key_value_update`: one probe in `mapSet`, and a loop guard that is a net loss
- LayoutParticle
- 7. Functions and control flow
- Ownership survives a second return
- 15. Working with agents
- Prismio IDE protocol
- 4. Language and module layout
- Results: the string-benchmark gap (2026-09-11)
- measure.py
- phase.cpp
- ablations.sh
- fn_mnemonic_diff.py
- 13. Performance
- 6. Naming
- common.rs
- list_push_inline_scalar_slow
- loop_named
- cost.c
- prismio_task_entry
- Who owns a call's result: asked of the call, not of its allocation site
- Results: `__builtin_string_hash` (2026-09-12)
- Properties are declared: `prop`
- .new_site
- The relational tier, byte-sized Bool elements, and three gaps read from disassembly
- Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs

## God Nodes (most connected - your core abstractions)
1. `resolve_value()` - 87 edges
2. `main()` - 82 edges
3. `intern_value()` - 75 edges
4. `run()` - 66 edges
5. `run_command()` - 56 edges
6. `type_from_key()` - 55 edges
7. `bits_test()` - 47 edges
8. `backend_fail()` - 46 edges
9. `block_done()` - 42 edges
10. `ir_intern()` - 41 edges

## Surprising Connections (you probably didn't know these)
- `Test naming convention (test_<NN>_<description>.psm)` --conceptually_related_to--> `fn main() -> Int`  [AMBIGUOUS]
  CONTRIBUTING.md → src/main.psm
- `run_check_overlay_test()` --calls--> `check()`  [INFERRED]
  tests/test_runner.py → tools/verify_separation.py
- `run_check_command_test()` --calls--> `records()`  [INFERRED]
  tests/test_runner.py → tools/incremental_manifest.py
- `run()` --calls--> `strided_memory()`  [INFERRED]
  benchmarks/cpp/suite.cpp → benchmarks/cpp/adversarial.cpp
- `run()` --calls--> `dependency_chain()`  [INFERRED]
  benchmarks/cpp/suite.cpp → benchmarks/cpp/adversarial.cpp

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Negative tests validating move/drop/borrow ownership checking** — tests_neg_03_use_after_move_main, tests_neg_04_use_after_drop_main, tests_neg_05_drop_borrow_main [INFERRED 0.85]
- **Negative tests validating semantic/type checking (type mismatch, integer width, duplicate overload)** — tests_neg_01_type_mismatch_bad_value, tests_neg_02_int_width_main, tests_neg_06_duplicate_overload_same [INFERRED 0.75]
- **Shared fail(message) test-harness helper pattern across feature tests** — tests_test_01_variables_fail, tests_test_02_if_else_fail, tests_test_03_while_loops_fail, tests_test_04_structs_fail, tests_test_05_enums_fail, tests_test_06_recursion_fail, tests_test_07_booleans_fail, tests_test_08_mutability_fail, tests_test_09_strings_fail, tests_test_10_expressions_fail, tests_test_11_returns_fail, tests_test_12_imports_fail, tests_test_13_globals_fail [INFERRED 0.95]
- **Prismio Ownership System (Move/Drop/Borrow) Demonstration** — tests_test_23_move_main, tests_test_24_drop_main, tests_test_25_conventions_main, tests_test_26_borrow_reuse_main [INFERRED 0.85]

## Communities (310 total, 9 thin omitted)

### Community 0 - "malloc"
Cohesion: 0.02
Nodes (48): aif_call_edge(), aif_call_opaque(), aif_check_pins(), aif_con_arg(), aif_con_bind(), aif_con_borrow(), aif_con_escape_caller(), aif_con_escape_global() (+40 more)

### Community 1 - "fn compile_source(path, output_file, run_after_build) -> Int"
Cohesion: 0.18
Nodes (10): Contributor Covenant Code of Conduct, Conventional Commits convention, Prismio Project Structure (src/ layout), Claim: no dedicated semantic analysis pass (planned), Test naming convention (test_<NN>_<description>.psm), Contributor Covenant (README reference), extern fn cli_arg, extern fn cli_arg_count (+2 more)

### Community 2 - "g6_bench.c"
Cohesion: 0.03
Nodes (66): check_llvm_version(), codegen_partition_count(), codegen_thread_budget(), debug_dispose(), default_target_cpu(), emit_trace_enabled(), emit_trace_ms(), emit_trace_stage() (+58 more)

### Community 3 - "ir_symbols.c"
Cohesion: 0.06
Nodes (31): cleanup_files(), The analysis-only IDE boundary and its versioned JSON Lines output., REQUIREMENTS 10, applied to the one module every build shares: the runtime., The T0 path has to be checked in the IR, not only in the output: falling     bac, AIF Level 5, checked in the IR because neither half shows in a value.      The n, SPEC 8.4's E-VIEW, checked in the manifest and in the IR.      Both halves are l, M4.1's discriminating representation, lifetime, and bounds gate., M4.3's real-column, mutable round-trip, alias, and release gate. (+23 more)

### Community 4 - "free"
Cohesion: 0.04
Nodes (44): RtProfField, RtProfType, list_get(), list_get_inline(), list_get_inline_scalar(), list_set_inline_scalar(), list_set_unstamped(), list_slice_get() (+36 more)

### Community 5 - "lang_runtime.c"
Cohesion: 0.07
Nodes (52): CallEdge, aif_arena_blockers(), aif_arena_high_water(), aif_arena_range_first(), aif_arena_range_last(), aif_arena_unsized_sites(), aif_auto_arena_at_node(), aif_bracket_callee() (+44 more)

### Community 7 - "Borrow Checking"
Cohesion: 0.08
Nodes (30): Borrow Checking, Drop Semantics, Move Semantics, Parameter Passing Conventions (borrow/inout/sink), Struct Types, main() function (neg_03_use_after_move), struct Point (neg_03_use_after_move), main() function (neg_04_use_after_drop) (+22 more)

### Community 8 - "Prismio — Compiler Audit"
Cohesion: 0.05
Nodes (50): aif_con_pin_region(), aif_elem_key(), aif_enum_new(), aif_extern_contract(), aif_extern_contract_set(), aif_field_access(), aif_field_has_range(), aif_field_range_bytes() (+42 more)

### Community 9 - "use_globals() function"
Cohesion: 0.09
Nodes (27): Arithmetic Operators, Global Variables, Mutability (mut bindings), Operator Precedence / Expression Evaluation, Variable Declarations, bump_global(amount) function, fail(message) function (test_01_variables), main() function (test_01_variables) (+19 more)

### Community 10 - "g2_bench_arena.c"
Cohesion: 0.14
Nodes (36): LLVMBasicBlockRef, block_done(), block_for(), element_from_memory(), element_memory_type(), element_to_memory(), flat_element_address(), ir_br_numbered() (+28 more)

### Community 11 - "bench.py"
Cohesion: 0.08
Nodes (62): byte_gep(), coerce_for(), global_named(), intern_value(), ir_alloca(), ir_array_copy_into(), ir_array_copy_key(), ir_array_load() (+54 more)

### Community 12 - "ir_intern"
Cohesion: 0.12
Nodes (29): NodeArgs, aif_arena_at_node(), aif_call_arg_outlives_call(), aif_cycle_at_node(), aif_elem_owner_at_node(), aif_elem_type_at_node(), aif_field_is_counted(), aif_frees_at_scope_node() (+21 more)

### Community 13 - "setup_llvm.py"
Cohesion: 0.08
Nodes (33): NamedValue, backend_fail(), const_from_text(), grow_table(), ir_array_literal_elem(), ir_br(), ir_call_begin(), ir_cond_br() (+25 more)

### Community 14 - "arena_would_serve"
Cohesion: 0.11
Nodes (29): adversarial_next(), AdversarialObject, a, b, c, d, allocation_escape(), aos_vs_soa() (+21 more)

### Community 15 - "cyc_hdr"
Cohesion: 0.07
Nodes (27): append_joined_argument(), append_quoted_argument(), compiler_host_stamp_matches(), compiler_host_stamp_write(), compiler_link_append_argument(), compiler_link_file(), compiler_link_framework(), compiler_link_library() (+19 more)

### Community 16 - "While Loops"
Cohesion: 0.21
Nodes (13): While Loops, Range-Based For Loops (a..b), factorial(n) function, fail(message) function (test_03_while_loops), main() function (test_03_while_loops), sum_to_n(n) function, count_to(limit), fail(message) (+5 more)

### Community 17 - "1. Language core"
Cohesion: 0.05
Nodes (12): drop_index(), ir_drop_kind(), ir_drop_slot(), ir_drop_type(), ir_loop_break_label_named(), ir_loop_continue_label_named(), ir_loop_drop_floor(), ir_loop_drop_floor_named() (+4 more)

### Community 18 - "Function Overloading"
Cohesion: 0.27
Nodes (12): Function Overloading, main() function (neg_06_duplicate_overload), same(value: Int) function, first declaration (neg_06_duplicate_overload), same(other: Int) function, duplicate declaration (neg_06_duplicate_overload), choose(value: Float), choose(value: Int), choose(value: String), combine(left: Int, right: Int) (+4 more)

### Community 19 - "main"
Cohesion: 0.23
Nodes (12): Module Imports, Multi-Argument Function Calls, fail(message) function (test_12_imports), main() function (test_12_imports), add3(a,b,c), add4(a,b,c,d), add5(a,b,c,d,e), fail(message) (+4 more)

### Community 20 - "main"
Cohesion: 0.25
Nodes (8): Driver/Runtime Split (OS-level extern functions), extern fn command_quote_arg, extern fn executable_directory, fail(message), extern fn file_exists, extern fn join_path, main(), extern fn str_length

### Community 21 - "generate_embedded_sources.py"
Cohesion: 0.08
Nodes (17): AIF Evidence, Before quoting any number, Judgement, Measured, Projected, not measured, 1 · How it was found, 2 · The defect, 3 · The fix, and why only one of the three (+9 more)

### Community 22 - "llvm-api-backend.c"
Cohesion: 0.12
Nodes (44): Deriv, aif_oom(), bits_clear(), bits_count_at_least_two(), bits_ensure(), bits_free(), bits_is_empty(), bits_or() (+36 more)

### Community 23 - "Enum Types"
Cohesion: 0.24
Nodes (11): Enum Types, Pattern Matching (match expressions), enum Color, enum ExitCode, fail(message) function (test_05_enums), main() function (test_05_enums), classify(n), enum Color (+3 more)

### Community 24 - "main"
Cohesion: 0.15
Nodes (13): String Runtime (extern str_* FFI functions), fail(message), extern fn int_to_str, main(), extern fn str_char_at, extern fn str_concat, extern fn str_contains, extern fn str_equals (+5 more)

### Community 25 - "layout.py"
Cohesion: 0.06
Nodes (36): find_prismio_exe(), main(), parse_runner_args(), Select fixtures by exact stem first, then by case-insensitive substring., `check --overlay` and `--module`: one file of a program, checked as the editor s, Nothing may take ordinal 0 in NodeKind or TypeKind.      A source check, because, The element-ownership mode is one wire protocol with three definitions.      Cod, The compiler and `aif/prototype/aif.py` must know the same builtins.      The di (+28 more)

### Community 26 - "diagnostics.c"
Cohesion: 0.06
Nodes (32): 0 · The answer, 10.1 · Emptying a function body without a `deleteBody`, 10.2 · Checked against the tool it replaces, 10.3 · It is also cheaper, 10.4 · The corpus, re-measured after the port, 10 · The merge moves in process, and the last blocker goes, 11.1 · Why neither option was the answer, 11.2 · What the corpus actually still called, and the false lead (+24 more)

### Community 27 - "test_runner.py"
Cohesion: 0.06
Nodes (32): 1 · Headline findings, 2.1 The invariant needs a boundary the spec does not currently draw, 2.2 Structs are affine references, not values, 2 · Frozen items, one by one, 3.1 What isn't behind the seam at all, 3 · The seam, precisely, 4.1 A pass between sema and codegen, 4.2 Scope-based drop (+24 more)

### Community 28 - "check_source_lists.py"
Cohesion: 0.06
Nodes (7): append_module_name(), directory_exists(), fs_list_begin(), fs_list_end(), fs_list_push(), list_modules(), make_directory()

### Community 29 - "main() function (test_09_strings)"
Cohesion: 0.48
Nodes (7): FFI / Extern Function Declarations, String Operations, fail(message) function (test_09_strings), main() function (test_09_strings), extern fn str_concat(s1, s2), extern fn str_equals(s1, s2), extern fn str_length(s)

### Community 30 - "compile(input_size)"
Cohesion: 0.33
Nodes (7): Function Composition / Pipeline Simulation, compile(input_size), create_token(t,v,l), fail(message), main(), parse(token_count), tokenize(input)

### Community 31 - "bad_value() function (neg_01_type_mismatch)"
Cohesion: 0.33
Nodes (7): Fixed-Width Integer Typing, Static Type Checking, bad_value() function (neg_01_type_mismatch), main() function (neg_01_type_mismatch), main() function (neg_02_int_width), fail(message), main()

### Community 32 - "Prismio — Compiler Status"
Cohesion: 0.16
Nodes (28): fm_get_or(), fm_init(), fm_probe(), fm_rehash(), fm_set(), im_get_or(), im_init(), im_probe() (+20 more)

### Community 33 - "Prismio — Bootstrap & Runtime-Linking Architecture Audit"
Cohesion: 0.07
Nodes (30): 10.1 The cache model has no associativity and no conflict misses, 10.2 `HandleCost` is a placeholder, 10.3 Profiles age, 10.4.1 A fabricated instance count decides the cache tier, and therefore the layout, 10.4 Static frequency estimation is crude, 10.5 One profile, one target, 10 · Known weaknesses, 1 · The key reframing (+22 more)

### Community 34 - "World"
Cohesion: 0.11
Nodes (31): build_one_sexpr(), build_tree(), BenchTree, string, unique_ptr, vector, edit_distance(), eval_sexpr_ast() (+23 more)

### Community 35 - "main"
Cohesion: 0.47
Nodes (5): Array Types (1D/2D indexing), array_sum(), fail(message), main(), matrix_diagonal()

### Community 36 - "Struct (Custom Data Type) Declarations"
Cohesion: 0.40
Nodes (6): Struct (Custom Data Type) Declarations, struct Parser, struct Token, struct Point, struct Point, struct Item

### Community 37 - "aif_tier_of"
Cohesion: 0.16
Nodes (12): BoundedQueue, cap_, closed_, mu_, not_empty_, not_full_, queue_, channel_pipeline() (+4 more)

### Community 38 - "main() function (test_07_booleans)"
Cohesion: 0.50
Nodes (5): Boolean Logic, fail(message) function (test_07_booleans), is_between(n) function, main() function (test_07_booleans), test_equal(a, b) function

### Community 39 - "main() function (test_02_if_else)"
Cohesion: 0.50
Nodes (5): If/Else Conditionals, fail(message) function (test_02_if_else), main() function (test_02_if_else), max(a, b) function, test_nested_if(x) function

### Community 40 - "main"
Cohesion: 0.60
Nodes (5): Float Arithmetic & Comparisons (f64), blended(offset), comparisons(value), fail(message), main()

### Community 41 - "fibonacci(n) function"
Cohesion: 0.70
Nodes (5): Recursion, fail(message) function (test_06_recursion), fibonacci(n) function, gcd(a, b) function, main() function (test_06_recursion)

### Community 42 - "main() function (test_11_returns)"
Cohesion: 0.50
Nodes (5): Return Statements / Early Return, classify_number(n) function, early_return(x) function, fail(message) function (test_11_returns), main() function (test_11_returns)

### Community 43 - "aif_support.c"
Cohesion: 0.09
Nodes (42): diag_add_file(), diag_detect_color(), diag_digits(), diag_elapsed(), diag_emit(), diag_emit_json(), diag_emit_json_summary(), diag_env_set() (+34 more)

### Community 44 - "main"
Cohesion: 0.67
Nodes (3): Generic Collections (List<T>), fail(message), main()

### Community 45 - "Prismio Toolchain Architecture Refactor — Session Handoff"
Cohesion: 0.41
Nodes (11): ch_close(), ch_init(), main(), recv(), relax(), s1(), s2(), send() (+3 more)

### Community 46 - "add_binding"
Cohesion: 0.11
Nodes (20): arena_current_slot(), data_view_add_column(), data_view_begin(), data_view_check_index(), data_view_finish(), data_view_release(), data_view_to_list(), list_new() (+12 more)

### Community 47 - "embedded_sources.h"
Cohesion: 0.19
Nodes (28): Actor, apply_orders(), arena_alloc(), arena_reserve(), arena_reset(), List, list_free_all(), list_new() (+20 more)

### Community 48 - "g2_bench.c"
Cohesion: 0.20
Nodes (9): Block partitioning in `sort`, `Key for String`, a word at a time, `list_swap`, called directly, Results: the string-performance follow-ups (2026-09-11), `s_expression_parse`'s arms are not the same program, `sort()` from a packaged `.plib`, `sortBy` on flat structs, and `list_set` within one flat list, `String.compare`, step one: the builtin, unused (+1 more)

### Community 49 - "strcmp"
Cohesion: 0.07
Nodes (28): 10. Per-module optimisation levels **[specified 2026-08-17, not implemented]**, 11. `verify` build mode **[needed]**, 12. Handles instead of raw pointers **[needed, long-horizon]**, 13. Generic containers — `Map<K,V>`, growable `Vec<T>` — **PARTLY DONE, 2026-08-19**, 14. Error handling — tagged unions, `Option` / `Result` — **DONE, 2026-08-19**, 15. Concurrency / task model — **DONE, 2026-08-19**, 16. Fix superlinear compile time — **DONE, 2026-08-17**, 17. `Int` ↔ `Float` conversion **[minor]** (+20 more)

### Community 50 - "strlen"
Cohesion: 0.21
Nodes (13): absolute_directory(), compiler_prepare_output_path(), compiler_temp_ir_path(), compiler_temp_obj_path(), compiler_temp_path(), compiler_temp_path_for(), compiler_temp_private_path(), ensure_directory_exists() (+5 more)

### Community 51 - "The G2 / G6 benchmark set"
Cohesion: 0.21
Nodes (27): LLVMMetadataRef, diag_file_count(), diag_file_path(), di_basic(), di_cache(), di_cached(), di_data_element_type(), di_enum_type() (+19 more)

### Community 52 - "noop.c"
Cohesion: 0.22
Nodes (8): 1 · What the first slice broke, 2 · Why, 3 · The change, 4 · Result, 5 · Cost, still uneven and still real, 6 · Two things this cost to find, 7 · What the gate could not see, and what to do about it, One flat-List guard per loop, and the tuned-g4 regression it repairs

### Community 53 - "g5_tuned.rs"
Cohesion: 0.07
Nodes (25): 0 · Why this file exists, 1 · The measurement, 2 · What was wrong: `str_substring` rescans the whole buffer, 3 · The compiler itself, 4 · What did *not* move, and why that is the finding, 5 · What this changes about the ranking, RESULTS — the string/parse axis, The fix, and why it is only half of one (+17 more)

### Community 54 - "g5_idiomatic.rs"
Cohesion: 0.05
Nodes (39): Adversarial benchmark design, Catalog by category, Coverage, Currently Unsupported by Prismio, Infrastructure changes, Interpretation cautions, Original g1-g9 audit, Prismio performance benchmarks (+31 more)

### Community 55 - "bench.py"
Cohesion: 0.08
Nodes (26): 0 · The one-paragraph answer, 10 · Reproducing, 1 · The full matrix, 2 · Prediction → session-3 measurement → now, per axis, 3 · The claim, stated the way the numbers support it, 4 · `region` on g2: session 3's sharpest negative result is fixed, 5.1 · The residual — the only design number, and it held, 5.2 · Executable size — still a large win, and it grew (+18 more)

### Community 56 - "World"
Cohesion: 0.13
Nodes (21): adversarial_next(), AdversarialObject, allocation_escape(), branch_mispredict(), consume_adversarial_object(), dead_code_elimination(), dead_kernel(), function_call_overhead() (+13 more)

### Community 57 - "g3.swift"
Cohesion: 0.14
Nodes (10): LiveProgress, progress(), Thread-safe live progress meter for the test suite.      In interactive terminal, Record and display one finished test result., Map `fn` over `items` in a thread pool, printing each result as it lands.      T, A `sys.stdout` that routes each worker thread's writes to its own buffer.      W, run_parallel(), _ThreadOut (+2 more)

### Community 58 - "g4.swift"
Cohesion: 0.15
Nodes (15): aif_check_placement_pins(), aif_fn_name(), aif_fn_symbol(), aif_nominal_name(), aif_order_symbol(), aif_profile_source(), aif_region_name_at_site(), aif_scope_region() (+7 more)

### Community 59 - "strncpy"
Cohesion: 0.35
Nodes (25): bad(), bootstrap(), check_corpus(), check_cross_target(), check_differential(), check_environment_switch(), check_fixpoint(), check_generations() (+17 more)

### Community 60 - "g4_idiomatic.rs"
Cohesion: 0.29
Nodes (6): Benchmarks, Checks, IR, Results: LLVM 22.1.8 to 23.1.1 (2026-09-17), What changed in the code, What the upgrade showed about the toolchain

### Community 61 - "g3_tuned.rs"
Cohesion: 0.09
Nodes (23): AIF — Design Rationale, Arena placement is a cost decision; `region` is a pin on it, Bake the static region, not the heap, C1, C10, C11, C2, C3 (+15 more)

### Community 62 - "g3_idiomatic.rs"
Cohesion: 0.14
Nodes (13): 1. Command-step arguments are interpreted by the shell *(reproduced)*, 2. `toolchain.host` executes a committed binary on every command *(reproduced)*, 3. `run` cannot pass arguments, and a program's exit status is lost *(reproduced)*, 4. `--release` changes the directory and nothing else *(reproduced)*, 5. Command steps run in the invoker's directory, not the project root *(reproduced)*, P0 — must fix before a user release, P1 — correctness and robustness, P2 — user experience and consistency (+5 more)

### Community 63 - "Building Prismio on macOS (and Linux)"
Cohesion: 0.22
Nodes (21): bench_next_random(), Key, cost_ns(), displacement(), keys_ids(), keys_sort_strings(), main(), mix_a() (+13 more)

### Community 64 - "Cross-language results — Prismio vs Rust vs Swift"
Cohesion: 0.12
Nodes (21): base_type(), bracket_masks(), elem_key(), ffi_arena_cannot_serve(), main(), measure_masks(), SPEC 5.2.1: per function, may a caller's `region` bracket a call to it?      The, The counts the differential compares against `prismio aif --summary`.      **`re (+13 more)

### Community 65 - "g4_tuned.rs"
Cohesion: 0.12
Nodes (21): _di_composite(), _di_located_lines(), _di_located_spans(), _di_nodes(), _di_scope_file(), _di_tuple(), _emitted_struct(), _expected_layout() (+13 more)

### Community 66 - "find_llvm_paths_ex"
Cohesion: 0.10
Nodes (21): 1 · AIF core — genuinely ours, 2 · AIF's stake in language features it does not own, 3 · Compiler requirements AIF genuinely has, 4 · Measurement, 5 · Not AIF — recorded, then handed over, 6 · Over-built — defer or cut, A3. Realised context counts *(measurement)*, A4. Arena high-water marks *(measurement)* (+13 more)

### Community 67 - "g1_arena.rs"
Cohesion: 0.12
Nodes (10): Engine, Where a value assigned to `name` has to stay alive until., Does this expression contain `join <name>`?          Stops at any statement kind, The statement list under a block child slot, or [] when absent., Some path through this statement leaves the scope without joining.          `in_, Every path through this statement joins., Every path through this chain joins before control leaves it.          The escap, Mark every `let t = spawn ...` in this chain that is joined before the         c (+2 more)

### Community 70 - "g2_cull_probe.c"
Cohesion: 0.10
Nodes (21): 10 · Reporting, 1 · The one place being wrong is unsafe, 2 · C-compatible layout, 3.1 The four cases, 3.2 Copy direction, 3.3 What is never copied, 3 · When a copy is mandatory, 4 · The cost model does the work (+13 more)

### Community 71 - "aif_str"
Cohesion: 0.10
Nodes (32): diag_file_module(), find_struct(), ir_caller_can_access_extern(), ir_caller_extern_hidden_level(), ir_extern_decl_record(), ir_file_declares_extern(), ir_file_imports_module(), ir_get_enum_variant() (+24 more)

### Community 72 - "Code style"
Cohesion: 0.07
Nodes (52): compare(), main(), parse_bracketing(), parse_compiler(), parse_oracle(), parse_threads(), A copy of `compiler` whose basename is not `prismio`, beside the original., run() (+44 more)

### Community 73 - "bootstrap.sh"
Cohesion: 0.17
Nodes (33): adopt(), build_zstd(), download(), exe(), extract(), is_bitcode(), llvm_config(), log() (+25 more)

### Community 74 - "verify_separation.sh"
Cohesion: 0.11
Nodes (35): binary_search_work(), dijkstra_shortest_path(), lz4_compress(), sort_strings(), bench_next_random(), band_sum(), blake3_chunk(), bytecode_interpreter() (+27 more)

### Community 75 - "Engine"
Cohesion: 0.17
Nodes (12): 1 · For 0.1, 2 · Where it stands, 3 · Design, 4 · Phases, 5 · Alternatives considered and set aside, 6 · Acceptance, before calling channels production-ready, 7 · Decisions still needed, Channels: what 0.1 needs, and the production design after it (+4 more)

### Community 76 - "package.sh script"
Cohesion: 0.11
Nodes (27): ctz64(), aif_field_is_cyclic(), aif_field_release(), aif_fn_lookup(), aif_fn_may_return_param(), aif_fn_may_return_view_of_param(), aif_param_reusable(), aif_type_acyclic() (+19 more)

### Community 77 - "Tier 2 — required by specified AIF features"
Cohesion: 0.23
Nodes (7): 1 · Result, 2 · The boundary is cheap because the API is handle-based, 3 · Most of the sealing loss is recoverable with contracts, 4 · A prototype bug worth recording, 5 · Compiler bug found: `List<Int>` miscompiles, 6 · What this does not show, AIF — Engine/Game Boundary Results (A2)

### Community 78 - "bootstrap.ps1"
Cohesion: 0.14
Nodes (6): band_sum(), BenchSphere, fft(), fft_transform(), parallel_reduction(), Particle

### Community 79 - "die"
Cohesion: 0.25
Nodes (7): Found on the way, Plain-data channels copy through the ring, Reproduce, The pointer path's ledger (same day), The result, Tried, and not levers, What was built

### Community 80 - "verify_separation.ps1"
Cohesion: 0.15
Nodes (19): Constraint, IntVec, NodeCall, vec_push(), aif_argv_push(), aif_call_arg_retained(), aif_owns_call_result_at_node(), call_fn_result_held() (+11 more)

### Community 81 - "Invoke-Step"
Cohesion: 0.17
Nodes (12): A command is manifest data; which names are free is not, Current limitations, Decisions, Generated state is project-local and isolated, Host selection is a stable prefix, Incremental-build extension seam, Module boundaries, Next implementation sequence (+4 more)

### Community 82 - "install.ps1"
Cohesion: 0.11
Nodes (17): 1 · Handles did not land, and two dimensions depend on them, 2.1 · It was built on 2026-08-17, and the corpus does not reproduce the 0.87×, 2.2 · The cost model chose two layouts the measurement rejected, and both reasons are nameable, 2.3 · The compiler self-hosted with a split AST, and then stopped splitting it, 2 · Hot/cold does *not* need handles, and it pays, 3 · Bit-packing is blocked by the specification, not by codegen, 4.1 · Both blockers are gone, and the remaining piece is a search loop, 4 · Empirical validation (LAYOUT §8) is behind §7.2, not behind the runner (+9 more)

### Community 83 - "refresh_seed.ps1"
Cohesion: 0.11
Nodes (17): 1. Every program that printed a number leaked, 2. g6 was not blocked on the obligation the notes said it was, 2a. Regime (a) asked the wrong question, 2b. Shared-body bit on bodies that allocate nothing, 2c. Every `List` in the program shared one element node, 3. The corpus, 4. Four tests changed meaning, and why that is the system working, 5.1 g3's 4095 — and the recorded cause was wrong (+9 more)

### Community 84 - "AIF — Workload Declaration, Cost Model, and Layout Search"
Cohesion: 0.15
Nodes (10): escape_join(), escape_le(), Flatten a value-set expression against the current points-to state., SPEC 8.4. The collections whose lifetime this value set depends on:         its, SPEC 8.4 E-VIEW:  v is a view of c  =>  E(c) ⊒ E(v).          Applied wherever a, Every rule that writes pt or holders reads only pt, so points-to has         a l, Round-synchronous (Jacobi) iteration, per INFERENCE 5.1: every round         rea, Records s in this round's delta and returns True, so a rule reads         `chang (+2 more)

### Community 85 - "AIF — Design Rationale"
Cohesion: 0.11
Nodes (18): 10 · What still needs measurement, 1 · What is actually in scope, 2 · The headline result, 3.1 Why trial deletion and not tracing, 3.2 The procedure, 3 · Algorithm, 4 · The cyclic-edge restriction, 5 · Object header (+10 more)

### Community 86 - "RESULTS-L0-tiers.md"
Cohesion: 0.14
Nodes (18): allocation_mutation(), build_memory_tree(), BenchTree, unique_ptr, large_buffer_copy(), memory_tree_sum(), MemoryParticle, life (+10 more)

### Community 87 - "5 · A staged path"
Cohesion: 0.17
Nodes (9): gcd_lcm(), gcd_value(), merge_range(), mergesort_work(), quick_range(), quicksort_work(), random_values(), Vec (+1 more)

### Community 88 - "1 · AIF core — genuinely ours"
Cohesion: 0.20
Nodes (21): CycHeader, cyc_alloc(), cyc_buffer(), cyc_collect(), cyc_collect_now(), cyc_collect_white(), cyc_collections_run(), cyc_enter() (+13 more)

### Community 89 - "AIF — The FFI Boundary"
Cohesion: 0.11
Nodes (18): aif_records(), aif_thread_records(), manifest_records(), symbol -> (tier, thread) from a manifest run., INFERENCE 4.3's thread module, one fixture function per rule.      The `T` domai, SPEC 5.2 / 5.2.1 / 5.2.1.1 -- the arena diagnostics, and which regions the     w, SPEC 5.4 applied to placement -- `pin(<region-name>)` can fail a build.      **T, SPEC 5.4 -- a honoured pin freezes the tier, and only where the mechanism     ex (+10 more)

### Community 90 - "malloc"
Cohesion: 0.12
Nodes (17): 1 · The methodological point that matters most, 2.1 Definitions, 2.2 The claim under test, 2.3 False sharing from field insensitivity, 2 · Primary metric: tier distribution, 3.1 B1 is a weak headline and should not be the first result, 3.2 Baselines, 3 · Benchmark programs (+9 more)

### Community 91 - "AIF — The T4 Cycle Collector"
Cohesion: 0.26
Nodes (13): candidates(), field_align(), field_width(), Layout, main(), min_size(), mu_for(), grouping in {AoS, SoA, AoSoA(w)}; `hot` is the field subset kept in the     prim (+5 more)

### Community 92 - "AIF — Measurement and Falsification Plan"
Cohesion: 0.08
Nodes (45): build_all(), build_key(), color_enabled(), command_text(), elimination_benchmarks(), elimination_cell(), elimination_row(), execute() (+37 more)

### Community 93 - "PIR — Prism Semantic IR"
Cohesion: 0.14
Nodes (16): DeclEntry, GuardSafeNode, add_binding(), decl_entry(), guard_safe_entry(), hash_str(), ir_decl_at(), ir_decl_count() (+8 more)

### Community 94 - "struct_entry"
Cohesion: 0.21
Nodes (17): PrismioPlib, codegen_uses_clang(), compiler_build_executable(), compiler_installed_runtime_hash(), compiler_link_inputs_supported(), extract_plib_bitcode(), find_in_lib_dir(), find_runtime_bitcode() (+9 more)

### Community 95 - "AIF — Level 0 Results"
Cohesion: 0.15
Nodes (22): RtList, list_check_insert_index(), list_copy_elem(), list_discard_slot(), list_insert(), list_insert_inline(), list_insert_inline_scalar(), list_insert_str() (+14 more)

### Community 96 - ".sites_of"
Cohesion: 0.20
Nodes (9): A bug worth remembering, Binary size and compile time against C++ and Rust (2026-09-28), Internal linkage changes inlining, both ways, Residuals, measured and not fixed, Second round, Verification, What changed, Where it stands (+1 more)

### Community 97 - "AIF — Adaptive Inference Framework"
Cohesion: 0.19
Nodes (19): AifLive, aif_ledger_enter(), aif_ledger_leave(), aif_live_hash(), aif_trace_enabled(), aif_trace_print(), aif_verify_alloc(), aif_verify_arm() (+11 more)

### Community 98 - "AIF — Cross-Language Comparison Suite"
Cohesion: 0.13
Nodes (15): 1 · Why bodies must ship, 2.1 Not LLVM IR, 2 · Content model, 3 · Deterministic emission, 4 · Merging, 5.1 Sealed surfaces SHALL publish ownership contracts, 5 · Sealed functions, 6.1 Format versioning (+7 more)

### Community 99 - "AIF — Evaluation as a General-Purpose Memory Model"
Cohesion: 0.06
Nodes (60): CallFrame, LLVMAttributeIndex, LLVMContextRef, LLVMLinkage, LLVMModuleRef, LLVMValueRef, PartitionJob, apply_borrow_attrs() (+52 more)

### Community 100 - "AIF — Adaptive Inference Framework"
Cohesion: 0.38
Nodes (7): FILE, PrismioPlibSection, compiler_plib_interface(), plib_empty(), plib_read_sections(), read_u32_le(), read_u64_le()

### Community 101 - "8.4 Views — slices and element references"
Cohesion: 0.21
Nodes (8): build_memory_tree(), memory_tree_sum(), MemoryParticle, recursive_tree_rebuild(), BenchTree, Box, Option, tree_add()

### Community 102 - "aif.py"
Cohesion: 0.37
Nodes (12): RtList, knap_slow_tail(), main(), now_ns(), v0(), v1(), v2(), v3() (+4 more)

### Community 103 - "nominal_find"
Cohesion: 0.15
Nodes (12): 1 · What this closes, 2 · The defect was documented, deliberate, and had stopped being true, 3 · The mechanism, 4 · The two things that cost the most to find, 5 · The fixture, and how it nearly measured nothing, 6 · Timing, 7 · What is left, measured, Appendix — M2's closing state, 2026-08-23 (+4 more)

### Community 104 - "5 · Annotations"
Cohesion: 0.22
Nodes (5): Profile, Collect (owner_type, field, is_write) for every member access in a         subtr, Names incremented by a literal inside the loop -- i.e. the induction         var, Extracted entirely from the AST. Every attribute LAYOUT 2.1 marks     'static, e, Traversal

### Community 105 - "AIF — Layout Results (A1)"
Cohesion: 0.38
Nodes (10): alpha(), byte_sum(), string, digit(), file_read(), file_write(), line_processing(), read_file() (+2 more)

### Community 106 - "AIF — The Inference Engine"
Cohesion: 0.15
Nodes (13): 0 · The diagnosis, and the one thing everybody had backwards, 1 · Close the runtime seam — built, with one deployment decision left, 2 · Reuse analysis — useful only where the program has its trigger shape, 3 · Regions: go non-lexical and polymorphic, 4 · Views and slices — bounded views and mutable data views shipped, 5 · The allocator — measured and closed for the current workload, 6 · The ranked plan, 7 · Measured dead ends — do not re-derive these (+5 more)

### Community 107 - "4 · Transfer rules"
Cohesion: 0.27
Nodes (12): LLVMTypeRef, array_base(), array_copy_bytes(), array_slot(), existing_global_of_type(), ir_array_alloca(), ir_array_alloca_zeroed(), ir_array_copy() (+4 more)

### Community 108 - "5 · The fixed-point algorithm"
Cohesion: 0.15
Nodes (12): LLVMOpaqueAttributeRef, LLVMOpaqueBasicBlock, LLVMOpaqueBuilder, LLVMOpaqueContext, LLVMOpaqueError, LLVMOpaqueMetadata, LLVMOpaqueModule, LLVMOpaquePassBuilderOptions (+4 more)

### Community 109 - "7 · Specialisation strategy and dedup"
Cohesion: 0.15
Nodes (12): Codegen, Concurrency, Known issues, Language surface, Measurement, if you are benchmarking this, Naming, Ownership, Platform (+4 more)

### Community 110 - "AIF — Engine/Game Boundary Results (A2)"
Cohesion: 0.17
Nodes (11): 1.1 What was actually quadratic, 1 · The frontend was quadratic in module size, and is now linear, 2.1 AIF's whole fixed point is 18 ms, 2 · The frontend is 4% of a cold build, 3.0 What a small build is now made of, 3.1 The compiler's own self-build, 3 · Cold and incremental, 4 · The toolchain object cache (+3 more)

### Community 111 - "AIF Prototype"
Cohesion: 0.17
Nodes (12): 1 · Headline, 2 · The finding: one decision accounts for the entire residue, 3 · What the game corpus showed that the compiler could not, 3a · Handles appear to eliminate T3 in engine code, 4.1 `retain_in(k)` is missing from FFI.md's contract vocabulary, 4.2 The cycle collector has no program that can exercise it, 4 · Two spec gaps the run found, 5 · Secondary measurements (+4 more)

### Community 112 - "rt_prof_slot"
Cohesion: 0.05
Nodes (39): emitted_layout_for(), The AIF memory model's tier derivation, one fixture per SPEC 4.2 clause.      As, Regime (a) keeps a per-iteration allocation out of the caller's region.      `pe, The default is an interactive explanation; the manifest is explicit.      This f, SPEC 6.2 / 11 item 8 -- every record the manifest emits must be a record     the, M3.2 -- an arena bracketed between statements rather than at the braces.      `g, LAYOUT 5's cost model ranks hot/cold cuts, and ranks them by cost rather     tha, LAYOUT 6's hot/cold split -- the release half, checked by running it.      A spl (+31 more)

### Community 113 - "2 · Fact domains"
Cohesion: 0.17
Nodes (11): 10 · Task 1.3 (MEM-011), curating `list_push_slot`: it works, and it loses, 1 · The bug, 2 · The fix, in three parts, 3 · What the exact bound unlocked, 4 · The regression the exact bound exposed, and why it was not the bound's fault, 5 · Measured, 6 · Totality, 7 · The TBAA audit (MEM-024), in full (+3 more)

### Community 114 - "8 · Annotations as axioms and constraints"
Cohesion: 0.17
Nodes (11): All-g old/new — `build/tbaa3` → `build/m6-rc`, Commands, Five-arm standing, Gate, Generated code before timings, It is the instruction, not the layout, M6 slice 2 — ordinary struct-path TBAA, and the g2 regression it caused, The decline, and why it is this line and not g2's (+3 more)

### Community 115 - "11 · Conformance boundary"
Cohesion: 0.17
Nodes (12): 0.1 · Engine and game remain two workloads, 0 · The actual stack, 1 · The two halves, 2.1 The annotations belong to the engine layer, 2.2 T3 lives in the engine, T0–T2 in the game, 2.3 The engine/game boundary is where whole-program analysis must hold, 2.4 The manifest becomes a contract between teams, 2.5 Optimisation level has to be **per module**, not per build (+4 more)

### Community 116 - "3 · The tier ladder"
Cohesion: 0.20
Nodes (10): posix_spawn_file_actions_t, PrismioSpawnOut, fs_lines_open(), proc_close(), proc_exec(), proc_spawn_run(), spawn_command_line(), spawn_quote_into() (+2 more)

### Community 117 - "Model"
Cohesion: 0.17
Nodes (12): 0 · Conformance language, 12 · What this model gives up *(informative)*, 1.1 What the invariant does not cover, 1 · The invariant, 6.1 Purpose, 6.2 Format, 6.3 Diff semantics, 6 · The tier manifest (+4 more)

### Community 118 - ".solve"
Cohesion: 0.24
Nodes (12): build_one_sexpr(), build_tree(), eval_sexpr_ast(), parse_sexpr_ast(), BenchTree, Box, Option, String (+4 more)

### Community 119 - "AIF Evidence"
Cohesion: 0.13
Nodes (12): binary_search_work(), dijkstra_shortest_path(), lz4_compress(), sort_strings(), next_random(), blake3_chunk(), bytecode_interpreter(), monte_carlo() (+4 more)

### Community 120 - "6 · Ownership contexts"
Cohesion: 0.27
Nodes (11): LineReader, fs_lines_close(), fs_lines_has_line(), fs_lines_reader(), fs_lines_take_line(), io_stdin_has_line(), io_stdin_read_all(), io_stdin_take_line() (+3 more)

### Community 121 - "2 · The objects of the model"
Cohesion: 0.42
Nodes (10): arena_alloc(), arena_reserve(), arena_reset(), build_scene(), List, cull(), list_init(), list_push() (+2 more)

### Community 122 - "4 · Tier derivation"
Cohesion: 0.27
Nodes (8): a_hdr_pair(), a_hdr_scalar(), a_reg_pair(), a_reg_scalar(), best_ms(), main(), slot_header(), slot_reg()

### Community 123 - "7 · Two-speed compilation"
Cohesion: 0.31
Nodes (8): now_ms(), run_boxed_aos(), run_boxed_split(), run_chunked_inline(), run_chunked_split(), run_inline_aos(), run_inline_split(), run_soa()

### Community 124 - "g1_boxed.rs"
Cohesion: 0.44
Nodes (10): key_of(), main(), mg(), mi(), mix(), mp(), mr(), ms() (+2 more)

### Community 125 - "AIF Corpus"
Cohesion: 0.18
Nodes (10): 1 · The design was already at the C ceiling, 2 · Four things that are not the cost, 3 · What it is: a scrambling hash throws away locality, 4 · The fold, and why it is not just the identity, 5 · So the table checks its own hash, 6 · The result, 7 · Verification, 8 · For the next agent (+2 more)

### Community 126 - "6 · The tier manifest"
Cohesion: 0.18
Nodes (10): 1 · The headline, 2 · Why an escape-lattice change does not move this, 3 · The measurement that was wrong twice, and why, 4 · `region` measured on g2, 5 · What a region *can* serve, 6 · `list_new_with_capacity`, the one speed result, 7 · What would actually close this, 8 · How much call-site bracketing could reach *(2026-08-16)* (+2 more)

### Community 127 - "Profile"
Cohesion: 0.18
Nodes (10): A note on `PRISMIO_INLINE_ELEMS=0`, A select, not a branch, Cost, which is real and uneven, Measurement, Reproducing, The change, The flat-list element view: codegen keeps the stride it already computed, What the loop looks like now (+2 more)

### Community 128 - "namelist_contains"
Cohesion: 0.18
Nodes (10): 1 · What was built, 2 · What it measured, 3 · The bug that made a correct analysis measure 1.29x slower, 4 · Two predictions from the C model, and how they held, 5 · What was rejected, 6 · Where the remaining gap actually is, 7 · The bug that hid all of this, 8 · What is left (+2 more)

### Community 129 - "NEXT-SESSION.md"
Cohesion: 0.27
Nodes (9): alpha(), base64_codec(), byte_sum(), csv_parse(), digit(), file_read(), file_write(), space() (+1 more)

### Community 130 - "g5.swift"
Cohesion: 0.18
Nodes (10): Debugging Prismio programs, Part 1 — `-g`, Part 2 — where the memory went, and why, See also, The storage plan — where each site went, `--verify` — did the inference hold?, What `-g` will not tell you, and why, Which tool answers which question (+2 more)

### Community 131 - "aif_manifest_diff.py"
Cohesion: 0.25
Nodes (11): NameList, ir_declare_named_type(), ir_is_borrowed(), ir_is_global_name(), ir_is_moved(), ir_mark_borrowed(), ir_mark_moved(), ir_named_type_kind() (+3 more)

### Community 132 - "g1_idiomatic.rs"
Cohesion: 0.08
Nodes (34): Nominal, bits_test(), Bits, aif_compute_type_acyclic(), aif_layout_cand_bytes(), aif_layout_cand_field_hot(), aif_layout_field(), aif_layout_rank() (+26 more)

### Community 133 - "g2_arena.rs"
Cohesion: 0.20
Nodes (10): 1 · The thesis, stated so it can be killed, 2 · Fairness rules, 3 · The suite, 4 · Isolating the memory-model tax, 5 · Where AIF is predicted to lose, 6 · Predicted results, 7 · Reporting, AIF — Cross-Language Comparison Suite (+2 more)

### Community 134 - "g7_idiomatic.rs"
Cohesion: 0.20
Nodes (10): 1 · The finding that should drive planning, 2 · What holds up as general-purpose, 3 · Where the spec is over-fitted — the 80/20 budget rule, 4 · Regions generalise better than layout, and are under-emphasised, 5 · The biggest hole: closures, 6 · PIR is a heavier liability for general-purpose than for games, 7 · Honest scorecard, 8 · What I would change (+2 more)

### Community 135 - "g7_owned.rs"
Cohesion: 0.20
Nodes (9): Cost, Experiments rejected during this investigation, Gate, Loop versioning exposes Prismio's flat-list fast path, Research-directed next order, Seven-program A/B, The remaining branch, What changed in machine code (+1 more)

### Community 136 - "g1_tuned.rs"
Cohesion: 0.20
Nodes (9): 0. The two halves, and why neither ships alone, 1. The circularity, cut the same way M3.1 cut it, 2. `g2.psm`, unannotated, 3. The corpus, 4. What the IR diff is, all of it, 5. The guard, which was not one, 6. What did not change, and is worth knowing, M3.2c-ii + M3.2d — an arena that opens and closes between statements (+1 more)

### Community 137 - "g2_boxed.rs"
Cohesion: 0.20
Nodes (9): 1 · The baseline, 2 · What was refuted, 3 · Mechanism 1 — self-recursion collapses the root onto a child site, 4 · Mechanism 2 — one parameter-returning path vetoes the whole return set, 5 · What this changes about the plan, 6 · Reproducers, 7 · The fix, `g8_tree_rebuild` leaks 12,282 of 12,284, and it is two mechanisms, not one (+1 more)

### Community 138 - "RESULTS — the string/parse axis"
Cohesion: 0.20
Nodes (9): 1. A module-wide `!alias.scope` pair for header versus elements, 2. `noalias` on the return of the list constructors, E5 · Scoped alias metadata on the list header, For the next agent, Reproduce, Verification, What it costs and what it buys, What was built (+1 more)

### Community 139 - "g2_idiomatic.rs"
Cohesion: 0.20
Nodes (10): AIF — Adaptive Inference Framework, Conformance is graded, Contents, Running the prototype, Start here, Status, The model in one screen, Two things to know before extending this (+2 more)

### Community 140 - "g2_tuned.rs"
Cohesion: 0.10
Nodes (30): accept_if_exists(), clang_identity(), compiler_binary_hash(), compiler_check_executable(), compiler_check_host_abi(), compiler_emit_local_toolchain(), compiler_forward_cli(), compiler_hosted_env_begin() (+22 more)

### Community 141 - "Frames"
Cohesion: 0.20
Nodes (10): 8.1 Handles, 8.2 The compiler owns layout, 8.3 The static region, 8.4 Views — slices and element references, 8 · Representation, Cost, stated plainly, Element references are views too — the deep consequence, Invalidation, without a borrow checker (+2 more)

### Community 142 - "Arena placement: what `region` serves, and what stops the rest"
Cohesion: 0.12
Nodes (16): A constant shared across the seam has one spelling everywhere, A returned `String` must be freeable on every path, Adding or removing a runtime source, Allocations returned to Prismio go through `rt_base_alloc`, Before you commit, C code style, Comments, Done (+8 more)

### Community 143 - "v0.1 concurrency — the blocking typed `Channel<T>`, and g9's fifth arm"
Cohesion: 0.33
Nodes (6): Particle, life, vx, vy, x, y

### Community 144 - "13. Performance"
Cohesion: 0.20
Nodes (9): Build it, Building Prismio on macOS (and Linux), Check you reached a fixed point, Cross-compiling from Windows, Refreshing the seed, Test, package, verify, Troubleshooting, What you need (+1 more)

### Community 145 - "tokenra"
Cohesion: 0.08
Nodes (39): compile_prismio_file(), elide_middle(), preserved_project_host(), project_host_lock(), v0.1 3.7 -- UMS manifest, dependency resolution, and the lockfile.      `ums/tes, Keep both ends of a diagnostic rather than one of them.      Truncating to the l, Shapes that released memory that was not live, under `--verify`.      Each probe, LAYOUT 3 -- `workload`, and the three normative constraints that are     checkab (+31 more)

### Community 146 - "Boxed `List` replacement ownership"
Cohesion: 0.14
Nodes (13): 0. Cast bugs, 1. Scalar optionals, 2. `as String`, 3. Checked number conversions, 4. Text to value, 5. std fill-out, 6. Enum and `Int`, 7. Docs (+5 more)

### Community 147 - "RESULTS — the string/parse axis"
Cohesion: 0.33
Nodes (8): build(), copy_project(), main(), A one-line edit that is a real edit: it changes the text, the AST and the     em, Copy the program *and the modules beside it*.      A corpus program may import a, Time one scenario for every compiler, interleaved. Returns label -> best.      E, scenario(), touch()

### Community 148 - "g7bench.py"
Cohesion: 0.22
Nodes (8): 1 · The measured design space, 2 · The recorded plan is worth nothing, 3 · Why the header reloads, and what actually fixes it, 4 · Why no LLVM pass will do this for us, 5 · The design that follows, 6 · If the induction-variable analysis is too much, 7 · Sources, What is actually left on a `List<Int>` loop: the check, not the header

### Community 149 - "optlevel.py"
Cohesion: 0.22
Nodes (8): 1 · What the standing entry actually named, 2.1 One invocation producing both was measured and rejected, 2 · Why the first step only got half of it, 3 · What is left, and why it is left, 4 · Result, 5 · Gates, 6 · Fails open, and the test that stops it failing open quietly, Genuinely-cold compilation

### Community 150 - "aif_tier_of"
Cohesion: 0.22
Nodes (8): Counted scalar fills and struct-list initialization, Full Suite Comparison (All 34 Workloads), Interpretation and remaining work, Measurement Results (25-run interleaved comparison), Mechanisms, Reproduction and evidence, Research grounding, Target Workloads

### Community 151 - "Prismio IDE protocol"
Cohesion: 0.22
Nodes (8): 1 · The defect, 2 · What it was not, 3 · What it was, 4 · The fix, and the line it must not cross, 5 · Result, 6 · Cost: none, and it is provable rather than measured, 7 · Coverage, An `extern` declared `alias` no longer outlives the argument it returns

### Community 152 - "Session of 2026-08-13 — `workload` lands; two of LAYOUT 6's dimensions are not blocked on what the brief said"
Cohesion: 0.33
Nodes (6): PrismioTask, prismio_task_await(), prismio_task_invoke(), prismio_task_join(), prismio_task_join_p(), prismio_task_join_v()

### Community 153 - "aif_verify_alloc"
Cohesion: 0.22
Nodes (8): 1 · What the loop was paying, 2 · Three readings that were wrong, and the one that was not, 3 · The change, 4 · What it measured, 5 · What was rejected, 6 · The regression that was kept, 7 · What is left, One `list_set` was declining a loop of eligible reads

### Community 154 - "LAYOUT 6's candidate space, measured against what this compiler can emit"
Cohesion: 0.22
Nodes (8): 0. What this session was asked to do, and why it did something else, 1. The census, before, 2. The recorded blocker was a circularity, not a missing obligation, 3. A latent soundness hole, found by turning the feature on, 4. What it buys, measured, 5. Where it does not fire, and why each is correct, 6. Gate, M3.1 — automatic call-site placement reaches a callee's allocations

### Community 155 - "The cross-language suite — Prismio vs Rust vs Swift"
Cohesion: 0.25
Nodes (7): Five-arm standing, Per-function mnemonic diff, RC against `build/tbaa3`, Sanitizers, Timings, v0.1 release candidate — the complete local gate, What is *not* proved here, What the gate ran

### Community 156 - "arena_census.py"
Cohesion: 0.22
Nodes (8): Changes that shipped, Maintained benchmark results, Map probing and full-width key hashing, Memory cost, Rejected experiments and research, Remaining critical gaps, Supplemental workloads, Validation and reproduction

### Community 157 - "HANDOFF.md"
Cohesion: 0.22
Nodes (8): An existing ownership defect exposed by the tests, Compare equal access counts, Controlled measurements, Existing callers also benefit, Memory and correctness, New API, Reproduce, Single-probe updates and direct entry lookup

### Community 158 - "run_data_view_gate_test"
Cohesion: 0.22
Nodes (9): 1 · The measurement that changed the plan, 2 · What it actually costs on real programs, 3 · Implementation, 4 · A parser defect this found, 5 · The gate, 6 · What this does not do, 7 · Also in this change: the benchmark clock, 8 · Sources (+1 more)

### Community 159 - "build_from_toolchain_sources"
Cohesion: 0.22
Nodes (8): 1 · The gate, 2 · What it costs, measured, 3 · What is *not* established here, 4 · The shape of the change (as planned), 5 · What landed, and what it cost, 6 · The scalar flat-read intrinsic, `List<Int>` and `List<Bool>` never reach the inline path, and the gate is one line, Measured, `build/base-gen1` against `build/rc-gen2`

### Community 160 - "Session of 2026-08-08 (measurement) — the first cross-language numbers, and the optimiser was never on"
Cohesion: 0.22
Nodes (8): 1 · The defect, 2 · Why the ordinary release point is wrong here, 3 · The release point, and its licence, 4 · What it costs the benchmark set: nothing, 5 · Two stale claims found on the way, 6 · Reproducing, 7 · Still open in this area, A `spawn`ed call's owned temporary argument now has an owner

### Community 161 - "0.1.0"
Cohesion: 0.22
Nodes (8): 1 · What was actually true before, 2 · What moved, 3.1 What stayed, and why each one did, 3 · Deleted from `lang_runtime.c`, 4 · Cost, measured, 5 · What the migration found, 6 · Gates, The C string layer is gone

### Community 162 - "v0.1 release candidate — the complete local gate"
Cohesion: 0.22
Nodes (8): A data race in `--verify` itself, Commands, g9's fifth arm, Gate, The four rules, and where each is enforced, The surface, Three model changes the feature needed, each found by a failing check, v0.1 concurrency — the blocking typed `Channel<T>`, and g9's fifth arm

### Community 163 - "ir_snapshot.py"
Cohesion: 0.22
Nodes (9): 5.0.1 Annotations are assertions, not directives *(normative)*, 5.0 Why exactly these four *(normative rationale)*, 5.1 `unique`, 5.2.1.1 Call-site placement, and which regime it uses *(normative)*, 5.2.1.2 Non-lexical extent, and what it does to the obligations *(normative)*, 5.2.1 A region only reaches allocations in its own function *(normative limitation)*, 5.2 `region { … }`, 5.3 `workload(…)` (+1 more)

### Community 164 - "Releasing Prismio"
Cohesion: 0.22
Nodes (9): 10. State and cleanup, 11. CLI architecture, 12. FFI and native boundaries, 14. Testing and validation, 17. The governing principles, 2. Production-code standard, 9. Error handling and process control, Behavior-preserving refactors (+1 more)

### Community 165 - "g2r_time.py"
Cohesion: 0.50
Nodes (4): PrismioChan, chan_bytes_ready(), chan_recv_copy(), chan_send_copy()

### Community 166 - "release_gate.sh"
Cohesion: 0.29
Nodes (6): Inlining the flat push: rejected, and why the obvious gate does not save it, The finding that motivated it, What was kept, What would make it viable, Where it went wrong, and the gate that did not work, Why it was rejected

### Community 167 - "Session of 2026-08-17 (second) — §8's forced candidate lands, and the IR differential turns out to have a concurrency hole"
Cohesion: 0.07
Nodes (51): array_rows(), case_column(), case_folding(), case_tables(), compositions(), confusables(), data_lines(), decompositions() (+43 more)

### Community 168 - "The prompt for the next session"
Cohesion: 0.36
Nodes (5): die(), green(), bootstrap.sh script, resolve_llvm(), step()

### Community 169 - "Session of 2026-08-08 (measurement) — the first cross-language numbers, and the optimiser was never on"
Cohesion: 0.10
Nodes (20): find_binding(), ir_binding_owns_slot(), ir_binding_predates_loop(), ir_get_var_data(), ir_get_var_slot(), ir_get_var_type(), ir_has_var_type(), ir_is_list_exclusive() (+12 more)

### Community 170 - "fn_mnemonic_diff.py"
Cohesion: 0.43
Nodes (7): main(), pct(), PROCESS_MEMORY_COUNTERS, Run the AIF benchmark set and report to BENCHMARKS 3.2's protocol.      python a, One run: wall milliseconds, and peak working set in MB.      The counters stay r, run_once(), suite()

### Community 171 - "ir_intern"
Cohesion: 0.64
Nodes (7): build_scene(), List, cull(), list_init(), list_push(), main(), submit()

### Community 172 - "ir_slot_diff.py"
Cohesion: 0.25
Nodes (8): 1 · Why the item existed, 2.1 The mechanism, and it is not a wash, 2 · Where Prismio stands, 3 · What the program found immediately, 4 · Defect 1 — the task handle had no owner. Fixed., 5 · Defect 2 — a callee-allocated argument still leaks, and it is not about spawn. Open., 6 · Gates, The concurrency axis

### Community 173 - "10 · Boundaries"
Cohesion: 0.25
Nodes (7): A field read is a view of the object it was read from, Scope, The defect, Two missing edges, and a missing type, Verification, What it costs, Why neither existing fact caught it

### Community 174 - "aif_place_arenas"
Cohesion: 0.25
Nodes (7): 1 · The four, by fixture, 2 · The fifth was not fixed; it was never a gate failure, 3 · What the four have that test_62 does not, 4 · Why this cannot be fixed by adding the missing disposition, 4a · What is inferred rather than measured, 5 · Reproducing, `PRISMIO_INLINE_ELEMS=0` fails four fixtures, and the fifth was never one

### Community 175 - "struct_entry"
Cohesion: 0.25
Nodes (8): 1 · Headline, 2 · The static profile is exact, 3 · The model discriminates, and that is the real result, 4 · Spec defect found: LAYOUT §5.4's total could go negative, 5 · What this does not show, 6 · What to do next, AIF — Layout Results (A1), Reproducing

### Community 176 - "block_done"
Cohesion: 0.25
Nodes (7): Hoisting the List header out of the loop: what worked, what did not, and the, noise floor that decided it, Note on measuring g5 at all, The finding, What the measurement said, What this leaves for the real fix, What was tried

### Community 177 - "release.sh"
Cohesion: 0.25
Nodes (7): 1 · What was wrong, 2 · The rule that replaced it, 3 · Measured, 4 · The two failures on the way, both instructive, 5 · Known limits, measured or explicitly not, 6 · Timing, M2.1a — recursive releases for self-referential types (fork (a))

### Community 178 - "One flat-List guard per loop, and the tuned-g4 regression it repairs"
Cohesion: 0.25
Nodes (7): `key_value_update`: one probe in `mapSet`, and a loop guard that is a net loss, Reproduce, Verification, What is left, and where it is, What was built: `mapSet` stops asking a question the probe answered, What was refuted: the flat guard for `loop` and `for`, Where the time is

### Community 179 - "g3.swift"
Cohesion: 0.25
Nodes (8): 1 · The defect, 2 · The fix, and the three conditions on it, 3 · Before / after, 4 · The discriminator, 5 · What this does not reach, An owned call result consumed directly as an argument now has an owner, `spawn` is excluded structurally, and that is required, The retention guard that was asked for does not exist and is not needed

### Community 180 - "cleanup_files"
Cohesion: 0.25
Nodes (8): 1 · The defect, 2 · Which escape routes were already guarded, and which was not, 3 · The fix, 4 · Before / after, 5 · What is still open, 6 · Sources, A binding that escapes through a callee's return was freed under its caller, Two things that were measured, not reasoned

### Community 181 - "run_command"
Cohesion: 0.25
Nodes (7): 1 · The defect, 2 · Why the wide test was there, 3 · The fix, 4 · Result, and the cases that must not move, 5 · Cost: none, provably, 6 · Still open in this area, The argument-position release no longer turns on the return's kind

### Community 182 - "manifest_records"
Cohesion: 0.25
Nodes (7): Found while building this, not caused by it, Measurement 1 — the `+` chain had to be flattened, Measurement 2 — a property may not allocate, The cost: 64 claimed global names, The String surface: operators, properties, iteration, Verification, What landed

### Community 183 - "5 · The accepted tradeoffs, reported anyway"
Cohesion: 0.25
Nodes (7): 1 · The blocker, as recorded and as measured, 2 · The measurement, and the probe that lied, 3 · Why this rules the builtin route out for these four, 4 · Migrating the call sites, 5 · The guard, and why the fixture alone is not one, 6 · What is left, The String operators lower to methods, and the prefixed names are gone

### Community 184 - "A `spawn`ed call's owned temporary argument now has an owner"
Cohesion: 0.29
Nodes (6): A struct crossing a `.plib` read its fields one slot late, Not verified, Results: the subprocess API (2026-09-12 to 2026-09-16), Two defects the fixture found, Validation of the final tree, What the design had to work around

### Community 185 - "run_check_command_test"
Cohesion: 0.57
Nodes (7): Vec, main(), now_ns(), vgrow(), vinit(), vpush(), vpush_out()

### Community 186 - "test_runner.py"
Cohesion: 0.25
Nodes (8): 10 · Worked example, 1 · Architecture, 3.1 Nodes, 3.2 Edges, 3.3 Node ordering (normative), 3 · The fact graph, 9 · Incrementality, AIF — The Inference Engine

### Community 187 - "4. Language and module layout"
Cohesion: 0.25
Nodes (8): 4.1 Escape module, 4.2 Aliasing module, 4.3 Thread module, 4.4 Cyclicity module, 4.5 Closure capture, 4.6 Dynamic dispatch, 4.7 Generics and ownership contexts, 4 · Transfer rules

### Community 188 - "run_suite.py"
Cohesion: 0.25
Nodes (8): 5.1 Iteration strategy (normative), 5.2 The algorithm, 5.3 The give-up condition — and why you cannot simply stop, 5.4 Determinism (normative), 5.5 Termination, 5.6 Minimal cause, 5.7 Optimisation levels, 5 · The fixed-point algorithm

### Community 189 - "call_edge_push"
Cohesion: 0.25
Nodes (8): 7.0.1 Three strategies, 7.0.2 Dedup still applies, 7.0 The ownership-divergence ratio, 7.1 Layer 1 — the relevant-parameter mask *(pre-instantiation, cheapest, does the most work)*, 7.2 Layer 2 — semantic equivalence *(pre-codegen)*, 7.3 Layer 3 — structural dedup *(post-codegen)*, 7.4 Budget-driven collapse, 7 · Specialisation strategy and dedup

### Community 190 - "fn resolve_imports(module, base_dir) -> ASTNode"
Cohesion: 0.33
Nodes (4): Code style, graphify, Runtime surface, Where the project's state lives

### Community 191 - "run_aif_layout_test"
Cohesion: 0.25
Nodes (8): BenchSphere, cb, cg, cr, r, x, y, z

### Community 192 - "run_aif_struct_field_test"
Cohesion: 0.25
Nodes (7): 0 · The commit, 1 · The local gate, 2 · The three-platform matrix — **needs authorisation**, 3 · Artifacts and checksums, 4 · Clean-environment smoke test, 5 · Tag and publish — **needs explicit authorisation**, Releasing Prismio

### Community 193 - "find_binding"
Cohesion: 0.39
Nodes (7): blockers_for(), main(), manifest_symbols(), programs(), `--summary`'s own count of placed calls and served sites.      A second, indepen, (records, brackets), or (None, 0) if the program does not build.      `records`, summary_brackets()

### Community 194 - "run_aif_stack_slot_test"
Cohesion: 0.36
Nodes (6): explain(), main(), parse(), (header key -> value, symbol -> Record). Unparseable lines are ignored:     the, SPEC 6.3's minimal cause for one regressed record, from the compiler.      The d, Record

### Community 195 - "add_binding"
Cohesion: 0.39
Nodes (7): artifact_symbols(), declared_externs(), Failure, main(), Exception, Every `extern fn` name, mapped to the places that declare it., Defined symbols across the given artifacts, with the Mach-O underscore     strip

### Community 196 - "noise floor that decided it"
Cohesion: 0.43
Nodes (6): files_needing_format(), formatted_text(), main(), repository_files(), main(), run_check()

### Community 197 - "The argument-position release no longer turns on the return's kind"
Cohesion: 0.29
Nodes (6): AIF and memory gap tracker, G-001 — `aif_rc` asserts a proxy that no longer tracks its property, G-002 — ownership annotations are not part of trait conformance, G-003 — return-position ownership is not part of trait conformance, G-004 — a node field assigned a local String, and a field overwritten while aliased, How to use it

### Community 198 - "Known issues"
Cohesion: 0.29
Nodes (6): A general affine index matcher, built and reverted, Kept from the attempt, What it measured, What was built, What would actually be needed, Why: a hypothesis, and the two experiments that refuted it

### Community 199 - "Ownership survives a second return"
Cohesion: 0.14
Nodes (17): ArenaChunk, ArenaState, compiler_library_emission_module(), compiler_plib_error(), arena_alloc(), arena_alloc_slot(), arena_chunk_new(), rt_base_alloc() (+9 more)

### Community 200 - "list_new_cap"
Cohesion: 0.29
Nodes (6): Allocation and validation evidence, Null empty variants for boxed recursive enums, Representation and safety boundaries, Reproduction, Result, Why the pass is restricted to recursive enums

### Community 201 - "Inlining the flat push: rejected, and why the obvious gate does not save it"
Cohesion: 0.29
Nodes (6): The measurement, The remaining tuned-g9 gap is not the channel topology, Two hypotheses, both refuted, What the handoff expected, What this leaves, Why the proposed slice cannot close it either

### Community 202 - "fn compile_source(path, output_file, run_after_build) -> Int"
Cohesion: 0.15
Nodes (16): fn append_non_imports(target, source), fn append_statement(module, stmt), fn compile_source(path, output_file, run_after_build) -> Int, extern fn compiler_build_executable, extern fn compiler_run_executable, extern fn compiler_temp_ir_path, extern fn delete_file, extern fn get_directory (+8 more)

### Community 203 - "Appendix — M2's closing state, 2026-08-23"
Cohesion: 0.36
Nodes (8): JitProcessSymbols, LLVMErrorRef, LLVMOrcLLJITRef, compiler_pending_arguments(), ir_jit_run_file(), jit_failed(), jit_failed_unresolved(), jit_process_symbols()

### Community 204 - "13. Performance"
Cohesion: 0.10
Nodes (30): ir_get_struct_field_count(), ir_get_struct_field_type_at(), ir_is_struct_type_name(), attach_cold(), attach_cold_rc(), get_or_declare_alloc_fn(), ir_alloc_cycle(), ir_alloc_object() (+22 more)

### Community 205 - "Getting Started"
Cohesion: 0.17
Nodes (24): build_curated_module(), build_trace_enabled(), build_trace_ms(), build_trace_stage(), compile_ir_to_object(), compile_native_sources(), compiler_jit_run(), discard_curated_raw_ir() (+16 more)

### Community 206 - "file_exists"
Cohesion: 0.20
Nodes (18): compare_dotted_versions(), compiler_run_executable_with(), compiler_run_workload(), emit_plib_section(), emit_runtime_bitcode(), link_program_msvc(), msvc_target_arch(), msvc_tools_dir() (+10 more)

### Community 207 - "prismio_llvm.h"
Cohesion: 0.15
Nodes (13): compiler_default_exe_path(), compiler_is_current_executable(), compiler_remove_tree(), find_llvm_paths(), find_llvm_paths_ex(), json_string_field(), llvm_link_name(), path_file_name() (+5 more)

### Community 208 - "Gap 1: sound owner facts at calls, `spawn`, and FFI"
Cohesion: 0.29
Nodes (6): 1 · Why this existed, 2 · What was built, 3 · What it is worth, 4 · The criterion is now an effect analysis, not a syntactic one, 5 · What is still declined, min/max/abs, and the call that used to cost 1.79x

### Community 209 - "HANDOFF.md"
Cohesion: 0.29
Nodes (6): 1 · The distinction that was missing, 2 · The g6 test, which is the whole point, 3 · The benchmark sweep, 4 · Why the two targets did not move, which is the finding worth keeping, 5 · What the guard promises, and what it does not, E1: the push check belongs in the preheader, and the profile it was said to need does not exist

### Community 210 - "The generated release loops on its tail self field"
Cohesion: 0.29
Nodes (6): Discriminator, Gates, Lowering, Remaining boundary, Result, The generated release loops on its tail self field

### Community 211 - "M2.1a — recursive releases for self-referential types (fork (a))"
Cohesion: 0.29
Nodes (6): AIF Prototype, Approximations, Running, Two bugs found here, both worth remembering, Two roles, What it implements

### Community 212 - "Worker-ready implementation tasks"
Cohesion: 0.29
Nodes (7): 11.1 Field sensitivity is object-insensitive, 11.2 The context set is discovered from facts that are still moving, 11.3 Loops are handled by the lattice, not by a loop analysis, 11.4 There is no interprocedural path sensitivity, 11.5 ~~The `⊤` context is a cliff~~ — resolved in 1.2, 11.6 Everything here assumes whole-program PIR, 11 · Known weaknesses

### Community 213 - "Gap 4: channel runtime ignores endpoint topology"
Cohesion: 0.29
Nodes (7): 2.1 `E` — escape, 2.2 `A` — aliasing, 2.3 `T` — thread affinity, 2.4 `C` — cyclicity, 2.5 `L` — lifetime determinacy *(derived)*, 2.6 The product, 2 · Fact domains

### Community 214 - "Concepts"
Cohesion: 0.10
Nodes (18): 1 · `tools/release_gate.py`, 2 · Benchmark matrix, The v0.1 gate and benchmark matrix on the branch head, 2026-09-25, Checking one file of a program, Current boundary, JSON diagnostics, Prismio IDE protocol, POST_INSTALL.txt (install success message) (+10 more)

### Community 216 - "LLVM IR and final assembly audit"
Cohesion: 0.43
Nodes (6): main(), manifest(), Everything the compiler may have left behind that a later run could read., The tier records only: the header carries a budget and a round count, and     `-, records(), wipe_state()

### Community 217 - "Gap 6: functional-update reuse is not represented"
Cohesion: 0.62
Nodes (6): check(), count_occurrences(), defined_symbols(), find_library(), main(), Path

### Community 218 - "Gap 7: temporary allocation extents are still coarse"
Cohesion: 0.33
Nodes (8): banner(), error(), fatal(), fetch(), info(), install.sh script, success(), update_profile()

### Community 219 - "std.math: Float's functions, and the three Float codegen bugs under them"
Cohesion: 0.33
Nodes (5): 1 · The lowering, 2 · Three bugs the library could not be written over, 3 · Cost, 4 · Not done, std.math: Float's functions, and the three Float codegen bugs under them

### Community 220 - "struct_entry"
Cohesion: 0.33
Nodes (5): -O3 for program builds, and the measurement that had gone stale, Result, The claim that was there, The fairness half, What it measures now

### Community 221 - "The two standing rules"
Cohesion: 0.33
Nodes (5): 1 · What the spec said, and what was actually there, 2 · The fix, 3 · Measured, 4 · A measurement that had to be thrown away first, MEM-035: the stencil's offsets were never the problem — its condition was

### Community 222 - "rt_prof_slot"
Cohesion: 0.33
Nodes (5): 1 · What was built, 2 · Measured, 3 · Why `large_buffer_copy` did not move much, and where its time actually is, 4 · One number in the sweep that is not real, and the check that says so, MEM-006: the whole-buffer copy is one `llvm.memmove`, and the benchmark it was aimed at is not a copy benchmark

### Community 223 - "Source-level and type representation inventory"
Cohesion: 0.33
Nodes (6): 8.1 Seeding and cutting, 8.2 `unique` — verification is complete, 8.3 `region` — verification is sound, and imprecision costs only performance, 8.4 `pin`, 8.5 Verification under budget, 8 · Annotations as axioms and constraints

### Community 224 - "Current baseline"
Cohesion: 0.33
Nodes (6): 11.0 Conformance levels, 11 · Conformance boundary, Annotation governance, Frozen — normative, Open — by descending risk, Resolved in 1.1 — was open in v1.0

### Community 225 - "aif_ledger_init"
Cohesion: 0.33
Nodes (6): 3 · The tier ladder, T0 — Value / stack, T1 — Region / arena, T2 — Unique owned, T3 — Shared, non-atomic reference counting, T4 — Managed residue

### Community 226 - "Ownership, lifetime, and AIF"
Cohesion: 0.33
Nodes (6): 5.4.1 A proven-false pin is a compile error, 5.4.2 An unproven pin is never an error, 5.4.3 Strictness is opt-in, per value, 5.4.4 The direction limit *(normative)*, 5.4.5 `pin(<region-name>)` — the placement form *(normative)*, 5.4 `pin`

### Community 227 - "Target architecture"
Cohesion: 0.33
Nodes (6): 7.1 Requirement, 7.2 Levels, 7.3 `verify` — facts as runtime assertions, 7.4 Layout search is opt-in, 7.5 Levels are per module, not per build, 7 · Two-speed compilation

### Community 228 - "Particle"
Cohesion: 0.29
Nodes (6): Answer: Prismio chooses after substitution, Discriminating gate, Exit, M4.4 — generic/container layout specialization, Performance control, Question

### Community 229 - "Ownership survives a second return"
Cohesion: 0.33
Nodes (6): 1 · What the matrix saw, and what this host did not, 2 · The defect, 3 · The fix, 4 · Before / after, 5 · What to check next, A payload-free enum variant allocated uninitialised memory

### Community 230 - "`list_new` allocates nothing until the first push"
Cohesion: 0.33
Nodes (6): 16. A practical review checklist, Architecture, Code, Comments, Correctness, Performance

### Community 231 - "Performance: what is open, and how to measure it"
Cohesion: 0.20
Nodes (8): 1 · For 0.1, 2 · Current position, 3.1 · Compiler levers, 3.2 · Platform, not performance, 3 · Later, 4 · Closed, with evidence, 5 · How this work is done, Performance: what is open, and how to measure it

### Community 232 - "aif_records"
Cohesion: 0.33
Nodes (6): 5. Ownership, handles, and globals, Globals holding handles need no initializer, Handles are `Ptr`, Strings and structs are affine, Test pointer absence with pointer helpers, The old string-punning invariant is retired

### Community 233 - "2 · Later"
Cohesion: 0.20
Nodes (9): 1 · For 0.1: no known way to corrupt memory in a program that compiles, 2.1 · Observability first, 2.2 · Correctness of the runtime model, 2.3 · Middle IR and interprocedural facts, 2.4 · Representation, 2.5 · Only if telemetry asks for them, 2 · Later, 3 · What the deep dive established that still holds (+1 more)

### Community 234 - "M4.1 — first-class `Slice<T>`"
Cohesion: 0.29
Nodes (6): 1 · The reader, 2 · The leak, 3 · Throughput, 4 · Reproducing, 5 · Why `std.input` and not `std.io`, and the workload link, Standard input, and the arena that could not serve a C allocation

### Community 235 - "Prompt 2 (residual) — the hot/cold split, and only that"
Cohesion: 0.33
Nodes (5): 1 · The shapes, 2 · Why, 3 · What moved, 4 · Pinned, Three ownership shapes that freed memory that was not live

### Community 236 - "arena_emit_range"
Cohesion: 0.40
Nodes (4): elem_spelling_resolved(), Bind a tainted base's element keys together, both ways.          A base with eve, Whether this spelling names one container rather than every instance of a     ba, vs_ref()

### Community 237 - "list_set"
Cohesion: 0.31
Nodes (10): list_set(), list_slice_set(), rc_alloc(), rc_attach_cold(), rc_cold_slot(), rc_release(), rc_release_atomic(), rc_retain() (+2 more)

### Community 238 - "bracket_place"
Cohesion: 0.40
Nodes (4): Fidelity, The G2 / G6 benchmark set, What it found, What the variants are

### Community 239 - "M4.4 — generic/container layout specialization"
Cohesion: 0.80
Nodes (4): digest(), main(), measure(), run()

### Community 240 - "Boxed `List` replacement ownership"
Cohesion: 0.70
Nodes (4): digest(), main(), replace_once(), run()

### Community 241 - "AIF Evidence"
Cohesion: 0.24
Nodes (12): ir_store_ptr(), ir_struct_store_ptr(), scalar_tbaa_tag(), struct_field_tbaa_tag(), struct_record_tbaa_tag(), tag_scalar(), tag_struct_field(), tbaa_leaf() (+4 more)

### Community 242 - "13. Performance"
Cohesion: 0.40
Nodes (4): 1 · What was built, 2 · What it is worth, which is almost nothing here, 3 · Step 2 of the task was not attempted, and why, MEM-033: the cycle collector stops locking when there is nothing to lock against

### Community 243 - "Gap 10: runtime curation has an incomplete dependency closure"
Cohesion: 0.40
Nodes (4): 1 · The benchmark is a serial modulo chain, not a container benchmark, 2 · The reload that looks redundant is load-bearing, 3 · What would actually collect the 9%, `vector_growth`: 93% of it is one modulo chain, and the redundant load is not redundant

### Community 244 - "The String surface: operators, properties, iteration"
Cohesion: 0.40
Nodes (5): 6.1 What a context is, 6.2 Context ordering, 6.3 Discovery (demand-driven), 6.4 The context cap, 6 · Ownership contexts

### Community 245 - "3 · Ownership, and the three ways to get it wrong"
Cohesion: 0.40
Nodes (5): 2.1 Allocation site, 2.2 Ownership context, 2.3 Abstract value, 2.4 What tier is not, 2 · The objects of the model

### Community 246 - "An owned call result consumed directly as an argument now has an owner"
Cohesion: 0.40
Nodes (5): 4.1 Inputs, 4.2 The derivation function, 4.3 Monotonicity (normative property), 4.4 Cost model constants *(informative)*, 4 · Tier derivation

### Community 247 - "A binding that escapes through a callee's return was freed under its caller"
Cohesion: 0.40
Nodes (5): BenchTree, left, right, value, unique_ptr

### Community 248 - "A payload-free enum variant allocated uninitialised memory"
Cohesion: 0.60
Nodes (5): BOOL, PINIT_ONCE, PVOID, aif_ledger_init(), cyc_lock_init()

### Community 249 - "`list_new` allocates nothing until the first push"
Cohesion: 0.33
Nodes (5): Host noise, for whoever measures next, `list_new` allocates nothing until the first push, The defect, The measurement, and why it says nothing, Why keep it

### Community 250 - "E1: the push check belongs in the preheader, and the profile it was said to need does not exist"
Cohesion: 0.40
Nodes (5): 3. Before changing code, Judge changes by emitted behavior, Self-hosting comes first, Two generations before trusting a compiler change, Understand the existing boundary first

### Community 251 - "run_ums_test"
Cohesion: 0.33
Nodes (5): Boundary, Code shape, Gates, Measurement, Scalar list writes cross the curated boundary

### Community 253 - "min/max/abs, and the call that used to cost 1.79x"
Cohesion: 0.40
Nodes (6): plib_sections(), A PLIB v3's code sections as (triple, normal bitcode), or None.      The layout, A cross build takes `std` bitcode compiled for its own target.      A PLIB used, Installed std/runtime artifacts are sharded, mandatory, and executable., run_module_artifact_test(), run_plib_triple_sections()

### Community 254 - "Target architecture"
Cohesion: 0.40
Nodes (6): spawn_and_wait(), proc_spawn_arg(), proc_spawn_begin(), proc_wait(), spawn_builder_reset(), spawn_dup()

### Community 256 - "nominal_find"
Cohesion: 0.60
Nodes (4): main(), Path, Whether this process could create the install. Walks up to the nearest     exist, writable()

### Community 257 - "Ownership survives a second return"
Cohesion: 0.50
Nodes (4): AIF Corpus, Building, Gaps to fill, Three things the corpus established

### Community 258 - "3. Before changing code"
Cohesion: 0.83
Nodes (3): digest(), main(), run()

### Community 259 - "3. Before changing code"
Cohesion: 0.83
Nodes (3): large_buffer_copy(), main(), now_ns()

### Community 260 - "aif_fn_lookup"
Cohesion: 0.83
Nodes (3): digest(), main(), run()

### Community 261 - "prismio_task_spawn"
Cohesion: 0.67
Nodes (3): prismio_memory_threads_enable(), prismio_task_spawn(), prismio_task_start_failed()

### Community 262 - "M4.3b — DataView element reads"
Cohesion: 0.29
Nodes (6): Correctness and closure gates, M4.3b — DataView element reads, Next gate, Read-only layout gate, Standard-corpus regression gate, What changed

### Community 263 - "M4.3b — DataView element reads"
Cohesion: 0.11
Nodes (17): 10 · Trojan Source and UTS #39, tested, 11 · A `break` in a nested loop is that loop's, 12 · Verification, round 2, 1 · The tables came from the interpreter, and the interpreter was wrong, 2 · Conformance, against the UCD's own tests, 3 · Representation: readable, after one codegen fix, 4 · std.unicode, before and after, 5 · Identifiers: UAX #31 (+9 more)

### Community 264 - "run_negative_test"
Cohesion: 0.33
Nodes (6): 1. Architecture, Do not place code in the nearest convenient file, Do not split into meaningless fragments, File size is a signal, not a law, Keep subsystem boundaries explicit, Modules own responsibilities

### Community 266 - "compiler_probe_executable"
Cohesion: 0.33
Nodes (5): Boundary microbenchmark, Correctness and reproducibility, M4.3a — explicit DataView conversion boundary, Standard milestone benchmark, What landed

### Community 267 - "The hot element accessor was never curated"
Cohesion: 0.29
Nodes (5): CLI behavior, Manifest edits, Manifest syntax, Project commands, Unified Manifest System (UMS)

### Community 268 - "AIF — Engine/Game Boundary Results (A2)"
Cohesion: 0.33
Nodes (5): Discriminating gates, M4.1 — first-class `Slice<T>`, Ownership result, Surface and representation, Verification and measurement

### Community 269 - "M4.3c — mutable DataView round trip"
Cohesion: 0.33
Nodes (6): 8. Comments, Bad comments explain, Comment density should be earned, Do not turn source files into the specification, Good comments explain, Preserve subtle bug explanations

### Community 270 - "Boxed `List` replacement ownership"
Cohesion: 0.40
Nodes (4): Boxed `List` replacement ownership, Discriminator, Gates, Why an exclusive operation

### Community 271 - "M5.1 — allocator evaluation"
Cohesion: 0.22
Nodes (9): Direct mimalloc result, Direct rpmalloc result, Final gate and decision, Initial dynamic-interposition result, M5.1 — allocator evaluation, Method, Question and acceptance rule, Research choice (+1 more)

### Community 272 - "`Int` width — the decision, and the three measurements that made it"
Cohesion: 0.17
Nodes (12): 1 · What the literature actually claims, 2 · Index width is free. Measured, on both targets., 3 · Making overflow UB buys nothing. Measured, on real Prismio programs., 4 · Data width costs 1.33×. Measured, in Prismio., 5 · The cost, stated plainly, 6 · Verdict, 7 · Re-examined 2026-09-24: the whole benchmark suite, 8 · Adaptive width: `Int` means 64 bits, AIF stores it narrow (2026-09-24) (+4 more)

### Community 273 - "MEM-006: the whole-buffer copy is one `llvm.memmove`, and the benchmark it was aimed at is not a copy benchmark"
Cohesion: 0.83
Nodes (3): main(), normalise(), slot_names()

### Community 274 - "measure.py"
Cohesion: 0.83
Nodes (3): main(), Path, run_fixture()

### Community 276 - "Single-probe updates and direct entry lookup"
Cohesion: 0.67
Nodes (3): 10.1 FFI, 10.2 Library distribution, 10 · Boundaries

### Community 278 - "LayoutParticle"
Cohesion: 0.33
Nodes (6): LayoutParticle, mass, velocity, x, y, z

### Community 279 - "7. Functions and control flow"
Cohesion: 0.40
Nodes (5): 7. Functions and control flow, Do not repeat ownership-sensitive work, One responsibility per function, Prefer early returns, Use `loop` for unconditional loops

### Community 280 - "Ownership survives a second return"
Cohesion: 0.40
Nodes (5): 1 · The defect, 2 · Why it did not need a fixed point, 3 · Before / after, 4 · What is still declined, Ownership survives a second return

### Community 281 - "15. Working with agents"
Cohesion: 0.40
Nodes (5): 15. Working with agents, Do not leave partial modularization, Do not solve architecture problems with comments, Do not solve architecture problems with one-off wrappers, Prefer one coherent refactor over many cosmetic edits

### Community 282 - "Prismio IDE protocol"
Cohesion: 0.67
Nodes (3): expected_errors(), Substrings the diagnostics must contain, from `// expect-error:` lines.      Wit, run_negative_test()

### Community 283 - "4. Language and module layout"
Cohesion: 0.50
Nodes (4): 4. Language and module layout, `extern fn` means foreign code, Imports, Internal functions do not need extern declarations

### Community 284 - "Results: the string-benchmark gap (2026-09-11)"
Cohesion: 0.25
Nodes (7): Bugs found on the way, Changes, Method, Results: the string-benchmark gap (2026-09-11), Root causes, Still open, The suite, before and after

### Community 285 - "measure.py"
Cohesion: 0.60
Nodes (4): main(), programs(), A copy of `compiler` whose basename is not `prismio`, beside the original., under_neutral_name()

### Community 286 - "phase.cpp"
Cohesion: 0.67
Nodes (3): die(), PRISMIO_SEED_IR, refresh_seed.sh script

### Community 293 - "fn_mnemonic_diff.py"
Cohesion: 0.18
Nodes (8): 1 · Decisions, 2 · Order of work and status, `Array<T, N>` is an array whose length is part of its type, Collections, `Slice<T>` has two layouts, chosen at compile time, `Vec<T>` is used through methods, `Vec<T, N>` and `Vec<T, Chunk>` are chunked, `Vec<T>` replaces `List<T>`

### Community 294 - "13. Performance"
Cohesion: 0.67
Nodes (3): 13. Performance, Elsewhere, Scanner

### Community 299 - "6. Naming"
Cohesion: 0.67
Nodes (3): 6. Naming, Name by responsibility, Parser and lexer naming

### Community 300 - "common.rs"
Cohesion: 0.50
Nodes (3): BenchTree, Box, Option

### Community 301 - "list_push_inline_scalar_slow"
Cohesion: 0.12
Nodes (29): PRISMIO_NOINLINE, arena_alloc_at(), int_to_str(), list_inline_grow(), list_push(), list_push_grow(), list_push_inline_scalar(), list_push_inline_scalar_slow() (+21 more)

### Community 302 - "loop_named"
Cohesion: 0.29
Nodes (8): RangeProofNode, ir_range_proof_data(), ir_range_proof_mark(), ir_range_proof_marked(), ir_range_proof_of(), range_proof_bucket(), range_proof_entry(), range_proofs_disabled()

### Community 304 - "cost.c"
Cohesion: 0.31
Nodes (12): bench_next_random(), Key, main(), measure(), mix_d(), mix_e(), mix_h(), mix_i() (+4 more)

### Community 305 - "prismio_task_entry"
Cohesion: 0.29
Nodes (7): HANDLE, prismio_memory_thread_enter(), DWORD, LPVOID, prismio_task_entry(), spawn_descriptor(), spawn_stream_win()

### Community 306 - "Who owns a call's result: asked of the call, not of its allocation site"
Cohesion: 0.25
Nodes (7): 1 · One allocation site, every call's answer, 2 · Pass-throughs, also asked of sites, 3 · A temporary the callee hands a view of back, 4 · Guards the new bindings needed, which user bindings needed already, 5 · What moved, 6 · Still open, Who owns a call's result: asked of the call, not of its allocation site

### Community 307 - "Results: `__builtin_string_hash` (2026-09-12)"
Cohesion: 0.25
Nodes (7): Checks, Choosing the mix, Left open, Results: `__builtin_string_hash` (2026-09-12), The fixture, and that it is not vacuous, What it buys, What the change is

### Community 308 - "Properties are declared: `prop`"
Cohesion: 0.29
Nodes (6): Landing, Properties are declared: `prop`, Still open, The rule before, The rule now, Which std functions are properties

### Community 311 - ".new_site"
Cohesion: 0.18
Nodes (6): ann_leaf_name(), Model, The type an annotation refers to: `[T]` and `List<T>` hang T off c1,     and the, Does a value of this type participate in the memory model at all?, Tarjan-free SCC via iterative Kosaraju on the type reference graph         (INFE, Site

### Community 313 - "The relational tier, byte-sized Bool elements, and three gaps read from disassembly"
Cohesion: 0.33
Nodes (5): Findings worth keeping, Numbers (scale 4), Tests, The relational tier, byte-sized Bool elements, and three gaps read from disassembly, What changed

### Community 316 - "Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs"
Cohesion: 0.40
Nodes (4): Findings worth keeping, Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs, Numbers (scale 4), What changed

## Ambiguous Edges - Review These
- `Test naming convention (test_<NN>_<description>.psm)` → `fn main() -> Int`  [AMBIGUOUS]
  CONTRIBUTING.md · relation: conceptually_related_to

## Knowledge Gaps
- **1255 isolated node(s):** `ablations.sh script`, `a`, `b`, `c`, `d` (+1250 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Test naming convention (test_<NN>_<description>.psm)` and `fn main() -> Int`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `ir_debug_begin()` connect `g6_bench.c` to `setup_llvm.py`, `Ownership survives a second return`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `current_directory()` connect `Ownership survives a second return` to `g6_bench.c`, `check_source_lists.py`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `rt_base_alloc()` connect `Ownership survives a second return` to `AIF — Adaptive Inference Framework`, `free`, `g2_tuned.rs`, `list_set`, `list_push_inline_scalar_slow`, `file_exists`, `prismio_llvm.h`, `Getting Started`, `strlen`, `check_source_lists.py`, `1 · AIF core — genuinely ours`, `6 · Ownership contexts`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `main()` (e.g. with `run_aif_annotation_test()` and `run_aif_concurrency_test()`) actually correct?**
  _`main()` has 70 INFERRED edges - model-reasoned connections that need verification._
- **Are the 63 inferred relationships involving `run()` (e.g. with `allocation_escape()` and `aos_vs_soa()`) actually correct?**
  _`run()` has 63 INFERRED edges - model-reasoned connections that need verification._
- **What connects `ablations.sh script`, `a`, `b` to the rest of the system?**
  _1255 weakly-connected nodes found - possible documentation gaps or missing edges._
# Type conversions: what 0.1 ships

The last language work before v0.1.0. Like the other `docs/*_PLAN.md` files, this
is the tracker: what is left, how each piece is meant to land, and its status.
Defects found on the way go to `KNOWN_ISSUES.md`; measurements to `aif/evidence/`.

**Status key:** `todo` · `in progress` · `done <date>` · `blocked: <why>`.

## The design

`as` is the one conversion operator, and its result type says whether it can fail.

| Expression | Meaning |
|---|---|
| `x as T` | A conversion that cannot fail: widening, truncating, saturating, or to `String`. |
| `x as T?` | A conversion that can fail: `none` when the value has no `T`. Never a run-time error. |
| `"12" as Int` | A `String` the compiler can read is converted at compile time, and one it rejects (`"12Sf"`) is a compile error. |
| `s as Int`, `s` unknown | A compile error that names `s as Int?`. |

A scalar's `T?` is `T` plus `none`: a present flag beside the value, copied like
`T`, never allocated. A plain `T` is accepted where a `T?` is expected. A
reference's `T?` is unchanged: a nullable pointer, where `none` is null.

## Tasks

| # | Task | Status |
|---|---|---|
| 0 | [Cast bugs](#0-cast-bugs) | done 2026-09-30 (suite pending) |
| 1 | [Scalar optionals: `T?` by value](#1-scalar-optionals) | in progress (std impls after the seed refresh) |
| 2 | [`as String`](#2-as-string) | todo |
| 3 | [Checked number conversions: `x as T?`](#3-checked-number-conversions) | todo |
| 4 | [Text to value: `s as T` and `s as T?`](#4-text-to-value) | todo |
| 5 | [std fill-out: every width has `toString`, `toFloat`, `parse`](#5-std-fill-out) | todo |
| 6 | [Enum and `Int` interchange](#6-enum-and-int) | todo (known issue) |
| 7 | [Docs, both apps](#7-docs) | todo |
| 8 | [IntelliJ plugin](#8-intellij-plugin) | todo |
| 9 | [Build and verify everything](#9-build-and-verify) | todo |

### 0. Cast bugs

- `true as Float` was -1.0 and `(200 as Char) as Float` was -56.0: `sitofp` read
  `Bool` and `Char` as signed. They convert unsigned now, as they widen.
- `as` bound tighter than a prefix operator: `-1 as U8` was a negation of an
  unsigned value (an error), and `-1e30 as I64` was one short of `I64.MIN`.
  `-x as T` is `(-x) as T` now, as in Rust. No site in `src/` or `std/` changed
  meaning: the compiler's IR is byte-identical before and after.
- `U8.MAX` without `import std.math` said "unknown identifier `U8`". It names the
  import now.

**Fixed on the way (not conversions).** `toolchain.host` in `build.ums` refused
anything outside `.prismio/` (`UMS2405`), which broke `sandbox/`'s
`../.prismio/build/debug/prismio`. Any path is accepted now, absolute included; the
`.trusted` stamp is what decides whether a host runs. `clean` deletes the host only
when it is the project's own build output. The IntelliJ plugin dropped the check,
and it now finds the compiler through `toolchain.host` rather than guessing
`.prismio/build/debug`. Suite 478/478; plugin tests green.

### 1. Scalar optionals

**Changed from the first plan: a scalar `T?` is not `Option<T>`.** `Option<Int>`
is a boxed payload enum -- a `malloc` per value, and move-only, so `let b = a`
moved `a`. A scalar's `T?` is instead `{ i1 present, T value }` by value (IR key
`opt:<key>`): copied like `T`, no allocation. `String?`, `Vec<T>?` and a struct's
`T?` stay nullable pointers, as before.

**Done, through the suite (481/481, build `build/cv-p8`):**
`T?` on `Int`/every width/`Float`/`Bool`/`Char`/fieldless enums; `none` and
`default`; a `T` wrapped implicitly in `let`, assignment, `return`, arguments and
struct fields (semaCheckScalarOptional/semaWrapPresent in `sema/ownership.psm`);
`== none`, `!= none`, `T? == T?` by value; `expect(o)` (panics with file:line);
`o.unwrapOr(x)` as a branchless `select` (new `ir_select` in the backend); generic
`fn f<T>(v: T?)` infers `T`; `-g` debug info; `half()` compiles to no `malloc`.

**Containers, done 2026-09-30.** A scalar `T?` in a `Vec`, a slice, an array
literal or a `Map` value:

- up to 32 bits of payload, an element is **one integer** twice the payload's
  width -- the value in the high half, the flag in the low one, so a zeroed row
  is `none` (`optCarrierKey` in `src/ir/types.psm`, `ir_opt_pack`/`ir_opt_unpack`
  in the backend). Every existing scalar path takes it unchanged: the runtime's
  i64 carrier, stored by width, and the guarded flat push/read/write in loops.
  `Vec<Int?>` is 8 bytes an element, as Rust's `Option<i32>`; a 20M-element read
  loop measured 1.15x of `Vec<Int>`.
- a 64-bit payload (`Float?`, `I64?`) has no integer wide enough on that carrier,
  so it is a 16-byte `{ i1, T }` row reached by address, as a flat struct is.
- `Vec<T?>.filled` takes the runtime's fill for a narrow `T?`; a wide one needs
  std.vec's copy loop and so the `Copy` impl below.
- `Channel<Int?>` is refused as `Channel<Int>` is: a channel carries references.
- A `Map`'s value may not be an owned type (the v0.1 rule), so `Map<K, String?>`
  stays refused, loudly, as `Map<K, String>` is.

**Fixed on the way.** Every `T?` mangled to `Invalid` (`semaMangleType`), so two
instantiations over different optionals were one: `Map<Int, Float?>` beside
`Map<Int, U8?>` gave the second the first's `set`. A generic parameter solved to
`T?` refused a plain `T` argument that a concrete `T?` parameter took. And
`return expect(x)` on an `Int?` became `expect<Int>` -- `Option<T>`'s
two-parameter method, solved from the expected return type -- once `std.option`
was loaded, which any `import std.map` does.

Also found by the suite: `Channel<Int>` compiled again. The channel rule was
"the element can be optional", which every scalar now is; it asks for a
reference now (`src/sema/types.psm`, neg_197).

Verified 2026-09-30: suite 481/481 (test_238, neg_239, the `scalar_optional`
harness check for no allocation in `half` and `expect(none)`'s panic, test_238
under `--verify` at 0 leaked); two generations to a byte-identical fixpoint; the
compiler's IR for `src/` identical to the session-start compiler's;
`aif_differential` agrees on every corpus program and AIF test (`src/main.psm`
was mid-edit and did not parse, so it was not compared).

**Left in task 1:**
- the seed refresh, then `impl Copy`/`Eq`/`Display` for scalar `T?` in std
  (`sort`, `contains`, `pop`, a wide `filled`) and `println` of a `T?`.

Original list, for reference:

- the annotation: `T?` on a non-reference resolves to `Option<T>` instead of the
  "only a reference can be optional" error;
- `none` where an `Option<T>` is expected is `Option<T>.None`;
- a `T` where an `Option<T>` is expected is `Option<T>.Some(value)`: a `let`, an
  assignment, a `return`, an argument, a struct field;
- `o == none` and `o != none` on an `Option<T>`;
- `Option` reachable without `import std.option`, since `Int?` is language syntax;
- tests: each position above, ownership of an `Option<String>`, and `--verify`.

`src/` and `std/` must not use the syntax until the seed is refreshed.

### 2. `as String`

Every number type, `Bool`, `Char` and `String` convert with `as String`, as
`x.toString()` does -- the same text, and an allocation the caller owns.

### 3. Checked number conversions

`x as T?` between any two number types. `none` when the value does not fit:
`300 as U8?`, `-1 as U64?`. From a `Float`, `none` also for NaN, an infinity, and
a value with a fraction: `3.5 as Int?` is `none`, `3.0 as Int?` is 3.

### 4. Text to value

`s as T?` for every integer width, `Float` and `Bool`, with `parseInt`'s rules.
`s as T` when `s` is a literal (or an immutable `let` bound to one): converted at
compile time, an error when the text does not parse. Otherwise an error naming
`as T?`.

### 5. std fill-out

`toString`, `toString(radix)`, `toFloat` and `parse*` on `I8`, `I16`, `U8`,
`U16`, `U32`, `Usize` and `Isize`, which today have none. These are also what
tasks 2-4 lower to.

### 6. Enum and `Int`

A fieldless enum and `Int` are interchangeable in sema: `let c: Color = 7`,
passing `2` for a `Color` parameter, and `7 as Color` all compile, and a `match`
on the result has no arm for it. Refusing only the cast closes nothing and broke
`Color.Blue as Color`, since a variant types as `Int`. A distinct enum type is a
change to how every `.kind == NodeKind.X` in `src/` is checked. Recorded in
`KNOWN_ISSUES.md`; the decision is open.

### 7. Docs

A `language/conversions.md` page; `optionals.md` (scalar optionals exist, and its
"no generic `Option<T>`" line is stale), `types.md`, `operators.md` (the
precedence), the type-system and behaviour spec pages, `strings.md`, `math.md`,
the errors pages, the roadmap, the 0.1.0 release notes and `CHANGELOG.md`; the
developers app on how casts lower. Both apps' `verify-doc-examples.mjs` pass.

### 8. IntelliJ plugin

Its hand-written lexer and completion must know `as T?` and `x as String`; the
corpus test catches drift.

### 9. Build and verify

Two generations to a fixpoint, the full suite, `aif_differential.py`, the corpus,
`release_gate.py`, a packaged toolchain, the project host promoted, the seed
refreshed once the syntax is in.

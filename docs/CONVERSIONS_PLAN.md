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
| 0 | [Cast bugs](#0-cast-bugs) | done 2026-09-30 |
| 1 | [Scalar optionals: `T?` by value](#1-scalar-optionals) | done 2026-09-30 |
| 2 | [`as String`](#2-as-string) | done 2026-09-30 |
| 3 | [Checked number conversions: `x as T?`](#3-checked-number-conversions) | done 2026-09-30 |
| 4 | [Text to value: `s as T` and `s as T?`](#4-text-to-value) | done 2026-09-30 |
| 5 | [std fill-out: every width has `toString`, `toFloat`, `parse`](#5-std-fill-out) | done 2026-09-30 |
| 6 | [Enum and `Int` interchange](#6-enum-and-int) | done 2026-09-30 |
| 7 | [Docs, both apps](#7-docs) | done 2026-09-30 (website a8b9b64) |
| 8 | [IntelliJ plugin](#8-intellij-plugin) | done 2026-09-30 (plugin f28e7d0) |
| 9 | [Build and verify everything](#9-build-and-verify) | done 2026-10-01 ([gate record](../aif/evidence/RESULTS-conversions-release-gate.md)) |

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

**std, done 2026-09-30.** `Copy`, `Eq`, `Ord` and `Display` for each scalar
`T?`, and `print`/`println`/`eprint`/`eprintln` of one: its value, or `none`.
`Ord` puts `none` before every value. So `Vec<Int?>` has `contains`, `indexOf`,
`clone`, `pop`, `sort`, `binarySearch`, and `Vec<Float?>.filled`. One `impl` per
type, which needed `impl Trait for Int?` in the parser and so a seed refresh
first (c80ef0b). Two resolution bugs on the way, both fixed there: a generic
template beat an exact concrete overload (`f(5)` beside `f(Int)` and `f<T>(T)`),
and `show(n)` beside `show(Int)` and `show(Int?)` was ambiguous -- an argument
taken as it is now outranks one wrapped into a `T?`. test_240, test_242,
neg_241; suite 484/484 from the committed seed.

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

**Done 2026-09-30.** Sema rewrites the cast into `toString(x)` bound to
std.string, as `a + b` becomes `concat`, so the two cannot disagree; without
`import std.string` it is an error saying so (neg_244). `String` gained a
`toString` (an owned copy). An enum is refused, except that a variant still
types as `Int` (task 6). test_243.

### 3. Checked number conversions

`x as T?` between any two number types. `none` when the value does not fit:
`300 as U8?`, `-1 as U64?`. From a `Float`, `none` also for NaN, an infinity, and
a value with a fraction: `3.5 as Int?` is `none`, `3.0 as Int?` is 3.

**Done 2026-09-30.** Branch-free (generateCheckedCast): a narrowing is a round
trip -- truncate, extend back by the target's sign, compare -- and a same- or
wider-width change of sign is one compare. From a Float the test is "whole, at
least the low bound, below the high one", the bounds being powers of two a
double holds exactly, so `2^63 as I64?` is `none` and `-2^63` is `I64.MIN`; NaN
fails every ordered compare. The value goes through the saturating conversion
so it is never poison. A `T?` source keeps `none`. Int to Float is always
present (a Float's range covers every integer; precision is rounding, as with
`as Float`). None of it allocates. test_245.

### 4. Text to value

`s as T?` for every integer width, `Float` and `Bool`, with `parseInt`'s rules.
`s as T` when `s` is a literal (or an immutable `let` bound to one): converted at
compile time, an error when the text does not parse. Otherwise an error naming
`as T?`.

**Done 2026-09-30, for literals.** `s as T?` is the parse method (`as Int?` is
`parseInt`), bound to std.string. `"12" as Int` is read at compile time by the
same parse the run time uses, and stays a cast of the number literal so
`"18446744073709551615" as U64` is named as `U64`. `"12Sf" as Int` is an error
(neg_247), and so is any non-literal String (neg_246), which names `as Int?`.
**Not done:** an immutable `let` bound to a literal. Sema keeps a binding's type,
not its initializer, and a scoped table of literal values for this one case was
not worth it; the error already says what to write.

### 5. std fill-out

`toString`, `toString(radix)`, `toFloat` and `parse*` on `I8`, `I16`, `U8`,
`U16`, `U32`, `Usize` and `Isize`, which today have none. These are also what
tasks 2-4 lower to.

**Done 2026-09-30, and `parse*` changed shape.** Every `parse` now answers a
scalar `T?` rather than `Option<T>` (decided with the user): no allocation per
parse, and `s as Int?` (task 4) is `s.parseInt()`. `parseI8`, `parseI16`,
`parseIsize`, `parseU8`, `parseU16`, `parseU32` and `parseUsize` are new, each
with a radix overload, range-checked by narrowing the 64-bit parse. The 11
`optionOr(x.parseInt(), d)` sites in `src/` are `x.parseInt().unwrapOr(d)`. The
docs pages that show the `Option` form are task 7.

### 6. Enum and `Int`

A fieldless enum and `Int` are interchangeable in sema: `let c: Color = 7`,
passing `2` for a `Color` parameter, and `7 as Color` all compile, and a `match`
on the result has no arm for it. Refusing only the cast closes nothing and broke
`Color.Blue as Color`, since a variant types as `Int`. A distinct enum type is a
change to how every `.kind == NodeKind.X` in `src/` is checked. Recorded in
`KNOWN_ISSUES.md`; the decision is open.

**Decided and done 2026-09-30: a distinct type.** A variant types as its enum,
and `semaEnumMatchesInt` is gone. `c as Int` names the ordinal; `n as Color`
is an error naming `n as Color?`, which is present for `0 <= n < count` (one
unsigned compare; variants have no written discriminants). `let c: Color = 1`
and an Int argument for a Color are errors, and a match pattern is checked
against the scrutinee's own type. Because a Color can only hold its variants,
a `match` naming every variant is now exhaustive without `_`, so a function
whose arms all return does not fall off its end (semaMatchCoversEnum).

The cost in `src/` was 61 sites, all one pattern: `ASTNode.i1` is an `Int` that
holds a `TokenType`, now written and compared as `TokenType.X as Int`. The
compiler's IR is byte-identical. test_05 and test_22 encoded the old rule and
were updated; test_248, neg_249, neg_250.

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

**State 2026-10-01.** `release_gate.py` against the packaged RC `build/cv-rc3`
passes in full, suite 492/492; the run is recorded in
[`aif/evidence/RESULTS-conversions-release-gate.md`](../aif/evidence/RESULTS-conversions-release-gate.md).
Two harness defects had been hiding it: the gate ran `bin/prismio` inside the
checkout, which forwards to the project host (now run under a neutral name), and
`target_cross` executed an x86_64 binary on a Mac without Rosetta (now reports
`built, not run here`).

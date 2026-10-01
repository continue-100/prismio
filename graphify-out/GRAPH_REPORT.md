# Graph Report - prismio  (2026-10-01)

## Corpus Check
- 924 files · ~1,270,246 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 47 file(s) not represented in the graph (top: .asm 21, (none) 18, .css 3)

## Summary
- 11744 nodes · 31613 edges · 615 communities (486 shown, 129 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 4723 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `450e44af`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ptr_to_node
- bridge.psm
- std/io.psm
- TypeInfo
- aif_support.c
- impl String
- imports.psm
- ASTNode
- llvm-api-backend.c
- model.psm
- nodeIsNull
- compile.psm
- display.psm
- rangeEmitConditionBound
- program_support.c
- context.psm
- string.psm
- report.psm
- __builtin_string_len
- lang_runtime.c
- std/vec.psm
- resolve_value
- ums_cli.psm
- test_98_multiple_trait_bounds.psm
- unicode.psm
- build_driver.c
- ranges.psm
- module.psm
- process.psm
- site_arena_scope
- generate_unicode_tables.py
- mapSet
- run.py
- Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs
- Option
- fs.psm
- NodeKind
- str_with_capacity
- Eq
- map.psm
- Key
- LLVMValueRef
- aif_tier_of
- relations.psm
- AIF — Compiler Requirements
- M4.3b — DataView element reads
- bracket_place
- scanner.psm
- min/max/abs, and the call that used to cost 1.79x
- nominal_find
- aifWalk
- key.psm
- diagnostics.c
- option.psm
- test_102_generic_trait_arguments.psm
- main
- ir_symbols.c
- alpha.psm
- impl Float
- bits_set
- Ord
- Default
- Which std functions are properties
- Architecture direction — what to build next, and what the literature already settled
- aifCallSites
- adversarial.psm
- setup_llvm.py
- command_quote_arg
- unicode_conformance.psm
- aifPrepareOrder
- block_for
- subprocess
- backend_fail
- aifEmitManifest
- compute.cpp
- arena_census.py
- rt_alloc
- join
- test_runner.py
- M5.1 — allocator evaluation
- targets/target.psm
- symbols.psm
- UmsTokenKind
- algorithms.cpp
- benchRun
- UmsDiagnostic
- kv-adaptive-hash-2026-09-06/ceiling.c
- compile_ir_to_object
- list_release
- ir_intern
- impl I16
- key-before.psm
- copy.psm
- test_101_generic_trait_impl.psm
- test_103_default_trait_methods.psm
- AIF — Workload Declaration, Cost Model, and Layout Search
- adversarial.cpp
- compute.psm
- Code Style
- g6_bench.c
- dbm.psm
- The loop range guard was not sound, and the bound it used was one too loose
- time.psm
- aif_differential.py
- di_type_for
- test_127_enum_null_variant.psm
- Cross-language results — Prismio vs Rust vs Swift
- README.md
- prismio_llvm.h
- adversarial.rs
- workspace.psm
- release_gate.py
- The cross-language benchmark — current standing and historical session-3 report
- host.psm
- TokenType
- test_169_loop_range_proofs.psm
- pop
- algorithms.rs
- dump.psm
- run_debug_info_test
- World
- aifEmitBrackets
- test_107_associated_types.psm
- test_116_trait_objects.psm
- World
- preexisting-ownership-repro.psm
- AIF — Design Rationale
- Engine
- TypeKind
- allocPlacedStruct
- aifReportPlacementPin
- impl Parser
- What is actually left on a `List<Int>` loop: the check, not the header
- hashquality.c
- shorthash.c
- aif.py
- build_curated_module
- test_104_where_clauses.psm
- test_118_impl_trait.psm
- Single-probe updates and direct entry lookup
- 1 · AIF core — genuinely ours
- retain
- 4 · Transfer rules
- test_105_supertraits.psm
- test_164_array_fields.psm
- test_71_nonlexical_extent.psm
- LiveProgress
- project.psm
- bench.py
- run
- test_253_void_closure.psm
- find_binding
- struct_entry
- ownership.psm
- test_232_channel_copies.psm
- arena_state
- memory.cpp
- common.psm
- neg_195_callable_bound.psm
- platform.psm
- aif_concurrency.psm
- debug_info.psm
- assert
- test_115_trait_imports.psm
- test_92_field_view_provenance.psm
- test_map_update.psm
- Decisions
- g5_asset_cache.psm
- benchPrint
- Particle
- src/main.psm
- E1: the push check belongs in the preheader, and the profile it was said to need does not exist
- layout.py
- AIF — The T4 Cycle Collector
- next_random
- compute.rs
- bits_test
- 11 · Known weaknesses
- Performance: what is open, and how to measure it
- main
- package.py
- test_100_generic_inherent_impl.psm
- test_240_overload_exactness.psm
- test_70_struct_field_release.psm
- compiler_plib_interface
- AIF — Measurement and Falsification Plan
- spin_probe.c
- .solve
- test_map_probe.psm
- Contributing to Prismio
- run_module_artifact_test
- manifest_writer.psm
- test_111_blanket_impls.psm
- test_128_enum_null_reserved.psm
- test_69_task_results.psm
- validation.psm
- Model
- C code style
- decl_entry
- rt_base_alloc
- run_bootstrap_cache_key_test
- Counted scalar fills and struct-list initialization
- M4.3a — explicit DataView conversion boundary
- .toString
- aif_tiers.psm
- test_108_trait_method_namespaces.psm
- test_109_trait_ownership.psm
- test_58_region_serves.psm
- Profile
- PIR — Prism Semantic IR
- tokenization
- memory.rs
- aif_manifest_diff.py
- M4.1 — first-class `Slice<T>`
- lexCheckIdentifierSecurity
- test_165_ranges_repeat_labels.psm
- neg_165_array_field_refused.psm
- test_132_counted_fill.psm
- test_157_shared_container_elements.psm
- test_170_match_switch.psm
- test_47_aif_containers.psm
- test_49_aif_struct_fields.psm
- test_87_traits.psm
- check_source_lists.py
- g4_ecs_world.psm
- .sites_of
- neg_107_impl_trait_return_mismatch.psm
- test_163_array_return.psm
- test_154_extern_globals.psm
- test_130_list_alias_scopes.psm
- test_177_type_functions.psm
- test_55_workload_profile.psm
- The relational tier, byte-sized Bool elements, and three gaps read from disassembly
- command.psm
- ceiling-knapsack.c
- The integer-print leak, and g6's arena
- cost.c
- 8 · Annotations as axioms and constraints
- common/target.psm
- 3 · The tier ladder
- main
- test_155_vec_methods.psm
- 5.4 `pin`
- test_121_guard_effect_analysis.psm
- test_82_generic_layout.psm
- test_184_call_result_ownership.psm
- test_192_callable_bounds.psm
- test_216_for_push_guard.psm
- test_42_aif_stack_promotion.psm
- test_68_optional_returns.psm
- test_99_trait_coherence.psm
- g3_scene_graph.psm
- benchmarks.hpp
- Compile time — where it goes, and what it scales like
- `Int` width — the decision, and the three measurements that made it
- Loop versioning exposes Prismio's flat-list fast path
- test_73_recursive_release.psm
- M4.4 — generic/container layout specialization
- AIF — The Target Workload
- AIF — Adaptive Inference Framework
- Channels: what 0.1 needs, and the production design after it
- 6 · Ownership contexts
- 4 · Tier derivation
- neg_65_generic_trait_impl_bound.psm
- neg_84_transitive_supertrait.psm
- test_148_struct_index.psm
- test_167_frame_struct_fields.psm
- test_238_scalar_optionals.psm
- test_66_payload_enums.psm
- test_86_impl_blocks.psm
- stdio
- float_builtins.psm
- layout_repr.c
- compile_bench.py
- `key_value_update`: the hash was the cost, and four other things were not
- test_62_split_release.psm
- The 2026-09-30 `--verify` sweep
- AIF Evidence
- io.rs
- Debugging Prismio programs
- install.sh
- namelist_contains
- neg_66_overlapping_generic_trait_impl.psm
- neg_93_ambiguous_trait_method.psm
- neg_94_wrong_trait_qualifier.psm
- test_05_enums.psm
- test_64_generics.psm
- test_126_push_predication.psm
- test_129_enum_null_ownership.psm
- test_179_proved_index_nsw.psm
- test_231_cold_functions.psm
- test_51_optional_refs.psm
- test_52_aif_cycle_collector.psm
- test_72_reassigned_ownership.psm
- test_74_reinit_assignment.psm
- A payload-free enum variant allocated uninitialised memory
- AIF — Evaluation as a General-Purpose Memory Model
- test_63_placement_pin.psm
- Binary size and compile time against C++ and Rust (2026-09-28)
- 6 · The tier manifest
- run_forced_layout_test
- forDirection
- MEM-033: the cycle collector stops locking when there is nothing to lock against
- maphash.psm
- AIF — Adaptive Inference Framework
- 8.4 Views — slices and element references
- color_enabled
- Style
- test_181_std_math.psm
- test_193_map_methods.psm
- test_48_aif_shared_elements.psm
- test_56_list_capacity.psm
- test_57_pin_tiers.psm
- test_59_bracket_summary.psm
- test_84_task_release.psm
- test_96_channels.psm
- test_256_string_view_pushed_twice.psm
- Genuinely-cold compilation
- Prismio performance benchmarks
- An `extern` declared `alias` no longer outlives the argument it returns
- Progress
- aif_ledger_init
- Map probing and full-width key hashing
- Debug-mode integer overflow checking
- A `spawn`ed call's owned temporary argument now has an owner
- test_120_min_max_abs.psm
- 5 · Annotations
- test_30_diamond_imports.psm
- neg_57_second_bound_not_satisfied.psm
- neg_68_blanket_trait_impl.psm
- range_direction_probe.psm
- test_123_loop_range_guard_wrap.psm
- test_144_sort_inline_elements.psm
- test_15_compiler_sim.psm
- test_166_for_each_collections.psm
- test_171_default_values.psm
- test_187_properties.psm
- test_22_match.psm
- test_53_aif_views.psm
- test_60_bracket_reset.psm
- test_79_slices.psm
- bootstrap.sh
- AIF Corpus
- g2_frame_loop.psm
- g2_bench.psm
- g7_particles.psm
- noise floor that decided it
- M2.1b — consuming same-tag rebuilds reuse their input block
- vec_push
- .charAt
- sort_strings
- v0.1 release candidate — the complete local gate
- AIF — The Inference Engine
- 5 · The fixed-point algorithm
- 7 · Specialisation strategy and dedup
- suite.rs
- ir_jit_run_file
- range_proof_entry
- Releasing Prismio
- Security Policy
- neg_101_dyn_self_not_object_safe.psm
- neg_104_dyn_returned.psm
- neg_241_optional_impl_overlap.psm
- neg_45_bound_not_satisfied.psm
- neg_58_second_bound_not_trait.psm
- neg_82_missing_supertrait.psm
- neg_91_unknown_projection.psm
- neg_92_equality_constraint.psm
- test_01_variables.psm
- test_04_structs.psm
- test_100_reuse_token.psm
- test_100_string_append_reuse.psm
- test_119_loop_range_guard.psm
- test_156_index_store.psm
- test_188_stdin.psm
- test_235_channel_owned_messages.psm
- test_248_enum_is_a_type.psm
- test_29_overloads.psm
- test_50_scalar_lists.psm
- test_80_data_view_conversion.psm
- A binding that escapes through a callee's return was freed under its caller
- How to use it
- A general affine index matcher, built and reverted
- main
- Null empty variants for boxed recursive enums
- AIF — Engine/Game Boundary Results (A2)
- M4.3c — mutable DataView round trip
- The generated release loops on its tail self field
- AIF Prototype
- 2 · Fact domains
- neg_192_property_declaration.psm
- neg_251_array_length_unknown.psm
- Shape
- neg_44_impl_generic.psm
- neg_60_unrelated_method_not_conformance.psm
- neg_67_generic_trait_conformance.psm
- neg_69_generic_trait_method_parameter.psm
- neg_72_missing_bound_trait_argument.psm
- neg_73_trait_argument_bound_mismatch.psm
- impl From for String
- neg_77_missing_method_with_defaults.psm
- neg_78_default_body_unknown_call.psm
- neg_80_where_bound_not_satisfied.psm
- neg_89_missing_associated_type.psm
- neg_96_trait_inout_not_honoured.psm
- owned_return_depth2.psm
- owned_temporary_argument.psm
- recursive_enum_bindings_probe.psm
- test_122_loop_local_index_term.psm
- test_124_whole_buffer_copy.psm
- test_125_stencil_range_guard.psm
- test_138_shadowing.psm
- test_13_globals.psm
- test_140_string_search.psm
- test_14_multi_args.psm
- test_158_sized_arrays.psm
- test_162_removal_parks_under_view.psm
- test_19_runtime_split.psm
- test_25_conventions.psm
- test_38_scoping.psm
- test_61_layout_cost_model.psm
- ast.psm
- impl Int
- MEM-035: the stencil's offsets were never the problem — its condition was
- 1. Architecture
- 5. Ownership, handles, and globals
- 8. Comments
- test_fft_direct.psm
- neg_109_impl_trait_bound.psm
- neg_161_index_store_refused.psm
- Color
- Shape
- neg_46_impl_missing_method.psm
- neg_70_missing_trait_argument.psm
- neg_71_extra_trait_argument.psm
- neg_74_trait_argument_conformance.psm
- neg_76_unknown_trait_argument_type.psm
- neg_83_supertrait_cycle.psm
- neg_85_missing_associated_constant.psm
- neg_86_associated_constant_type.psm
- neg_87_associated_constant_not_global.psm
- neg_95_trait_sink_not_honoured.psm
- test_10_expressions.psm
- test_142_sort_patterns.psm
- test_143_string_compare.psm
- test_16_arrays.psm
- test_174_slice_mut.psm
- test_217_vec_filled.psm
- test_21_loops.psm
- test_26_borrow_reuse.psm
- test_73_recursive_release_depth.psm
- test_88_single_loop_inline.psm
- The G2 / G6 benchmark set
- AIF — Cross-Language Comparison Suite
- build_tree
- aif_concurrency_shared.psm
- extern_alias_escape.psm
- neg_102_dyn_associated_type.psm
- neg_103_dyn_in_struct_field.psm
- neg_108_impl_trait_position.psm
- neg_187_bare_type_function.psm
- Color
- Color
- Result
- neg_43_impl_self_position.psm
- scoreWith
- neg_62_unconstrained_generic_impl.psm
- neg_64_duplicate_impl_method_parameter.psm
- neg_79_where_unknown_parameter.psm
- neg_81_where_bound_not_trait.psm
- pointer_return_temp.psm
- recursive_optional_probe.psm
- test_02_if_else.psm
- test_03_while_loops.psm
- test_06_recursion.psm
- test_07_booleans.psm
- test_08_mutability.psm
- test_11_returns.psm
- test_149_list_literal.psm
- test_161_removal_releases_now.psm
- test_18_floats.psm
- test_206_nested_loop_breaks.psm
- test_23_move.psm
- test_33_unary_operators.psm
- test_41_punned_slot_bytes.psm
- test_93_data_view_from_helper.psm
- test_95_literal_tbaa.psm
- bootstrap.ps1
- g9_bands.psm
- Conversions: the release gate, run on a packaged RC
- common.rs
- aif_loop_bracket.psm
- fixture_slice_escape.psm
- neg_05_drop_borrow.psm
- neg_105_dyn_unknown_trait.psm
- neg_153_extern_global_declaration.psm
- neg_155_extern_global_type.psm
- neg_160_empty_literal_untyped.psm
- neg_176_param_not_inout.psm
- neg_198_array_type_argument.psm
- neg_22_push_borrowed_element.psm
- use_it
- neg_24_unique_aliased_args.psm
- neg_25_pin_refuted.psm
- neg_26_placement_pin_refuted.psm
- neg_47_unknown_trait.psm
- neg_48_bound_not_a_trait.psm
- neg_61_duplicate_trait_impl.psm
- neg_63_impl_for_type_parameter.psm
- neg_88_trait_constant_with_value.psm
- neg_90_trait_associated_type_value.psm
- neg_97_nonterminating_instantiation.psm
- target_cross.psm
- test_133_string_dispatch.psm
- test_134_print_arguments.psm
- test_139_string_chain_append.psm
- test_145_list_set_within_list.psm
- test_159_vec_binding_empty.psm
- test_160_i32_alias.psm
- test_180_descending_ranges.psm
- test_24_drop.psm
- test_28_list.psm
- test_31_strings_in_control_flow.psm
- test_32_sized_int_modulo.psm
- test_40_annotated_arrays.psm
- test_53_memory_budget.psm
- refresh_seed.sh
- scalar_list_read.psm
- scalar_list_sieve.psm
- scalar_list_write.psm
- test_bfs.psm
- aif_vec_display.psm
- neg_01_type_mismatch.psm
- neg_03_use_after_move.psm
- neg_04_use_after_drop.psm
- neg_08_missing_return.psm
- neg_100_for_over_non_iterator.psm
- neg_100_struct_index_without_at.psm
- neg_10_move_in_loop.psm
- neg_13_syntax_recovery.psm
- neg_14_wrong_arity.psm
- neg_158_vec_last_needs_name.psm
- neg_16_return_local_array.psm
- neg_172_default_without_type.psm
- neg_183_slice_returned_read_only.psm
- neg_189_code_after_panic.psm
- neg_207_break_outer_leaves_loop.psm
- neg_21_container_takes_ownership.psm
- neg_224_type_without_new.psm
- neg_233_channel_runtime_names.psm
- neg_23_optional_needs_unwrap.psm
- neg_27_generic_arity.psm
- neg_36_soa_non_flat.psm
- neg_38_data_view_field.psm
- neg_39_soa_moves_source.psm
- neg_40_data_element_escape.psm
- neg_41_list_set_exclusive_observed.psm
- neg_42_list_set_exclusive_inline.psm
- neg_50_closure_param_type.psm
- neg_56_channel_send_moves.psm
- neg_99_compare_without_ord.psm
- platform_target.psm
- scalar_optional_expect_probe.psm
- test_117_block_comments.psm
- test_20_integers.psm
- test_213_digit_separators.psm
- test_27_for.psm
- test_36_casts.psm
- test_37_bitwise_and_compound.psm
- test_81_data_view_drop.psm
- test_83_list_set_exclusive.psm
- ablations.sh

## God Nodes (most connected - your core abstractions)
1. `ASTNode` - 683 edges
2. `ptr_to_node()` - 595 edges
3. `nodeExists()` - 444 edges
4. `__builtin_string_len()` - 246 edges
5. `nodeIsNull()` - 208 edges
6. `node_to_ptr()` - 183 edges
7. `TypeInfo` - 178 edges
8. `generateCall()` - 136 edges
9. `ptr_null()` - 115 edges
10. `ir_get_temp_name()` - 104 edges

## Surprising Connections (you probably didn't know these)
- `Current limitations` --references--> `release()`  [INFERRED]
  ums/ARCHITECTURE.md → aif/corpus/g5_asset_cache.psm
- `Manifest syntax` --references--> `release()`  [INFERRED]
  ums/README.md → aif/corpus/g5_asset_cache.psm
- `5 · What was rejected` --references--> `gcd_lcm()`  [INFERRED]
  aif/evidence/RESULTS-knapsack-flat-set.md → benchmarks/cpp/algorithms.cpp
- `3 · The benchmark sweep` --references--> `tree_traversal()`  [INFERRED]
  aif/evidence/RESULTS-push-predication.md → benchmarks/cpp/algorithms.cpp
- `Element references are views too — the deep consequence` --references--> `Particle`  [INFERRED]
  aif/spec/SPEC.md → benchmarks/cpp/compute.cpp

## Import Cycles
- None detected.

## Communities (615 total, 129 thin omitted)

### Community 0 - "ptr_to_node"
Cohesion: 0.03
Nodes (238): 2 · Order of work and status, aifArgTypeAt(), aifAnnotationLeafName(), aifFieldTypeName(), aifLayoutFixStandardLibrary(), aifRegisterTypeEdges(), aifNodeType(), aifBindPayloadArm() (+230 more)

### Community 1 - "bridge.psm"
Cohesion: 0.02
Nodes (472): Kept from the attempt, What changed, 4 · The shape of the change (as planned), The AIF oracle, nodeGetType(), nodeHasType(), typeIntBits(), typeIrKey() (+464 more)

### Community 2 - "std/io.psm"
Cohesion: 0.02
Nodes (123): prismio_rt_eprint_float(), prismio_rt_eprintln_float(), prismio_rt_print_float(), prismio_rt_println_float(), str_with_capacity(), eprint(), eprint(), eprint() (+115 more)

### Community 3 - "TypeInfo"
Cohesion: 0.06
Nodes (134): The surface, 4. Optional / nullable reference fields — **DONE, 2026-08-07; return position 2026-08-19**, aifLayoutVetoDataViews(), ir_extern_decl_record(), ir_index_decl(), ir_reset_decl_index(), ptr_to_type(), type_to_ptr() (+126 more)

### Community 4 - "aif_support.c"
Cohesion: 0.02
Nodes (74): aif_arena_range_first(), aif_arena_range_last(), aif_auto_arena_at_node(), aif_call_edge(), aif_call_opaque(), aif_check_placement_pins(), aif_con_arg(), aif_con_bind() (+66 more)

### Community 5 - "impl String"
Cohesion: 0.02
Nodes (54): 9 · Case mapping: a search per scalar was 5.4× Rust, Language surface, str_find_byte(), str_find_needle(), charIsSpace(), strClone(), strContains(), strContainsChar() (+46 more)

### Community 6 - "imports.psm"
Cohesion: 0.10
Nodes (41): diag_finish(), compiler_plib_error(), compiler_plib_interface(), current_directory(), executable_directory(), file_exists(), get_directory(), join_path() (+33 more)

### Community 7 - "ASTNode"
Cohesion: 0.03
Nodes (240): Two missing edges, and a missing type, Answer: Prismio chooses after substitution, node_to_ptr(), ptr_null(), createNode(), nodeList(), nodeListPush(), nodeMarkCold() (+232 more)

### Community 8 - "llvm-api-backend.c"
Cohesion: 0.03
Nodes (82): What changed, Toolchain layout, assign_partitions(), check_llvm_version(), clear_packaging_target_attributes(), codegen_partition_count(), codegen_thread_budget(), copy_attributes_at_index() (+74 more)

### Community 9 - "model.psm"
Cohesion: 0.03
Nodes (89): aif_check_pins(), aif_check_placement_pins(), aif_compute_type_acyclic(), aif_con_bind(), aif_con_fn(), aif_con_pin(), aif_con_pin_region(), aif_con_unique() (+81 more)

### Community 10 - "nodeIsNull"
Cohesion: 0.06
Nodes (94): 3 · What it was, 7 · What is left, measured, 8 · A binding returned on one path leaked on the others, 3 · How, ptr_is_null(), nodeIsCallableBound(), nodeIsNull(), ir_named_type_kind() (+86 more)

### Community 11 - "compile.psm"
Cohesion: 0.06
Nodes (59): aif_layout_force_applied(), aif_layout_forced_count(), aif_layout_forced_hot(), aif_layout_forced_type(), diag_add_file(), diag_error_count(), diag_progress_begin(), diag_progress_clear() (+51 more)

### Community 12 - "display.psm"
Cohesion: 0.03
Nodes (63): impl Display for Bool, impl Display for Char, impl Display for Float, impl Display for I16, impl Display for I64, impl Display for I8, impl Display for Int, impl Display for Isize (+55 more)

### Community 13 - "rangeEmitConditionBound"
Cohesion: 0.13
Nodes (32): ir_add(), ir_mul(), ir_sub(), generateForRangeGuard(), rangeBinaryInterval(), rangeBindsInPattern(), rangeBindsInPatternChain(), rangeBodyDeclares() (+24 more)

### Community 14 - "program_support.c"
Cohesion: 0.04
Nodes (47): 15. Concurrency / task model — **DONE, 2026-08-19**, spawn_and_wait(), prismio_memory_thread_enter(), append_module_name(), chan_bytes_ready(), chan_send_copy(), current_directory(), directory_exists() (+39 more)

### Community 15 - "context.psm"
Cohesion: 0.03
Nodes (63): aif_call_arg_outlives_call(), aif_call_arg_retained(), aif_elem_literal_copies_only(), aif_elem_owner_at_node(), aif_elem_type_at_node(), aif_field_is_cyclic(), aif_field_release(), aif_frees_unless_returned_node() (+55 more)

### Community 16 - "string.psm"
Cohesion: 0.03
Nodes (91): main(), makeView(), main(), 6 · What is left, Resolved in 1.1 — was open in v1.0, 2. `json_parse` and `json_serialize` — P1, Checklist, Model and public surface to settle (+83 more)

### Community 17 - "report.psm"
Cohesion: 0.07
Nodes (58): aif_alias_name(), aif_arena_blockers(), aif_cause_build(), aif_cause_col(), aif_cause_domain_for(), aif_cause_file(), aif_cause_line(), aif_cause_rule() (+50 more)

### Community 18 - "__builtin_string_len"
Cohesion: 0.04
Nodes (93): `key_value_update`: one probe in `mapSet`, and a loop guard that is a net loss, Reproduce, Verification, What is left, and where it is, What was built: `mapSet` stops asking a question the probe answered, What was refuted: the flat guard for `loop` and `for`, Where the time is, Verification of the final compiler (+85 more)

### Community 19 - "lang_runtime.c"
Cohesion: 0.03
Nodes (79): 1 · What was built, Method, 2.2 · Correctness of the runtime model, arena_current_slot(), cyc_alloc(), cyc_buffer(), cyc_collect(), cyc_collect_now() (+71 more)

### Community 20 - "std/vec.psm"
Cohesion: 0.04
Nodes (17): listHeapSort(), listInsertionSort(), listPartialInsertionSort(), listPartitionLeft(), listPartitionRight(), listSiftDown(), listSort2(), listSort3() (+9 more)

### Community 21 - "resolve_value"
Cohesion: 0.08
Nodes (68): array_base(), array_copy_bytes(), array_slot(), block_done(), data_view_tbaa_tag(), intern_value(), ir_array_alloca(), ir_array_alloca_zeroed() (+60 more)

### Community 22 - "ums_cli.psm"
Cohesion: 0.06
Nodes (81): diag_error_code(), diag_print_help(), diag_set_json_mode(), compiler_spawn_arg(), compiler_spawn_wait(), compileOptions(), CompileOptions, ir_set_opt_level() (+73 more)

### Community 23 - "test_98_multiple_trait_bounds.psm"
Cohesion: 0.28
Nodes (8): activeScore(), checkedScore(), main(), impl Enabled for Int, impl Scored for Int, Gate, Enabled, Scored

### Community 24 - "unicode.psm"
Cohesion: 0.05
Nodes (62): 1 · The tables came from the interpreter, and the interpreter was wrong, 2 · Conformance, against the UCD's own tests, 3 · Representation: readable, after one codegen fix, 4 · std.unicode, before and after, 5 · Identifiers: UAX #31, 6 · Verification, Unicode 18.0.0 from the UCD, UAX #31 identifiers, and constant array literals, scalarWidth() (+54 more)

### Community 25 - "build_driver.c"
Cohesion: 0.04
Nodes (76): accept_if_exists(), append_joined_argument(), append_quoted_argument(), clang_identity(), compare_dotted_versions(), compiler_binary_hash(), compiler_check_executable(), compiler_check_host_abi() (+68 more)

### Community 26 - "ranges.psm"
Cohesion: 0.08
Nodes (76): ir_range_proof_new(), ir_range_trace(), generateWhileRangeGuard(), rangeAddVar(), rangeApplyUpdate(), rangeBitCount(), rangeBoundingVar(), rangeBoundSideOk() (+68 more)

### Community 27 - "module.psm"
Cohesion: 0.04
Nodes (88): `sort()` from a packaged `.plib`, nodeIsCold(), ir_decl_at(), ir_decl_count(), diag_file_module(), ir_blank_line(), ir_clear_var_types(), ir_declare_function_begin() (+80 more)

### Community 28 - "process.psm"
Cohesion: 0.06
Nodes (42): main(), StreamMode, Inherit, proc_close(), proc_env_get(), proc_env_has(), proc_env_remove(), proc_env_set() (+34 more)

### Community 29 - "site_arena_scope"
Cohesion: 0.11
Nodes (21): 1 · The headline, 2 · Why an escape-lattice change does not move this, 3 · The measurement that was wrong twice, and why, 4 · `region` measured on g2, 5 · What a region *can* serve, 6 · `list_new_with_capacity`, the one speed result, 7 · What would actually close this, 9 · Call-site placement, landed *(2026-08-16, second session)* (+13 more)

### Community 30 - "generate_unicode_tables.py"
Cohesion: 0.07
Nodes (36): array_rows(), case_column(), case_folding(), case_tables(), compositions(), confusables(), data_lines(), decompositions() (+28 more)

### Community 31 - "mapSet"
Cohesion: 0.12
Nodes (48): clock_gettime(), intProbe(), main(), now(), stringProbe(), wideProbe(), Stamp, main() (+40 more)

### Community 32 - "run.py"
Cohesion: 0.10
Nodes (28): build_all(), build_key(), command_text(), elimination_benchmarks(), elimination_cell(), elimination_row(), execute(), format_bytes() (+20 more)

### Community 33 - "Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs"
Cohesion: 0.50
Nodes (3): Findings worth keeping, Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs, Numbers (scale 4)

### Community 34 - "Option"
Cohesion: 0.05
Nodes (43): 1 · The shapes, 3 · What moved, 4 · Pinned, Three ownership shapes that freed memory that was not live, Option, None, Some, impl Option (+35 more)

### Community 35 - "fs.psm"
Cohesion: 0.06
Nodes (63): 4 · The toolchain object cache, 5 · Why `std.input` and not `std.io`, and the workload link, benchLineProcessing(), rt_workload_stub(), current_directory(), delete_file(), directory_exists(), executable_directory() (+55 more)

### Community 36 - "NodeKind"
Cohesion: 0.04
Nodes (57): NodeKind, ARRAY_LITERAL_EXPR, ASSIGNMENT_STATEMENT, ASSOC_CONST, ASSOC_TYPE, ASSOC_TYPE_REF, BINARY_EXPR, BLOCK (+49 more)

### Community 37 - "str_with_capacity"
Cohesion: 0.11
Nodes (18): 3.2 The procedure, str_with_capacity(), strEmpty(), prismio_rt_color_supported(), colorEnabled(), stderrColorEnabled(), termByte(), termFill() (+10 more)

### Community 38 - "Eq"
Cohesion: 0.06
Nodes (36): impl Eq for Bool, impl Eq for Char, impl Eq for Float, impl Eq for I16, impl Eq for I64, impl Eq for I8, impl Eq for Int, impl Eq for Isize (+28 more)

### Community 39 - "map.psm"
Cohesion: 0.07
Nodes (30): 9.1 · It is not the representation. The boxed layout is *free* here, mapBucketOfEntry(), mapClear(), mapEmpty(), mapFromEntries(), mapHashOf(), mapInitialCapacity(), mapInsert() (+22 more)

### Community 40 - "Key"
Cohesion: 0.11
Nodes (45): mapGet(), mapGetOr(), mapHas(), mapIndexOf(), mapInitialCapacity(), mapKeyAt(), mapLen(), mapNew() (+37 more)

### Community 41 - "LLVMValueRef"
Cohesion: 0.08
Nodes (39): apply_param_attrs(), build_bswap64(), build_three_way(), byte_gep(), coerce_for(), debug_clear_location(), ir_call_arg_borrow(), ir_call_arg_cstr() (+31 more)

### Community 42 - "aif_tier_of"
Cohesion: 0.07
Nodes (40): 8 · How much call-site bracketing could reach *(2026-08-16)*, 3 · The mechanism, 1 · The defect, 2 · Why it did not need a fixed point, 3 · Before / after, 4 · What is still declined, Ownership survives a second return, 1 · The baseline (+32 more)

### Community 43 - "relations.psm"
Cohesion: 0.08
Nodes (60): ir_icmp_sge(), ir_icmp_sle(), ir_list_data(), ir_range_proof_mark(), ir_range_proof_marked(), dbmGet(), rangeDataFor(), rangeEmitAccess() (+52 more)

### Community 44 - "AIF — Compiler Requirements"
Cohesion: 0.14
Nodes (14): 13. Generic containers — `Map<K,V>`, growable `Vec<T>` — **PARTLY DONE, 2026-08-19**, 17. `Int` ↔ `Float` conversion **[minor]**, 18. Struct size / layout introspection **[minor]**, 1. Affine collections — `String`, `List<T>`, arrays become move-only **[done, 2026-08-07]**, 20. `List<T>` miscompiles for scalar element types — **DONE, 2026-08-07**, 21. PIR — the compiler's IR and package-distribution format **[compiler track]**, 2. `region { }` — keyword, arena runtime, handle threading **[done, 2026-08-07]**, 3. Shared references **[blocker for T3/T4]** (+6 more)

### Community 45 - "M4.3b — DataView element reads"
Cohesion: 0.29
Nodes (6): Correctness and closure gates, M4.3b — DataView element reads, Next gate, Read-only layout gate, Standard-corpus regression gate, What changed

### Community 46 - "bracket_place"
Cohesion: 0.06
Nodes (59): 0. What this session was asked to do, and why it did something else, 1. The census, before, 2. The recorded blocker was a circularity, not a missing obligation, 3. A latent soundness hole, found by turning the feature on, 4. What it buys, measured, 5. Where it does not fire, and why each is correct, 6. Gate, M3.1 — automatic call-site placement reaches a callee's allocations (+51 more)

### Community 47 - "scanner.psm"
Cohesion: 0.18
Nodes (48): charCode(), isOperator(), isSeparator(), exit(), byteText(), hexDigitValue(), isHexDigit(), isRadixDigit() (+40 more)

### Community 48 - "min/max/abs, and the call that used to cost 1.79x"
Cohesion: 0.33
Nodes (5): 1 · Why this existed, 2 · What was built, 3 · What it is worth, 5 · What is still declined, min/max/abs, and the call that used to cost 1.79x

### Community 49 - "nominal_find"
Cohesion: 0.06
Nodes (49): 2 · The rule that replaced it, aif_con_pin_region(), aif_elem_key(), aif_enum_new(), aif_field_access(), aif_field_has_range(), aif_field_is_counted(), aif_field_is_cyclic() (+41 more)

### Community 50 - "aifWalk"
Cohesion: 0.07
Nodes (41): aif_con_at(), aif_con_live_in(), aif_con_return_binding(), aif_con_return(), aif_con_spawn(), aif_con_store(), aif_elem_key(), aif_field_access() (+33 more)

### Community 51 - "key.psm"
Cohesion: 0.05
Nodes (24): keyHashBytes(), keyMixInt(), keyMixWide(), keyStrengthen(), impl Key for Bool, impl Key for Char, impl Key for I64, impl Key for Int (+16 more)

### Community 52 - "diagnostics.c"
Cohesion: 0.08
Nodes (43): 10 · Trojan Source and UTS #39, tested, diag_add_file(), diag_detect_color(), diag_digits(), diag_elapsed(), diag_emit(), diag_emit_json(), diag_emit_json_summary() (+35 more)

### Community 53 - "option.psm"
Cohesion: 0.06
Nodes (34): A field read is a view of the object it was read from, Scope, The defect, Verification, What it costs, 14. Error handling — tagged unions, `Option` / `Result` — **DONE, 2026-08-19**, Result, Err (+26 more)

### Community 54 - "test_102_generic_trait_arguments.psm"
Cohesion: 0.08
Nodes (28): impl ScaleBy for String, acceptsWrapped(), crossTag(), fail(), main(), make(), sameTag(), scaleWithBool() (+20 more)

### Community 55 - "main"
Cohesion: 0.06
Nodes (9): impl I64, impl Isize, impl U16, impl U32, impl U64, impl U8, impl Usize, fail() (+1 more)

### Community 56 - "ir_symbols.c"
Cohesion: 0.05
Nodes (12): drop_index(), ir_drop_kind(), ir_drop_slot(), ir_drop_type(), ir_loop_break_label_named(), ir_loop_continue_label_named(), ir_loop_drop_floor(), ir_loop_drop_floor_named() (+4 more)

### Community 57 - "alpha.psm"
Cohesion: 0.08
Nodes (27): main(), main(), main(), main(), fail(), main(), main(), main() (+19 more)

### Community 58 - "impl Float"
Cohesion: 0.04
Nodes (5): 1 · `tools/release_gate.py`, The v0.1 gate and benchmark matrix on the branch head, 2026-09-25, benchFft(), benchFftTransform(), impl Float

### Community 59 - "bits_set"
Cohesion: 0.14
Nodes (34): aif_oom(), bits_clear(), bits_count_at_least_two(), bits_ensure(), bits_free(), bits_is_empty(), bits_or(), bits_set() (+26 more)

### Community 60 - "Ord"
Cohesion: 0.06
Nodes (28): impl Ord for Char, impl Ord for Float, impl Ord for I16, impl Ord for I64, impl Ord for I8, impl Ord for Int, impl Ord for Isize, impl Ord for String (+20 more)

### Community 61 - "Default"
Cohesion: 0.08
Nodes (23): impl Default for Bool, impl Default for Char, impl Default for Float, impl Default for I16, impl Default for I64, impl Default for I8, impl Default for Int, impl Default for Isize (+15 more)

### Community 62 - "Which std functions are properties"
Cohesion: 0.08
Nodes (17): Landing, Properties are declared: `prop`, Still open, The rule before, The rule now, Which std functions are properties, 0. The two halves, and why neither ships alone, charDigitValue() (+9 more)

### Community 63 - "Architecture direction — what to build next, and what the literature already settled"
Cohesion: 0.17
Nodes (12): 0 · The diagnosis, and the one thing everybody had backwards, 1 · Close the runtime seam — built, with one deployment decision left, 2 · Reuse analysis — useful only where the program has its trigger shape, 3 · Regions: go non-lexical and polymorphic, 4 · Views and slices — bounded views and mutable data views shipped, 5 · The allocator — measured and closed for the current workload, 6 · The ranked plan, 7 · Measured dead ends — do not re-derive these (+4 more)

### Community 64 - "aifCallSites"
Cohesion: 0.07
Nodes (42): 2 · What it was not, 5 · What is still open, 1 · The blocker, as recorded and as measured, 2.3 · Middle IR and interprocedural facts, aifCallIsSummarised(), aifCompilerBuiltinContract(), aifDeclaredContract(), aifDeclaredReturnIsAlias() (+34 more)

### Community 65 - "adversarial.psm"
Cohesion: 0.13
Nodes (26): Residuals, measured and not fixed, benchAdversarialNext(), benchAllocationEscape(), benchAosVsSoa(), benchBranchMispredict(), benchConsumeAdversarialObject(), benchDeadCodeElimination(), benchDeadKernel() (+18 more)

### Community 66 - "setup_llvm.py"
Cohesion: 0.07
Nodes (47): release(), C3, `verify` mode — every inferred fact becomes a runtime assertion, 10. Per-module optimisation levels **[specified 2026-08-17, not implemented]**, 11. `verify` build mode **[needed]**, 12. Handles instead of raw pointers **[needed, long-horizon]**, 5. A pass between sema and codegen **[enabling]**, 6. Three allocation hooks, not one **[needed]** (+39 more)

### Community 67 - "command_quote_arg"
Cohesion: 0.12
Nodes (32): 7.1 Fixed, 2026-08-17 (compile time), 7 · `tools/ir_snapshot.py` reports a false difference when anything else compiles the same tree, absolute_directory(), compiler_build_executable(), compiler_jit_run(), compiler_run_executable_with(), compiler_run_workload(), compiler_temp_ir_path() (+24 more)

### Community 68 - "unicode_conformance.psm"
Cohesion: 0.08
Nodes (35): 7 · The ASCII regression was the caller's loop, not `toUpper`'s, identifierSkeleton(), builderPiece(), strFromScalar(), impl StringBuilder, StringBuilder, firstByte(), main() (+27 more)

### Community 69 - "aifPrepareOrder"
Cohesion: 0.26
Nodes (12): aif_fn_symbol(), aif_order_add(), aif_order_count(), aif_order_site(), aif_order_sort(), aif_site_ordinal(), aifEmitHumanGroup(), aifExplain() (+4 more)

### Community 70 - "block_for"
Cohesion: 0.17
Nodes (27): block_for(), element_from_memory(), element_memory_type(), element_to_memory(), flat_element_address(), ir_br_numbered(), ir_cond_br_numbered(), ir_get_label() (+19 more)

### Community 71 - "subprocess"
Cohesion: 0.04
Nodes (43): digest(), main(), run(), digest(), main(), run(), main(), run_once() (+35 more)

### Community 72 - "backend_fail"
Cohesion: 0.08
Nodes (36): apply_borrow_attrs(), backend_fail(), const_from_text(), grow_table(), ir_alloca(), ir_array_literal_elem(), ir_br(), ir_call_arg() (+28 more)

### Community 73 - "aifEmitManifest"
Cohesion: 0.07
Nodes (30): Found on the way, aif_arena_high_water(), aif_arena_unsized_sites(), aif_layout_best(), aif_layout_cand_bytes(), aif_layout_cand_hot(), aif_layout_cand_ratio(), aif_layout_hot_count() (+22 more)

### Community 74 - "compute.cpp"
Cohesion: 0.10
Nodes (17): BenchSphere, cb, cg, cr, r, x, y, z (+9 more)

### Community 75 - "arena_census.py"
Cohesion: 0.10
Nodes (14): blockers_for(), main(), manifest_symbols(), programs(), summary_brackets(), 1 · Decisions, `Array<T, N>` is an array whose length is part of its type, Collections (+6 more)

### Community 76 - "rt_alloc"
Cohesion: 0.05
Nodes (51): The finding that motivated it, 2 · The leak, 3 · Throughput, 4 · Reproducing, Standard input, and the arena that could not serve a C allocation, 0 · Why this file exists, 1 · The measurement, 2 · What was wrong: `str_substring` rescans the whole buffer (+43 more)

### Community 77 - "join"
Cohesion: 0.25
Nodes (9): 1 · Why the item existed, 2.1 The mechanism, and it is not a wash, 2 · Where Prismio stands, 3 · What the program found immediately, 5 · Defect 2 — a callee-allocated argument still leaks, and it is not about spawn. Open., 6 · Gates, The concurrency axis, benchStringJoin() (+1 more)

### Community 78 - "test_runner.py"
Cohesion: 0.02
Nodes (97): 7 · Coverage, Verified discriminating, by mutating the compiler and rebuilding it, What changed, 5 · The gate, 6 · Reproducers, 5 · The guard, and why the fixture alone is not one, Analysis quality — three recorded gaps closed, 2026-08-06, Level 2 — T2 and scope drop — **DONE, 2026-08-06** (+89 more)

### Community 79 - "M5.1 — allocator evaluation"
Cohesion: 0.09
Nodes (16): Direct mimalloc result, Direct rpmalloc result, Final gate and decision, Initial dynamic-interposition result, M5.1 — allocator evaluation, Question and acceptance rule, Research choice, Rust standing (+8 more)

### Community 80 - "targets/target.psm"
Cohesion: 0.10
Nodes (31): join_path(), umsBuildPlanCreate(), umsBuildProfileValid(), umsPlannedOutput(), UmsLinkKind, FRAMEWORK, LIBRARY, RESPONSE_FILE (+23 more)

### Community 81 - "symbols.psm"
Cohesion: 0.11
Nodes (32): 1.1 What was actually quadratic, 16. Fix superlinear compile time — **DONE, 2026-08-17**, isExternDecl(), isNamedTopLevel(), diag_file_count(), appendStatement(), hasNamedTopLevel(), sameTopLevelName() (+24 more)

### Community 82 - "UmsTokenKind"
Cohesion: 0.14
Nodes (22): umsParse(), impl UmsParser, UmsParser, UmsTokenKind, BOOLEAN, COMMA, EOF, EQUAL (+14 more)

### Community 83 - "algorithms.cpp"
Cohesion: 0.13
Nodes (21): `s_expression_parse`'s arms are not the same program, build_one_sexpr(), build_tree(), eval_sexpr_ast(), fibonacci(), gcd_value(), knapsack(), merge_range() (+13 more)

### Community 84 - "benchRun"
Cohesion: 0.08
Nodes (51): 5 · What moved, 5 · Measured, BenchSExpr, Empty, Num, Op, benchBinarySearch(), benchBuildOneExpr() (+43 more)

### Community 85 - "UmsDiagnostic"
Cohesion: 0.36
Nodes (8): umsDiagnosticAdd(), UmsDiagnostic, umsDependencyScope(), umsLowerDocument(), umsSpanOf(), impl UmsProjectModel, UmsAstDocument, UmsAstStatement

### Community 86 - "kv-adaptive-hash-2026-09-06/ceiling.c"
Cohesion: 0.16
Nodes (24): fm_get_or(), fm_init(), fm_probe(), fm_rehash(), fm_set(), im_get_or(), im_init(), im_probe() (+16 more)

### Community 87 - "compile_ir_to_object"
Cohesion: 0.10
Nodes (30): 0 · The answer, 1 · Why the `llvm-link` merge escaped this and LTO did not, 2 · The part that decides how M1.1 is built: the match must be exact, 3 · It generalises across the corpus, 4 · What this does and does not settle, 5 · Reproducing, 6 · Threats to validity, 7.1 · The mechanism (+22 more)

### Community 88 - "list_release"
Cohesion: 0.13
Nodes (22): 1 · The four, by fixture, 2 · The fifth was not fixed; it was never a gate failure, 3 · What the four have that test_62 does not, 4 · Why this cannot be fixed by adding the missing disposition, 4a · What is inferred rather than measured, 5 · Reproducing, `PRISMIO_INLINE_ELEMS=0` fails four fixtures, and the fifth was never one, list_check_insert_index() (+14 more)

### Community 89 - "ir_intern"
Cohesion: 0.10
Nodes (31): diag_file_module(), find_struct(), ir_caller_can_access_extern(), ir_caller_extern_hidden_level(), ir_extern_decl_record(), ir_file_declares_extern(), ir_file_imports_module(), ir_get_enum_variant() (+23 more)

### Community 90 - "impl I16"
Cohesion: 0.18
Nodes (4): impl I16, main(), impl Square, Square

### Community 91 - "key-before.psm"
Cohesion: 0.10
Nodes (12): keyHashBytes(), keyMixInt(), keyMixWide(), impl Key for Bool, impl Key for Char, impl Key for I64, impl Key for Int, impl Key for String (+4 more)

### Community 92 - "copy.psm"
Cohesion: 0.10
Nodes (15): impl Copy for Bool, impl Copy for Char, impl Copy for Float, impl Copy for I16, impl Copy for I64, impl Copy for I8, impl Copy for Int, impl Copy for Isize (+7 more)

### Community 93 - "test_101_generic_trait_impl.psm"
Cohesion: 0.11
Nodes (18): fail(), main(), markAny(), pairKindAny(), readAny(), impl Marked for Label, impl PairKind for Pair, impl Positive for Int (+10 more)

### Community 94 - "test_103_default_trait_methods.psm"
Cohesion: 0.11
Nodes (16): fail(), greetThrough(), main(), impl Bump for Counter, impl Greet for Cat, impl Greet for Dog, impl ScaleBy for Dog, impl Tagged for Box (+8 more)

### Community 95 - "AIF — Workload Declaration, Cost Model, and Layout Search"
Cohesion: 0.07
Nodes (29): 10.1 The cache model has no associativity and no conflict misses, 10.2 `HandleCost` is a placeholder, 10.3 Profiles age, 10.4.1 A fabricated instance count decides the cache tier, and therefore the layout, 10.4 Static frequency estimation is crude, 10.5 One profile, one target, 10 · Known weaknesses, 1 · The key reframing (+21 more)

### Community 96 - "adversarial.cpp"
Cohesion: 0.11
Nodes (31): adversarial_next(), AdversarialObject, a, b, c, d, allocation_escape(), branch_mispredict() (+23 more)

### Community 97 - "compute.psm"
Cohesion: 0.11
Nodes (26): Plain-data channels copy through the ring, Reproduce, The pointer path's ledger (same day), The result, Tried, and not levers, What was built, BenchBand, benchBandSum() (+18 more)

### Community 98 - "Code Style"
Cohesion: 0.05
Nodes (40): 10. State and cleanup, 11. CLI architecture, 12. FFI and native boundaries, 13. Performance, 14. Testing and validation, 15. Working with agents, 16. A practical review checklist, 17. The governing principles (+32 more)

### Community 99 - "g6_bench.c"
Cohesion: 0.19
Nodes (23): apply_orders(), arena_alloc(), arena_reserve(), arena_reset(), list_free_all(), list_new(), list_push(), main() (+15 more)

### Community 100 - "dbm.psm"
Cohesion: 0.19
Nodes (29): dbmAssign(), dbmAssumeLE(), dbmClose(), dbmCopy(), dbmCopyInto(), dbmForget(), dbmIsBottom(), dbmJoin() (+21 more)

### Community 101 - "The loop range guard was not sound, and the bound it used was one too loose"
Cohesion: 0.07
Nodes (28): 1 · What the loop was paying, 4 · What it measured, 5 · What was rejected, 6 · The regression that was kept, 7 · What is left, One `list_set` was declining a loop of eligible reads, 1 · The bug, 2 · The fix, in three parts (+20 more)

### Community 102 - "time.psm"
Cohesion: 0.16
Nodes (12): main(), time_monotonic_nanos(), time_sleep_nanos(), time_unix_nanos(), sleep(), unixTime(), impl Duration, impl Instant (+4 more)

### Community 103 - "aif_differential.py"
Cohesion: 0.13
Nodes (15): compare(), main(), parse_bracketing(), parse_compiler(), parse_oracle(), parse_threads(), run(), under_neutral_name() (+7 more)

### Community 104 - "di_type_for"
Cohesion: 0.19
Nodes (27): diag_file_count(), diag_file_path(), di_basic(), di_cache(), di_cached(), di_data_element_type(), di_enum_type(), di_field_type_name() (+19 more)

### Community 105 - "test_127_enum_null_variant.psm"
Cohesion: 0.15
Nodes (27): Maybe, None, Some, Reversed, Empty, Value, Three, First (+19 more)

### Community 106 - "Cross-language results — Prismio vs Rust vs Swift"
Cohesion: 0.06
Nodes (39): build_system(), count_alive(), fade(), integrate(), main(), spawn_particle(), Particle, 1 · Handles did not land, and two dimensions depend on them (+31 more)

### Community 107 - "README.md"
Cohesion: 0.10
Nodes (14): Currently Unsupported by Prismio, Deduplicated capabilities, Potential future benchmarks unlocked, Code style, graphify, Runtime surface, Where the project's state lives, A first look (+6 more)

### Community 108 - "prismio_llvm.h"
Cohesion: 0.06
Nodes (12): LLVMOpaqueAttributeRef, LLVMOpaqueBasicBlock, LLVMOpaqueBuilder, LLVMOpaqueContext, LLVMOpaqueError, LLVMOpaqueMetadata, LLVMOpaqueModule, LLVMOpaquePassBuilderOptions (+4 more)

### Community 109 - "adversarial.rs"
Cohesion: 0.12
Nodes (21): adversarial_next(), AdversarialObject, allocation_escape(), branch_mispredict(), consume_adversarial_object(), dead_code_elimination(), dead_kernel(), function_call_overhead() (+13 more)

### Community 110 - "workspace.psm"
Cohesion: 0.17
Nodes (16): impl UmsDiagnostic, get_directory(), join_path(), read_file(), umsBootstrapPrefixLength(), umsHostExecutable(), umsProjectHost(), umsProjectOwnsHost() (+8 more)

### Community 111 - "release_gate.py"
Cohesion: 0.32
Nodes (21): bad(), bootstrap(), check_corpus(), check_cross_target(), check_differential(), check_environment_switch(), check_fixpoint(), check_generations() (+13 more)

### Community 112 - "The cross-language benchmark — current standing and historical session-3 report"
Cohesion: 0.08
Nodes (25): 0 · The one-paragraph answer, 10 · Reproducing, 1 · The full matrix, 2 · Prediction → session-3 measurement → now, per axis, 3 · The claim, stated the way the numbers support it, 4 · `region` on g2: session 3's sharpest negative result is fixed, 5.1 · The residual — the only design number, and it held, 5.2 · Executable size — still a large win, and it grew (+17 more)

### Community 113 - "host.psm"
Cohesion: 0.18
Nodes (24): diag_styled_err(), compiler_check_executable(), compiler_check_host_abi(), compiler_emit_local_toolchain(), compiler_forward_cli(), compiler_host_stamp_matches(), compiler_host_stamp_write(), compiler_promote_executable() (+16 more)

### Community 114 - "TokenType"
Cohesion: 0.08
Nodes (25): TokenType, AMPERSAND, ARITHMETIC_OPERATOR, ARROW, ASSIGNMENT_OPERATOR, BITWISE_OR, BOOL_LITERAL, CHAR_LITERAL (+17 more)

### Community 115 - "test_169_loop_range_proofs.psm"
Cohesion: 0.19
Nodes (25): Slot, At, Empty, ascending(), binderShadow(), bisect(), bisectSum(), check() (+17 more)

### Community 116 - "pop"
Cohesion: 0.11
Nodes (17): A struct crossing a `.plib` read its fields one slot late, Not verified, Results: the subprocess API (2026-09-12 to 2026-09-16), Validation of the final tree, What the design had to work around, 1. `mixed_map_removal` — P0 — done 2026-09-25, 3. `priority_queue` — P2, API to settle before implementation (+9 more)

### Community 117 - "algorithms.rs"
Cohesion: 0.12
Nodes (13): build_one_sexpr(), eval_sexpr_ast(), gcd_lcm(), gcd_value(), merge_range(), mergesort_work(), parse_sexpr_ast(), quick_range() (+5 more)

### Community 118 - "dump.psm"
Cohesion: 0.47
Nodes (9): dumpAstJson(), dumpChain(), dumpFileTable(), dumpNode(), hexDigit(), jsonFieldInt(), jsonFieldStr(), jsonString() (+1 more)

### Community 119 - "run_debug_info_test"
Cohesion: 0.10
Nodes (12): _di_composite(), _di_located_lines(), _di_located_spans(), _di_nodes(), _di_scope_file(), _di_tuple(), _emitted_struct(), _expected_layout() (+4 more)

### Community 120 - "World"
Cohesion: 0.24
Nodes (22): apply_orders(), main(), make_squad(), plan_orders(), recruit(), resolve_combat(), scenario(), Member (+14 more)

### Community 121 - "aifEmitBrackets"
Cohesion: 0.10
Nodes (25): aif_bracket_callee(), aif_bracket_count(), aif_bracket_scope(), aif_bracket_served(), aif_bracketable_region_call_sites(), aif_budget_count(), aif_call_edge_count(), aif_fn_count() (+17 more)

### Community 122 - "test_107_associated_types.psm"
Cohesion: 0.16
Nodes (18): fail(), intContainer(), itemOf(), itemOf(), main(), matches(), pick(), same() (+10 more)

### Community 123 - "test_116_trait_objects.psm"
Cohesion: 0.16
Nodes (14): fail(), forwarded(), main(), measure(), measureScaled(), nameOf(), impl Named for Rect, impl Named for Square (+6 more)

### Community 124 - "World"
Cohesion: 0.25
Nodes (21): world_actor(), world_count_alive(), world_create(), world_damage(), world_set_velocity(), world_spawn(), world_step(), world_transform() (+13 more)

### Community 126 - "preexisting-ownership-repro.psm"
Cohesion: 0.17
Nodes (22): Maybe, None, Some, Reversed, Empty, Value, Three, First (+14 more)

### Community 127 - "AIF — Design Rationale"
Cohesion: 0.10
Nodes (21): AIF — Design Rationale, Arena placement is a cost decision; `region` is a pin on it, Bake the static region, not the heap, C1, C10, C11, C2, C4 (+13 more)

### Community 129 - "TypeKind"
Cohesion: 0.11
Nodes (18): TypeKind, ARRAY, CHAR, DATAELEMENT, DATAVIEW, ENUM, FLOAT, FUNCTION (+10 more)

### Community 130 - "allocPlacedStruct"
Cohesion: 0.20
Nodes (10): ir_alloc_cycle(), ir_alloc_object(), ir_alloc_rc(), ir_alloc_region(), aif_arena_at_node(), aif_cycle_at_node(), aif_rc_at_node(), aif_tier_at_node() (+2 more)

### Community 131 - "aifReportPlacementPin"
Cohesion: 0.14
Nodes (22): aif_fn_bracket_blockers(), aif_fn_call_sites(), aif_fn_calls_in_region(), aif_site_col(), aif_site_derived_tier(), aif_site_file(), aif_site_fn(), aif_site_line() (+14 more)

### Community 132 - "impl Parser"
Cohesion: 0.28
Nodes (6): exit(), parserCreate(), parserDescribe(), startsConstruct(), impl Parser, Parser

### Community 133 - "What is actually left on a `List<Int>` loop: the check, not the header"
Cohesion: 0.22
Nodes (8): 1 · The measured design space, 2 · The recorded plan is worth nothing, 3 · Why the header reloads, and what actually fixes it, 4 · Why no LLVM pass will do this for us, 5 · The design that follows, 6 · If the induction-variable analysis is too much, 7 · Sources, What is actually left on a `List<Int>` loop: the check, not the header

### Community 134 - "hashquality.c"
Cohesion: 0.44
Nodes (9): key_of(), main(), mg(), mi(), mix(), mp(), mr(), ms() (+1 more)

### Community 135 - "shorthash.c"
Cohesion: 0.22
Nodes (20): bench_next_random(), cost_ns(), displacement(), keys_ids(), keys_sort_strings(), main(), mix_a(), mix_b() (+12 more)

### Community 136 - "aif.py"
Cohesion: 0.12
Nodes (11): base_type(), bracket_masks(), elem_key(), elem_spelling_resolved(), main(), measure_masks(), scan(), report() (+3 more)

### Community 137 - "build_curated_module"
Cohesion: 0.09
Nodes (32): 10.1 · Emptying a function body without a `deleteBody`, 10.2 · Checked against the tool it replaces, 10.3 · It is also cheaper, 10.4 · The corpus, re-measured after the port, 10 · The merge moves in process, and the last blocker goes, 8.2 · What landed, 9.1 · Compile time, 9.2 · `--verify`, `--target` and the object cache -- exercised, not assumed (+24 more)

### Community 138 - "test_104_where_clauses.psm"
Cohesion: 0.16
Nodes (15): both(), fail(), heavy(), main(), render(), renderBoth(), impl Boxed for Box, impl Show for Bool (+7 more)

### Community 139 - "test_118_impl_trait.psm"
Cohesion: 0.23
Nodes (16): choose(), describe(), fail(), heavy(), main(), makePoint(), pair(), roundTrip() (+8 more)

### Community 140 - "Single-probe updates and direct entry lookup"
Cohesion: 0.22
Nodes (8): An existing ownership defect exposed by the tests, Compare equal access counts, Controlled measurements, Existing callers also benefit, Memory and correctness, New API, Reproduce, Single-probe updates and direct entry lookup

### Community 141 - "1 · AIF core — genuinely ours"
Cohesion: 0.10
Nodes (21): 1 · AIF core — genuinely ours, 2 · AIF's stake in language features it does not own, 3 · Compiler requirements AIF genuinely has, 4 · Measurement, 5 · Not AIF — recorded, then handed over, 6 · Over-built — defer or cut, A3. Realised context counts *(measurement)*, A4. Arena high-water marks *(measurement)* (+13 more)

### Community 142 - "retain"
Cohesion: 0.07
Nodes (35): 1 · Headline, 2 · The finding: one decision accounts for the entire residue, 3 · What the game corpus showed that the compiler could not, 3a · Handles appear to eliminate T3 in engine code, 4.1 `retain_in(k)` is missing from FFI.md's contract vocabulary, 4.2 The cycle collector has no program that can exercise it, 4 · Two spec gaps the run found, 5 · Secondary measurements (+27 more)

### Community 143 - "4 · Transfer rules"
Cohesion: 0.25
Nodes (8): 4.1 Escape module, 4.2 Aliasing module, 4.3 Thread module, 4.4 Cyclicity module, 4.5 Closure capture, 4.6 Dynamic dispatch, 4.7 Generics and ownership contexts, 4 · Transfer rules

### Community 144 - "test_105_supertraits.psm"
Cohesion: 0.17
Nodes (12): describeAny(), fail(), main(), impl Described for Item, impl Named for Item, impl Reported for Item, impl Sized for Item, Item (+4 more)

### Community 145 - "test_164_array_fields.psm"
Cohesion: 0.19
Nodes (17): Shape, Cells, Empty, corners(), fail(), fourDown(), main(), makeGrid() (+9 more)

### Community 146 - "test_71_nonlexical_extent.psm"
Cohesion: 0.23
Nodes (20): build_a(), build_b0(), build_b(), build_c0(), build_c(), build_d0(), build_d(), build_e() (+12 more)

### Community 148 - "project.psm"
Cohesion: 0.14
Nodes (21): joinPath(), UmsDependencyScope, API, IMPLEMENTATION, TEST_IMPLEMENTATION, UNKNOWN, umsDependencyFind(), umsDependencyScopeName() (+13 more)

### Community 149 - "bench.py"
Cohesion: 0.27
Nodes (6): main(), pct(), PROCESS_MEMORY_COUNTERS, run_once(), suite(), Run

### Community 150 - "run"
Cohesion: 0.12
Nodes (58): 6 · The result, The benchmark matrix, 2026-09-25, The table, Full Suite Comparison (All 34 Workloads), Measurement Results (25-run interleaved comparison), Target Workloads, 2 · What it is worth, which is almost nothing here, Benchmarks (+50 more)

### Community 151 - "test_253_void_closure.psm"
Cohesion: 0.39
Nodes (7): forEach(), add(), each(), fail(), main(), twice(), total

### Community 152 - "find_binding"
Cohesion: 0.10
Nodes (20): find_binding(), ir_binding_owns_slot(), ir_binding_predates_loop(), ir_get_var_data(), ir_get_var_slot(), ir_get_var_type(), ir_has_var_type(), ir_is_list_exclusive() (+12 more)

### Community 153 - "struct_entry"
Cohesion: 0.08
Nodes (39): ir_get_struct_field_count(), ir_get_struct_field_type_at(), ir_is_struct_type_name(), attach_cold(), attach_cold_rc(), get_or_declare_alloc_fn(), get_or_declare_free_fn(), global_named() (+31 more)

### Community 154 - "ownership.psm"
Cohesion: 0.20
Nodes (19): ir_mark_readonly_view(), ir_var_is_inout(), ir_var_is_mutable(), ir_var_is_readonly_view(), semaBindingIsBorrow(), semaCheckExternContracts(), semaCheckMutablePlace(), semaContractArgument() (+11 more)

### Community 155 - "test_232_channel_copies.psm"
Cohesion: 0.26
Nodes (19): closeWakesReceiver(), double(), fail(), keptAcrossIterations(), main(), next(), notesStayBoxed(), produceCount() (+11 more)

### Community 156 - "arena_state"
Cohesion: 0.16
Nodes (22): 4. What the IR diff is, all of it, Per-function mnemonic diff, RC against `build/tbaa3`, 19. Memory budget reporting — **DONE, 2026-08-07**, 7.1 Arena placement, aif_ledger_enter(), aif_ledger_leave(), aif_live_hash(), aif_trace_enabled() (+14 more)

### Community 157 - "memory.cpp"
Cohesion: 0.21
Nodes (11): build_memory_tree(), large_buffer_copy(), memory_tree_sum(), MemoryParticle, life, vx, vy, x (+3 more)

### Community 158 - "common.psm"
Cohesion: 0.21
Nodes (15): benchPrintln(), benchPrintln(), benchPrintln(), benchWrite(), BenchBucket, BenchTree, benchAllocationMutation(), benchBuildMemoryTree() (+7 more)

### Community 159 - "neg_195_callable_bound.psm"
Cohesion: 0.39
Nodes (6): Maybe, Just, Nothing, apply(), main(), impl Maybe

### Community 160 - "platform.psm"
Cohesion: 0.13
Nodes (11): Architecture, X86_64, Environment, GNU, Platform, Windows, impl PlatformQuery, PlatformQuery (+3 more)

### Community 161 - "aif_concurrency.psm"
Cohesion: 0.33
Nodes (18): cli_arg(), register_forever(), break_is_absorbed_by_its_loop(), join_on_both_paths(), joined_stays_local(), loop_between_spawn_and_join(), main(), no_task_at_all() (+10 more)

### Community 162 - "debug_info.psm"
Cohesion: 0.18
Nodes (18): Channel, EAST, NORTH, SOUTH, channelOf(), checkpointTotal(), describe(), main() (+10 more)

### Community 163 - "assert"
Cohesion: 0.23
Nodes (11): Language at a glance, exit(), assert(), main(), classify(), main(), checkedSum(), half() (+3 more)

### Community 164 - "test_115_trait_imports.psm"
Cohesion: 0.19
Nodes (11): fail(), greetAny(), main(), impl Greet for Local, Local, decoration(), impl Greet for Host, impl Sized for Host (+3 more)

### Community 165 - "test_92_field_view_provenance.psm"
Cohesion: 0.21
Nodes (18): Count, Absent, Present, Holder, Empty, Full, str_with_capacity(), boxText() (+10 more)

### Community 166 - "test_map_update.psm"
Cohesion: 0.16
Nodes (10): abort(), unexpectedUpdate(), impl Copy for ProbeKey, impl Copy for UpdateKey, impl CountUpdate, impl Key for ProbeKey, impl Key for UpdateKey, CountUpdate (+2 more)

### Community 167 - "Decisions"
Cohesion: 0.11
Nodes (17): A command is manifest data; which names are free is not, Current limitations, Decisions, Generated state is project-local and isolated, Host selection is a stable prefix, Incremental-build extension seam, Module boundaries, Next implementation sequence (+9 more)

### Community 168 - "g5_asset_cache.psm"
Cohesion: 0.32
Nodes (16): acquire(), build_assets(), evict_unused(), load_material(), load_mesh(), load_texture(), main(), make_cache() (+8 more)

### Community 169 - "benchPrint"
Cohesion: 0.23
Nodes (12): main(), phaseLargeBufferCopy(), main(), phaseKeyValueUpdate(), main(), run(), benchPrint(), clock_gettime() (+4 more)

### Community 170 - "Particle"
Cohesion: 0.29
Nodes (7): 1 · Headline, Particle, life, vx, vy, x, y

### Community 171 - "src/main.psm"
Cohesion: 0.04
Nodes (77): 2 · The defect, 3 · The fix, 5.1 g3's 4095 — and the recorded cause was wrong, aifAlignUp(), aifComputeSizes(), aifComputeSizesOf(), aifComputeStructSize(), aifFieldIsInlineExact() (+69 more)

### Community 172 - "E1: the push check belongs in the preheader, and the profile it was said to need does not exist"
Cohesion: 0.29
Nodes (6): 1 · The distinction that was missing, 2 · The g6 test, which is the whole point, 3 · The benchmark sweep, 4 · Why the two targets did not move, which is the finding worth keeping, 5 · What the guard promises, and what it does not, E1: the push check belongs in the preheader, and the profile it was said to need does not exist

### Community 173 - "layout.py"
Cohesion: 0.23
Nodes (11): candidates(), field_align(), field_width(), Layout, main(), min_size(), mu_for(), record_size() (+3 more)

### Community 174 - "AIF — The T4 Cycle Collector"
Cohesion: 0.12
Nodes (17): 10 · What still needs measurement, 1 · What is actually in scope, 2 · The headline result, 3.1 Why trial deletion and not tracing, 3 · Algorithm, 4 · The cyclic-edge restriction, 5 · Object header, 6.1 Trigger (+9 more)

### Community 175 - "next_random"
Cohesion: 0.12
Nodes (12): binary_search_work(), dijkstra_shortest_path(), lz4_compress(), sort_strings(), next_random(), blake3_chunk(), bytecode_interpreter(), monte_carlo() (+4 more)

### Community 176 - "compute.rs"
Cohesion: 0.12
Nodes (6): band_sum(), BenchSphere, fft(), fft_transform(), parallel_reduction(), Particle

### Community 177 - "bits_test"
Cohesion: 0.05
Nodes (55): Not delivered, and why, 1 · What was wrong, 3 · Measured, 4 · The two failures on the way, both instructive, 5 · Known limits, measured or explicitly not, 6 · Timing, M2.1a — recursive releases for self-referential types (fork (a)), 2 · Why (+47 more)

### Community 178 - "11 · Known weaknesses"
Cohesion: 0.29
Nodes (7): 11.1 Field sensitivity is object-insensitive, 11.2 The context set is discovered from facts that are still moving, 11.3 Loops are handled by the lattice, not by a loop analysis, 11.4 There is no interprocedural path sensitivity, 11.5 ~~The `⊤` context is a cliff~~ — resolved in 1.2, 11.6 Everything here assumes whole-program PIR, 11 · Known weaknesses

### Community 179 - "Performance: what is open, and how to measure it"
Cohesion: 0.29
Nodes (7): 1 · For 0.1, 3.1 · Compiler levers, 3.2 · Platform, not performance, 3 · Later, 4 · Closed, with evidence, 5 · How this work is done, Performance: what is open, and how to measure it

### Community 180 - "main"
Cohesion: 0.13
Nodes (18): binarySearch(), isSorted(), reverse(), sort(), main(), fail(), fill(), grow() (+10 more)

### Community 181 - "package.py"
Cohesion: 0.23
Nodes (10): build_plib(), build_plib_ir(), build_runtime_bitcode(), die(), llvm_bin(), llvm_clang(), main(), run() (+2 more)

### Community 182 - "test_100_generic_inherent_impl.psm"
Cohesion: 0.18
Nodes (9): fail(), main(), impl Box, impl Cell, impl Score for Int, Box, Cell, Pair (+1 more)

### Community 183 - "test_240_overload_exactness.psm"
Cohesion: 0.16
Nodes (8): fail(), main(), twice(), impl Dup for Int, impl Dup for T, impl Name for U8, Dup, Name

### Community 184 - "test_70_struct_field_release.psm"
Cohesion: 0.29
Nodes (17): check(), crate_inventory_again(), main(), make_crate(), make_crate_inventory(), make_inventory(), nested_owner_again(), nested_owner() (+9 more)

### Community 185 - "compiler_plib_interface"
Cohesion: 0.38
Nodes (6): compiler_plib_interface(), plib_empty(), plib_read_sections(), read_u32_le(), read_u64_le(), FILE

### Community 186 - "AIF — Measurement and Falsification Plan"
Cohesion: 0.12
Nodes (17): 1 · The methodological point that matters most, 2.1 Definitions, 2.2 The claim under test, 2.3 False sharing from field insensitivity, 2 · Primary metric: tier distribution, 3.1 B1 is a weak headline and should not be the first result, 3.2 Baselines, 3 · Benchmark programs (+9 more)

### Community 187 - "spin_probe.c"
Cohesion: 0.12
Nodes (23): ch_close(), ch_init(), main(), recv(), relax(), s1(), s2(), send() (+15 more)

### Community 189 - "test_map_probe.psm"
Cohesion: 0.43
Nodes (3): impl Copy for CollidingKey, impl Key for CollidingKey, CollidingKey

### Community 190 - "Contributing to Prismio"
Cohesion: 0.06
Nodes (33): Checks, IR, Results: LLVM 22.1.8 to 23.1.1 (2026-09-17), What changed in the code, What the upgrade showed about the toolchain, Before opening a pull request, Building the compiler, Code of Conduct (+25 more)

### Community 191 - "run_module_artifact_test"
Cohesion: 0.33
Nodes (3): plib_sections(), run_module_artifact_test(), run_plib_triple_sections()

### Community 192 - "manifest_writer.psm"
Cohesion: 0.30
Nodes (15): umsManifestAddDependency(), umsManifestAppendDependencyBlock(), umsManifestChildIndent(), umsManifestDependencyBlock(), umsManifestDependencyText(), umsManifestEscape(), umsManifestIndentAt(), umsManifestInsertDependency() (+7 more)

### Community 193 - "test_111_blanket_impls.psm"
Cohesion: 0.19
Nodes (11): fail(), main(), viaBound(), impl Pretty for T, impl Show for Cat, impl Show for Dog, Cat, Dog (+3 more)

### Community 194 - "test_128_enum_null_reserved.psm"
Cohesion: 0.20
Nodes (16): Exposed, Empty, Node, Generic, None, Some, OptionalTree, Empty (+8 more)

### Community 195 - "test_69_task_results.psm"
Cohesion: 0.32
Nodes (16): print(), println(), acknowledge(), check(), count_span(), int_result(), main(), name_span() (+8 more)

### Community 196 - "validation.psm"
Cohesion: 0.17
Nodes (16): umsAbsolutePath(), umsHostIsProjectBuildOutput(), file_exists(), join_path(), umsRunnableScript(), umsSemverIdentifiers(), umsValidLicenseExpression(), umsValidNumericVersion() (+8 more)

### Community 197 - "Model"
Cohesion: 0.13
Nodes (3): ann_leaf_name(), Model, Scopes

### Community 198 - "C code style"
Cohesion: 0.14
Nodes (13): A constant shared across the seam has one spelling everywhere, A returned `String` must be freeable on every path, Allocations returned to Prismio go through `rt_base_alloc`, Before you commit, C code style, Comments, `extern fn` names are the ABI, Files and modules (+5 more)

### Community 199 - "decl_entry"
Cohesion: 0.14
Nodes (14): add_binding(), decl_entry(), guard_safe_entry(), hash_str(), ir_decl_at(), ir_decl_count(), ir_get_fn_return_type(), ir_index_decl() (+6 more)

### Community 200 - "rt_base_alloc"
Cohesion: 0.13
Nodes (17): 11.2 · What the corpus actually still called, and the false lead, 11.3 · The answer: outline the growth path, 11.4 · Measured, through the driver, 11.5 · The split is invisible with the feature off, 11 · M1.3 — the deeper form, decided by measurement, arena_alloc(), arena_alloc_at(), arena_alloc_slot() (+9 more)

### Community 201 - "run_bootstrap_cache_key_test"
Cohesion: 0.33
Nodes (4): 3.0 What a small build is now made of, 3.1 The compiler's own self-build, 3 · Cold and incremental, run_bootstrap_cache_key_test()

### Community 202 - "Counted scalar fills and struct-list initialization"
Cohesion: 0.33
Nodes (5): Counted scalar fills and struct-list initialization, Interpretation and remaining work, Mechanisms, Reproduction and evidence, Research grounding

### Community 203 - "M4.3a — explicit DataView conversion boundary"
Cohesion: 0.33
Nodes (5): Boundary microbenchmark, Correctness and reproducibility, M4.3a — explicit DataView conversion boundary, Standard milestone benchmark, What landed

### Community 204 - ".toString"
Cohesion: 0.25
Nodes (13): fail(), find(), label(), lengthOf(), main(), make(), named(), spelled() (+5 more)

### Community 205 - "aif_tiers.psm"
Cohesion: 0.27
Nodes (15): cli_arg(), str_concat(), tree_root(), main(), tier_array_elements(), tier_four_cyclic(), tier_one_dropped(), tier_one_string() (+7 more)

### Community 206 - "test_108_trait_method_namespaces.psm"
Cohesion: 0.26
Nodes (10): fail(), loudly(), main(), impl Loud for Dog, impl Loud for Robot, impl Soft for Dog, Dog, Robot (+2 more)

### Community 207 - "test_109_trait_ownership.psm"
Cohesion: 0.24
Nodes (9): fail(), main(), impl Consume for Buffer, impl Read for Buffer, impl Update for Buffer, Buffer, Consume, Read (+1 more)

### Community 208 - "test_58_region_serves.psm"
Cohesion: 0.43
Nodes (16): 4. Four tests changed meaning, and why that is the system working, arena_objects(), print(), println(), fail(), main(), make(), make_out() (+8 more)

### Community 209 - "Profile"
Cohesion: 0.18
Nodes (4): Profile, walk(), find_gets(), Traversal

### Community 210 - "PIR — Prism Semantic IR"
Cohesion: 0.14
Nodes (16): 1 · Why bodies must ship, 2.1 Not LLVM IR, 2 · Content model, 3 · Deterministic emission, 4 · Merging, 5.1 Sealed surfaces SHALL publish ownership contracts, 5 · Sealed functions, 6.1 Format versioning (+8 more)

### Community 211 - "tokenization"
Cohesion: 0.10
Nodes (24): 2 · What it measured, 3 · The bug that made a correct analysis measure 1.29x slower, 4 · Two predictions from the C model, and how they held, 5 · What was rejected, 6 · Where the remaining gap actually is, 7 · The bug that hid all of this, 8 · What is left, 9 · The benchmark was fixed, and what that is worth on its own (+16 more)

### Community 212 - "memory.rs"
Cohesion: 0.19
Nodes (5): build_memory_tree(), memory_tree_sum(), MemoryParticle, recursive_tree_rebuild(), tree_add()

### Community 213 - "aif_manifest_diff.py"
Cohesion: 0.31
Nodes (4): explain(), main(), parse(), Record

### Community 214 - "M4.1 — first-class `Slice<T>`"
Cohesion: 0.33
Nodes (5): Discriminating gates, M4.1 — first-class `Slice<T>`, Ownership result, Surface and representation, Verification and measurement

### Community 215 - "lexCheckIdentifierSecurity"
Cohesion: 0.17
Nodes (16): diag_file_content(), diag_warning_at_code(), identifierIndex(), identifierWarnConfusable(), identifierWarnRestricted(), lexCheckIdentifierSecurity(), confusablePrototype(), identifierRangeRow() (+8 more)

### Community 216 - "test_165_ranges_repeat_labels.psm"
Cohesion: 0.12
Nodes (17): Iterator, fail(), main(), impl Iterator for Countdown, impl Iterator for Letters, Countdown, Letters, classify() (+9 more)

### Community 217 - "neg_165_array_field_refused.psm"
Cohesion: 0.16
Nodes (13): Shape, Dot, Many, Quad, fromView(), main(), Box, Grid (+5 more)

### Community 218 - "test_132_counted_fill.psm"
Cohesion: 0.27
Nodes (13): boolFill(), checkFill(), fill(), inclusiveFill(), interruptedFill(), main(), nearLimitFill(), observedFill() (+5 more)

### Community 219 - "test_157_shared_container_elements.psm"
Cohesion: 0.26
Nodes (14): Shape, Box, Dot, Tree, Leaf, Node, crossFlat(), crossList() (+6 more)

### Community 220 - "test_170_match_switch.psm"
Cohesion: 0.22
Nodes (14): Dir, East, North, South, West, byName(), byte(), classify() (+6 more)

### Community 221 - "test_47_aif_containers.psm"
Cohesion: 0.32
Nodes (13): build(), build_row(), check(), consumes_returned_container(), forwards(), identity(), main(), nested_containers() (+5 more)

### Community 222 - "test_49_aif_struct_fields.psm"
Cohesion: 0.34
Nodes (14): check(), main(), make_crate(), make_crate_inventory(), make_inventory(), nested_owner(), owned_struct_return(), per_iteration() (+6 more)

### Community 223 - "test_87_traits.psm"
Cohesion: 0.24
Nodes (10): fail(), main(), maxOf(), pickLarger(), sortInPlace(), impl Ord for Int, impl Ord for String, impl Ord for Version (+2 more)

### Community 224 - "check_source_lists.py"
Cohesion: 0.29
Nodes (8): bootstrap_ps1_list(), bootstrap_sh_list(), Failure, main(), manifest_native_sources(), package_runtime_bitcode(), read(), runtime_table()

### Community 225 - "g4_ecs_world.psm"
Cohesion: 0.38
Nodes (13): main(), make_world(), spawn(), system_movement(), system_physics(), system_regen(), system_render(), Health (+5 more)

### Community 226 - ".sites_of"
Cohesion: 0.15
Nodes (5): ffi_arena_cannot_serve(), Site, vs_sites(), vs_union(), vs_view_of()

### Community 227 - "neg_107_impl_trait_return_mismatch.psm"
Cohesion: 0.33
Nodes (7): main(), pick(), impl Show for A, impl Show for B, A, B, Show

### Community 228 - "test_163_array_return.psm"
Cohesion: 0.35
Nodes (9): bytes(), fail(), id(), main(), make(), pair(), total(), impl Grid (+1 more)

### Community 229 - "test_154_extern_globals.psm"
Cohesion: 0.19
Nodes (10): readerArgc(), prismio_argc, main(), main(), prismio_argc, shadowed, fail(), main() (+2 more)

### Community 230 - "test_130_list_alias_scopes.psm"
Cohesion: 0.31
Nodes (13): aliasedReceiver(), check(), digest(), growsUnderneath(), lengthObservedDuringPush(), main(), oneName(), pushBoth() (+5 more)

### Community 231 - "test_177_type_functions.psm"
Cohesion: 0.31
Nodes (8): fail(), main(), impl Box, impl Config, impl Server, Box, Config, Server

### Community 232 - "test_55_workload_profile.psm"
Cohesion: 0.29
Nodes (13): exit(), print(), println(), build(), checksum(), cold(), hot(), main() (+5 more)

### Community 233 - "The relational tier, byte-sized Bool elements, and three gaps read from disassembly"
Cohesion: 0.33
Nodes (5): Findings worth keeping, Numbers (scale 4), Tests, The relational tier, byte-sized Bool elements, and three gaps read from disassembly, What changed

### Community 234 - "command.psm"
Cohesion: 0.26
Nodes (12): UmsCommandStepKind, BUILD, RUN, SHELL, UNKNOWN, umsCommand(), umsCommandArgument(), umsCommandFind() (+4 more)

### Community 235 - "ceiling-knapsack.c"
Cohesion: 0.23
Nodes (15): knap_slow_tail(), main(), now_ns(), v0(), v1(), v2(), v3(), v4() (+7 more)

### Community 236 - "The integer-print leak, and g6's arena"
Cohesion: 0.12
Nodes (15): 1. Every program that printed a number leaked, 2. g6 was not blocked on the obligation the notes said it was, 2b. Shared-body bit on bodies that allocate nothing, 2c. Every `List` in the program shared one element node, 3. The corpus, 5.2 `test_47`'s 6 — correctly deferred, and now for a better reason, 5.3 g4's 1.050× — measurement, not regression, 5. The three items this session left open, taken in the same sitting (+7 more)

### Community 237 - "cost.c"
Cohesion: 0.31
Nodes (11): bench_next_random(), main(), measure(), mix_d(), mix_e(), mix_h(), mix_i(), now_ns() (+3 more)

### Community 238 - "8 · Annotations as axioms and constraints"
Cohesion: 0.33
Nodes (6): 8.1 Seeding and cutting, 8.2 `unique` — verification is complete, 8.3 `region` — verification is sound, and imprecision costs only performance, 8.4 `pin`, 8.5 Verification under budget, 8 · Annotations as axioms and constraints

### Community 239 - "common/target.psm"
Cohesion: 0.25
Nodes (14): ir_target_data_layout(), ir_target_is_explicit(), ir_target_pointer_bits(), ir_target_select(), ir_target_triple(), targetArchCode(), targetCurrent(), targetEnvCode() (+6 more)

### Community 240 - "3 · The tier ladder"
Cohesion: 0.33
Nodes (6): 3 · The tier ladder, T0 — Value / stack, T1 — Region / arena, T2 — Unique owned, T3 — Shared, non-atomic reference counting, T4 — Managed residue

### Community 241 - "main"
Cohesion: 0.31
Nodes (7): filter(), min(), fail(), filter(), main(), impl Parser, Parser

### Community 242 - "test_155_vec_methods.psm"
Cohesion: 0.32
Nodes (11): get(), removeAt(), fail(), ints(), jobs(), main(), points(), strings() (+3 more)

### Community 243 - "5.4 `pin`"
Cohesion: 0.33
Nodes (6): 5.4.1 A proven-false pin is a compile error, 5.4.2 An unproven pin is never an error, 5.4.3 Strictness is opt-in, per value, 5.4.4 The direction limit *(normative)*, 5.4.5 `pin(<region-name>)` — the placement form *(normative)*, 5.4 `pin`

### Community 244 - "test_121_guard_effect_analysis.psm"
Cohesion: 0.36
Nodes (12): bumpIt(), check(), filled(), growIt(), indirectGrow(), main(), plain(), readIt() (+4 more)

### Community 245 - "test_82_generic_layout.psm"
Cohesion: 0.42
Nodes (10): fail(), flatMatches(), genericGet(), genericSet(), instantiateNamedSet(), main(), namedMatches(), singleton() (+2 more)

### Community 246 - "test_184_call_result_ownership.psm"
Cohesion: 0.35
Nodes (12): boxed(), expectedLength(), fail(), joined(), listed(), lookup(), main(), make() (+4 more)

### Community 247 - "test_192_callable_bounds.psm"
Cohesion: 0.29
Nodes (9): Maybe, Just, Nothing, combine(), fail(), half(), main(), twice() (+1 more)

### Community 248 - "test_216_for_push_guard.psm"
Cohesion: 0.31
Nodes (12): appended(), armThenTail(), branches(), digest(), down(), either(), fail(), loneFill() (+4 more)

### Community 249 - "test_42_aif_stack_promotion.psm"
Cohesion: 0.32
Nodes (13): Level 1 — T0 — **DONE, 2026-08-05**, check(), escapes(), loop_local(), main(), mixed(), mutated(), nested_in_array() (+5 more)

### Community 250 - "test_68_optional_returns.psm"
Cohesion: 0.36
Nodes (12): print(), println(), bare_none_binding_still_matches(), bound_absent_is_absent(), bound_result_is_optional(), check(), find(), main() (+4 more)

### Community 251 - "test_99_trait_coherence.psm"
Cohesion: 0.22
Nodes (7): main(), useLeft(), impl Left for Bool, impl Left for Int, impl Right for Int, Left, Right

### Community 252 - "g3_scene_graph.psm"
Cohesion: 0.11
Nodes (28): build_hierarchy(), count_visible(), identity_transform(), link_child(), main(), make_node(), propagate(), unit_bounds() (+20 more)

### Community 253 - "benchmarks.hpp"
Cohesion: 0.13
Nodes (8): large_buffer_copy(), main(), now_ns(), BenchTree, left, right, value, main()

### Community 254 - "Compile time — where it goes, and what it scales like"
Cohesion: 0.29
Nodes (6): 1 · The frontend was quadratic in module size, and is now linear, 2.1 AIF's whole fixed point is 18 ms, 2 · The frontend is 4% of a cold build, 5 · Pricing the per-module split, without building one, 6 · Reproducing, Compile time — where it goes, and what it scales like

### Community 255 - "`Int` width — the decision, and the three measurements that made it"
Cohesion: 0.11
Nodes (15): 1 · What the literature actually claims, 2 · Index width is free. Measured, on both targets., 3 · Making overflow UB buys nothing. Measured, on real Prismio programs., 4 · Data width costs 1.33×. Measured, in Prismio., 5 · The cost, stated plainly, 6 · Verdict, 7 · Re-examined 2026-09-24: the whole benchmark suite, 8 · Adaptive width: `Int` means 64 bits, AIF stores it narrow (2026-09-24) (+7 more)

### Community 256 - "Loop versioning exposes Prismio's flat-list fast path"
Cohesion: 0.20
Nodes (9): Cost, Experiments rejected during this investigation, Gate, Loop versioning exposes Prismio's flat-list fast path, Research-directed next order, Seven-program A/B, The remaining branch, What changed in machine code (+1 more)

### Community 257 - "test_73_recursive_release.psm"
Cohesion: 0.40
Nodes (9): Tree, Leaf, Node, depth(), fail(), main(), makeDeep(), makeTree() (+1 more)

### Community 258 - "M4.4 — generic/container layout specialization"
Cohesion: 0.40
Nodes (4): Exit, M4.4 — generic/container layout specialization, Performance control, Question

### Community 259 - "AIF — The Target Workload"
Cohesion: 0.17
Nodes (12): 0.1 · Engine and game remain two workloads, 0 · The actual stack, 1 · The two halves, 2.1 The annotations belong to the engine layer, 2.2 T3 lives in the engine, T0–T2 in the game, 2.3 The engine/game boundary is where whole-program analysis must hold, 2.4 The manifest becomes a contract between teams, 2.5 Optimisation level has to be **per module**, not per build (+4 more)

### Community 260 - "AIF — Adaptive Inference Framework"
Cohesion: 0.12
Nodes (16): 0 · Conformance language, 10.1 FFI, 10.2 Library distribution, 10 · Boundaries, 12 · What this model gives up *(informative)*, 1.1 What the invariant does not cover, 1 · The invariant, 2.1 Allocation site (+8 more)

### Community 261 - "Channels: what 0.1 needs, and the production design after it"
Cohesion: 0.06
Nodes (38): The measurement, The remaining tuned-g9 gap is not the channel topology, Two hypotheses, both refuted, What the handoff expected, What this leaves, Why the proposed slice cannot close it either, 2 · Why the ordinary release point is wrong here, A data race in `--verify` itself (+30 more)

### Community 262 - "6 · Ownership contexts"
Cohesion: 0.40
Nodes (5): 6.1 What a context is, 6.2 Context ordering, 6.3 Discovery (demand-driven), 6.4 The context cap, 6 · Ownership contexts

### Community 263 - "4 · Tier derivation"
Cohesion: 0.40
Nodes (5): 4.1 Inputs, 4.2 The derivation function, 4.3 Monotonicity (normative property), 4.4 Cost model constants *(informative)*, 4 · Tier derivation

### Community 264 - "neg_65_generic_trait_impl_bound.psm"
Cohesion: 0.24
Nodes (7): main(), readAny(), impl Positive for Int, impl Readable for Box, Box, Positive, Readable

### Community 265 - "neg_84_transitive_supertrait.psm"
Cohesion: 0.23
Nodes (5): impl Described for String, impl Reported for String, Described, Named, Reported

### Community 266 - "test_148_struct_index.psm"
Cohesion: 0.24
Nodes (8): fail(), main(), impl Letters, impl Squares, Holder, Letters, Squares, held

### Community 267 - "test_167_frame_struct_fields.psm"
Cohesion: 0.39
Nodes (11): assignedField(), emptyLiteralField(), fail(), inALoop(), literalFields(), main(), makeJob(), namedFields() (+3 more)

### Community 268 - "test_238_scalar_optionals.psm"
Cohesion: 0.26
Nodes (11): Color, Blue, Green, Red, describe(), fail(), firstOr(), half() (+3 more)

### Community 269 - "test_66_payload_enums.psm"
Cohesion: 0.26
Nodes (11): Color, Green, Red, Shape, Circle, Dot, Rect, area() (+3 more)

### Community 270 - "test_86_impl_blocks.psm"
Cohesion: 0.47
Nodes (4): fail(), main(), impl Point, Point

### Community 271 - "stdio"
Cohesion: 0.09
Nodes (29): arena_alloc(), arena_reserve(), arena_reset(), build_scene(), cull(), list_init(), list_push(), main() (+21 more)

### Community 272 - "float_builtins.psm"
Cohesion: 0.70
Nodes (4): floatBuiltinArity(), floatBuiltinOp(), floatBuiltinPrefix(), floatBuiltinSymbol()

### Community 273 - "layout_repr.c"
Cohesion: 0.31
Nodes (8): now_ms(), run_boxed_aos(), run_boxed_split(), run_chunked_inline(), run_chunked_split(), run_inline_aos(), run_inline_split(), run_soa()

### Community 274 - "compile_bench.py"
Cohesion: 0.25
Nodes (5): build(), copy_project(), main(), scenario(), touch()

### Community 275 - "`key_value_update`: the hash was the cost, and four other things were not"
Cohesion: 0.22
Nodes (8): 1 · The design was already at the C ceiling, 3 · What it is: a scrambling hash throws away locality, 4 · The fold, and why it is not just the identity, 5 · So the table checks its own hash, 7 · Verification, 8 · For the next agent, `key_value_update`: the hash was the cost, and four other things were not, Reproduce

### Community 276 - "test_62_split_release.psm"
Cohesion: 0.61
Nodes (7): build(), cold_sum(), count_ids(), main(), make_body(), step(), Body

### Community 277 - "The 2026-09-30 `--verify` sweep"
Cohesion: 0.04
Nodes (100): G-001 — `aif_rc` asserts a proxy that no longer tracks its property, Measured, 2 · Four things that are not the cost, Internal linkage changes inlining, both ways, Boxed `List` replacement ownership, Discriminator, Gates, Why an exclusive operation (+92 more)

### Community 278 - "AIF Evidence"
Cohesion: 0.50
Nodes (4): AIF Evidence, Before quoting any number, Judgement, Projected, not measured

### Community 279 - "io.rs"
Cohesion: 0.27
Nodes (9): alpha(), base64_codec(), byte_sum(), csv_parse(), digit(), file_read(), file_write(), space() (+1 more)

### Community 280 - "Debugging Prismio programs"
Cohesion: 0.18
Nodes (10): Debugging Prismio programs, Part 1 — `-g`, Part 2 — where the memory went, and why, See also, The storage plan — where each site went, `--verify` — did the inference hold?, What `-g` will not tell you, and why, Which tool answers which question (+2 more)

### Community 281 - "install.sh"
Cohesion: 0.33
Nodes (8): banner(), error(), fatal(), fetch(), info(), install.sh script, success(), update_profile()

### Community 282 - "namelist_contains"
Cohesion: 0.25
Nodes (10): ir_declare_named_type(), ir_is_borrowed(), ir_is_global_name(), ir_is_moved(), ir_mark_borrowed(), ir_mark_moved(), ir_named_type_kind(), ir_register_global_name() (+2 more)

### Community 283 - "neg_66_overlapping_generic_trait_impl.psm"
Cohesion: 0.24
Nodes (5): impl Positive for Int, impl Readable for Box, Box, Positive, Readable

### Community 284 - "neg_93_ambiguous_trait_method.psm"
Cohesion: 0.27
Nodes (6): main(), impl Loud for Dog, impl Soft for Dog, Dog, Loud, Soft

### Community 285 - "neg_94_wrong_trait_qualifier.psm"
Cohesion: 0.29
Nodes (6): main(), impl Loud for Dog, impl Soft for Dog, Dog, Loud, Soft

### Community 286 - "test_05_enums.psm"
Cohesion: 0.20
Nodes (10): Color, Blue, Green, Red, ExitCode, Ok, ParseError, RuntimeError (+2 more)

### Community 287 - "test_64_generics.psm"
Cohesion: 0.15
Nodes (15): fail(), main(), impl Bounded for Dial, impl Bounded for Gauge, Dial, Gauge, Bounded, boxUp() (+7 more)

### Community 288 - "test_126_push_predication.psm"
Cohesion: 0.38
Nodes (10): check(), digest(), fillBreak(), fillExact(), fillGrowing(), fillOneShort(), fillPair(), fillSparse() (+2 more)

### Community 289 - "test_129_enum_null_ownership.psm"
Cohesion: 0.29
Nodes (10): OwnedTree, Empty, Node, SharedEmpty, Empty, Node, build(), isEmpty() (+2 more)

### Community 290 - "test_179_proved_index_nsw.psm"
Cohesion: 0.38
Nodes (10): ascending(), check(), knapsack(), knapsackLet(), lookedUp(), main(), offsetBack(), rotated() (+2 more)

### Community 291 - "test_231_cold_functions.psm"
Cohesion: 0.35
Nodes (8): clamp(), cold(), failWith(), lengthOr(), main(), sumSquares(), impl Counter, Counter

### Community 292 - "test_51_optional_refs.psm"
Cohesion: 0.42
Nodes (10): check(), depth_of_chain(), main(), presence_is_visible(), unwrap_is_not_a_move(), zero_first_field_is_still_present(), Carrier, Holder (+2 more)

### Community 293 - "test_52_aif_cycle_collector.psm"
Cohesion: 0.44
Nodes (10): cyc_collect_now(), node_to_ptr(), ptr_to_node(), build_cycle(), check(), collected_when_unreachable(), live_cycle_survives(), main() (+2 more)

### Community 294 - "test_72_reassigned_ownership.psm"
Cohesion: 0.14
Nodes (19): 1 · What this closes, 2 · The defect was documented, deliberate, and had stopped being true, 4 · The two things that cost the most to find, 5 · The fixture, and how it nearly measured nothing, 6 · Timing, Appendix — M2's closing state, 2026-08-23, Delivered, M2.0 — release on reassignment, and the M2 gate restated (+11 more)

### Community 295 - "test_74_reinit_assignment.psm"
Cohesion: 0.33
Nodes (11): What moved, Tree, Leaf, Node, build(), consumeStr(), fail(), main() (+3 more)

### Community 296 - "A payload-free enum variant allocated uninitialised memory"
Cohesion: 0.50
Nodes (4): 1 · What the matrix saw, and what this host did not, 4 · Before / after, 5 · What to check next, A payload-free enum variant allocated uninitialised memory

### Community 297 - "AIF — Evaluation as a General-Purpose Memory Model"
Cohesion: 0.20
Nodes (10): 1 · The finding that should drive planning, 2 · What holds up as general-purpose, 3 · Where the spec is over-fitted — the 80/20 budget rule, 4 · Regions generalise better than layout, and are under-emphasised, 5 · The biggest hole: closures, 6 · PIR is a heavier liability for general-purpose than for games, 7 · Honest scorecard, 8 · What I would change (+2 more)

### Community 298 - "test_63_placement_pin.psm"
Cohesion: 0.61
Nodes (7): arena_objects(), bracketed_make(), bracketed_pin(), fail(), lexical_pin(), main(), Cmd

### Community 299 - "Binary size and compile time against C++ and Rust (2026-09-28)"
Cohesion: 0.12
Nodes (14): A bug worth remembering, Binary size and compile time against C++ and Rust (2026-09-28), Second round, Verification, Where it stands, Where it stood, delete_function_body(), emit_one_partition() (+6 more)

### Community 300 - "6 · The tier manifest"
Cohesion: 0.50
Nodes (4): 6.1 Purpose, 6.2 Format, 6.3 Diff semantics, 6 · The tier manifest

### Community 301 - "run_forced_layout_test"
Cohesion: 0.12
Nodes (12): Inlining the flat push: rejected, and why the obvious gate does not save it, What was kept, What would make it viable, Where it went wrong, and the gate that did not work, Why it was rejected, Host noise, for whoever measures next, `list_new` allocates nothing until the first push, The defect (+4 more)

### Community 302 - "forDirection"
Cohesion: 0.50
Nodes (4): forDirection(), forIntLiteralValue(), forIsIntLiteral(), forIsLength()

### Community 304 - "maphash.psm"
Cohesion: 0.40
Nodes (9): clock_gettime(), write(), distinctKeys(), main(), nextRandom(), now(), say(), vocabulary() (+1 more)

### Community 305 - "AIF — Adaptive Inference Framework"
Cohesion: 0.22
Nodes (9): AIF — Adaptive Inference Framework, Conformance is graded, Contents, Running the prototype, Start here, Status, The model in one screen, Two things to know before extending this (+1 more)

### Community 306 - "8.4 Views — slices and element references"
Cohesion: 0.20
Nodes (10): 8.1 Handles, 8.2 The compiler owns layout, 8.3 The static region, 8.4 Views — slices and element references, 8 · Representation, Cost, stated plainly, Element references are views too — the deep consequence, Invalidation, without a borrow checker (+2 more)

### Community 309 - "test_181_std_math.psm"
Cohesion: 0.26
Nodes (8): 3 · Cost, checkBool(), checkInt(), main(), near(), same(), sumOfRoots(), sumOfRootsInline()

### Community 310 - "test_193_map_methods.psm"
Cohesion: 0.36
Nodes (6): fail(), keyName(), main(), impl Copy for Clash, impl Key for Clash, Clash

### Community 311 - "test_48_aif_shared_elements.psm"
Cohesion: 0.49
Nodes (9): borrow_into_temp(), check(), main(), overwrite_releases(), shared_between_containers(), spread(), survives_first_release(), two_hops() (+1 more)

### Community 312 - "test_56_list_capacity.psm"
Cohesion: 0.53
Nodes (9): print(), println(), computed_hint(), exact_fit(), fail(), grows_past_the_hint(), main(), zero_hint_is_clamped() (+1 more)

### Community 313 - "test_57_pin_tiers.psm"
Cohesion: 0.53
Nodes (9): print(), println(), boxed_elements(), counted_but_uncounted(), counted_elements(), deliberate_pessimisation(), fail(), main() (+1 more)

### Community 314 - "test_59_bracket_summary.psm"
Cohesion: 0.44
Nodes (9): print(), println(), bracketable(), drops(), fail(), main(), middle(), stores_param() (+1 more)

### Community 315 - "test_84_task_release.psm"
Cohesion: 0.38
Nodes (11): 4 · Defect 1 — the task handle had no owner. Fixed., print(), println(), check(), copied_handle(), join_inside_a_loop(), main(), many_frames() (+3 more)

### Community 316 - "test_96_channels.psm"
Cohesion: 0.49
Nodes (9): capacity_and_length(), fail(), main(), pool_round_trip(), serial_round_trip(), step(), worker(), Answer (+1 more)

### Community 318 - "Genuinely-cold compilation"
Cohesion: 0.17
Nodes (9): 1 · What the standing entry actually named, 2.1 One invocation producing both was measured and rejected, 2 · Why the first step only got half of it, 3 · What is left, and why it is left, 4 · Result, 5 · Gates, 6 · Fails open, and the test that stops it failing open quietly, Genuinely-cold compilation (+1 more)

### Community 319 - "Prismio performance benchmarks"
Cohesion: 0.40
Nodes (5): Coverage, Currently Unsupported by Prismio, Infrastructure changes, Prismio performance benchmarks, The three arms must be the same program

### Community 320 - "An `extern` declared `alias` no longer outlives the argument it returns"
Cohesion: 0.33
Nodes (5): 1 · The defect, 4 · The fix, and the line it must not cross, 5 · Result, 6 · Cost: none, and it is provable rather than measured, An `extern` declared `alias` no longer outlives the argument it returns

### Community 322 - "Progress"
Cohesion: 0.14
Nodes (6): Progress, RusagePopen, Checking one file of a program, Current boundary, JSON diagnostics, Prismio IDE protocol

### Community 323 - "aif_ledger_init"
Cohesion: 0.60
Nodes (3): aif_ledger_init(), cyc_lock_init(), BOOL

### Community 324 - "Map probing and full-width key hashing"
Cohesion: 0.22
Nodes (8): Changes that shipped, Maintained benchmark results, Map probing and full-width key hashing, Memory cost, Rejected experiments and research, Remaining critical gaps, Supplemental workloads, Validation and reproduction

### Community 326 - "Debug-mode integer overflow checking"
Cohesion: 0.22
Nodes (9): 1 · The measurement that changed the plan, 2 · What it actually costs on real programs, 3 · Implementation, 4 · A parser defect this found, 6 · What this does not do, 7 · Also in this change: the benchmark clock, 8 · Sources, Debug-mode integer overflow checking (+1 more)

### Community 328 - "A `spawn`ed call's owned temporary argument now has an owner"
Cohesion: 0.22
Nodes (8): 1 · The defect, 3 · The release point, and its licence, 4 · What it costs the benchmark set: nothing, 5 · Two stale claims found on the way, 6 · Reproducing, 7 · Still open in this area, A `spawn`ed call's owned temporary argument now has an owner, prismio_task_release()

### Community 329 - "test_120_min_max_abs.psm"
Cohesion: 0.70
Nodes (4): check(), clampSum(), clampSumInline(), main()

### Community 331 - "5 · Annotations"
Cohesion: 0.22
Nodes (9): 5.0.1 Annotations are assertions, not directives *(normative)*, 5.0 Why exactly these four *(normative rationale)*, 5.1 `unique`, 5.2.1.1 Call-site placement, and which regime it uses *(normative)*, 5.2.1.2 Non-lexical extent, and what it does to the obligations *(normative)*, 5.2.1 A region only reaches allocations in its own function *(normative limitation)*, 5.2 `region { … }`, 5.3 `workload(…)` (+1 more)

### Community 333 - "test_30_diamond_imports.psm"
Cohesion: 0.44
Nodes (5): left_value(), right_value(), shared_double(), fail(), main()

### Community 334 - "neg_57_second_bound_not_satisfied.psm"
Cohesion: 0.36
Nodes (5): activeScore(), main(), impl Scored for Int, Enabled, Scored

### Community 335 - "neg_68_blanket_trait_impl.psm"
Cohesion: 0.31
Nodes (4): impl Named for Dog, impl Named for T, Dog, Named

### Community 336 - "range_direction_probe.psm"
Cohesion: 0.58
Nodes (8): counted(), eitherWay(), endBeforeCount(), lengthUp(), literalDown(), literalUp(), main(), mark()

### Community 337 - "test_123_loop_range_guard_wrap.psm"
Cohesion: 0.53
Nodes (8): check(), filled(), main(), runAwayDown(), runAwayUp(), strideTwo(), wrapDown(), wrapUp()

### Community 338 - "test_144_sort_inline_elements.psm"
Cohesion: 0.42
Nodes (8): fail(), freshSeen(), main(), rnd(), Named, Pt, Small, Wide

### Community 339 - "test_15_compiler_sim.psm"
Cohesion: 0.36
Nodes (8): compile(), create_token(), fail(), main(), parse(), tokenize(), Parser, Token

### Community 340 - "test_166_for_each_collections.psm"
Cohesion: 0.36
Nodes (6): countdown(), fail(), main(), impl Iterator for Countdown, Countdown, Shelf

### Community 341 - "test_171_default_values.psm"
Cohesion: 0.42
Nodes (8): fail(), fresh(), made(), main(), zero(), Box, Inner, Outer

### Community 342 - "test_187_properties.psm"
Cohesion: 0.42
Nodes (5): fail(), main(), impl Rect, perimeter(), Rect

### Community 343 - "test_22_match.psm"
Cohesion: 0.33
Nodes (8): Color, Blue, Green, Red, classify(), describe(), fail(), main()

### Community 344 - "test_53_aif_views.psm"
Cohesion: 0.53
Nodes (8): main(), scalar_read_is_not_a_view(), sum_visible(), view_escapes_by_return(), view_escapes_through_a_binding(), view_in_a_callee(), view_stays_local(), Item

### Community 345 - "test_60_bracket_reset.psm"
Cohesion: 0.44
Nodes (8): arena_objects(), print(), println(), main(), make(), served_in_a_region(), touch(), Cmd

### Community 347 - "test_79_slices.psm"
Cohesion: 0.50
Nodes (8): fail(), first(), main(), middle(), pointSum(), Point, Tagged, Window

### Community 348 - "bootstrap.sh"
Cohesion: 0.42
Nodes (7): cache_entry(), die(), green(), hash_stdin(), bootstrap.sh script, resolve_llvm(), step()

### Community 349 - "AIF Corpus"
Cohesion: 0.50
Nodes (4): AIF Corpus, Building, Gaps to fill, Three things the corpus established

### Community 350 - "g2_frame_loop.psm"
Cohesion: 0.54
Nodes (7): build_scene(), cull(), main(), submit(), DrawCmd, Renderable, Stats

### Community 352 - "g2_bench.psm"
Cohesion: 0.54
Nodes (7): build_scene(), cull(), main(), submit(), DrawCmd, Renderable, Stats

### Community 353 - "g7_particles.psm"
Cohesion: 0.61
Nodes (7): alive(), build(), main(), make_particle(), step(), Particle, Vec3

### Community 358 - "noise floor that decided it"
Cohesion: 0.25
Nodes (7): Hoisting the List header out of the loop: what worked, what did not, and the, noise floor that decided it, Note on measuring g5 at all, The finding, What the measurement said, What this leaves for the real fix, What was tried

### Community 360 - "M2.1b — consuming same-tag rebuilds reuse their input block"
Cohesion: 0.25
Nodes (7): Boundary retained, Gates, Ledger result, M2.1b — consuming same-tag rebuilds reuse their input block, Performance result, Semantic fallback guard, Shape accepted

### Community 364 - "vec_push"
Cohesion: 0.06
Nodes (42): 1 · One allocation site, every call's answer, 2 · Pass-throughs, also asked of sites, 3 · A temporary the callee hands a view of back, 4 · Guards the new bindings needed, which user bindings needed already, 6 · Still open, Who owns a call's result: asked of the call, not of its allocation site, Why neither existing fact caught it, 1 · The defect (+34 more)

### Community 366 - ".charAt"
Cohesion: 0.11
Nodes (18): Found while building this, not caused by it, Measurement 1 — the `+` chain had to be flattened, Measurement 2 — a property may not allocate, The cost: 64 claimed global names, The String surface: operators, properties, iteration, Verification, What landed, 2 · The measurement, and the probe that lied (+10 more)

### Community 367 - "sort_strings"
Cohesion: 0.14
Nodes (31): Bugs found on the way, Changes, Method, Results: the string-benchmark gap (2026-09-11), Root causes, Still open, The suite, before and after, Block partitioning in `sort` (+23 more)

### Community 370 - "v0.1 release candidate — the complete local gate"
Cohesion: 0.29
Nodes (6): Five-arm standing, Sanitizers, Timings, v0.1 release candidate — the complete local gate, What is *not* proved here, What the gate ran

### Community 372 - "AIF — The Inference Engine"
Cohesion: 0.25
Nodes (8): 10 · Worked example, 1 · Architecture, 3.1 Nodes, 3.2 Edges, 3.3 Node ordering (normative), 3 · The fact graph, 9 · Incrementality, AIF — The Inference Engine

### Community 374 - "5 · The fixed-point algorithm"
Cohesion: 0.25
Nodes (8): 5.1 Iteration strategy (normative), 5.2 The algorithm, 5.3 The give-up condition — and why you cannot simply stop, 5.4 Determinism (normative), 5.5 Termination, 5.6 Minimal cause, 5.7 Optimisation levels, 5 · The fixed-point algorithm

### Community 375 - "7 · Specialisation strategy and dedup"
Cohesion: 0.25
Nodes (8): 7.0.1 Three strategies, 7.0.2 Dedup still applies, 7.0 The ownership-divergence ratio, 7.1 Layer 1 — the relevant-parameter mask *(pre-instantiation, cheapest, does the most work)*, 7.2 Layer 2 — semantic equivalence *(pre-codegen)*, 7.3 Layer 3 — structural dedup *(post-codegen)*, 7.4 Budget-driven collapse, 7 · Specialisation strategy and dedup

### Community 377 - "suite.rs"
Cohesion: 0.29
Nodes (3): main(), run(), BENCH_MOD

### Community 378 - "ir_jit_run_file"
Cohesion: 0.36
Nodes (5): compiler_pending_arguments(), ir_jit_run_file(), jit_failed(), jit_failed_unresolved(), jit_process_symbols()

### Community 379 - "range_proof_entry"
Cohesion: 0.29
Nodes (7): ir_range_proof_data(), ir_range_proof_mark(), ir_range_proof_marked(), ir_range_proof_of(), range_proof_bucket(), range_proof_entry(), range_proofs_disabled()

### Community 380 - "Releasing Prismio"
Cohesion: 0.29
Nodes (7): 0 · The commit, 1 · The local gate, 2 · The three-platform matrix — **needs authorisation**, 3 · Artifacts and checksums, 4 · Clean-environment smoke test, 5 · Tag and publish — **needs explicit authorisation**, Releasing Prismio

### Community 381 - "Security Policy"
Cohesion: 0.25
Nodes (7): Acknowledgements, Reporting a Vulnerability, Response Timeline, Responsible Disclosure, Scope, Security Policy, Supported Versions

### Community 387 - "neg_101_dyn_self_not_object_safe.psm"
Cohesion: 0.36
Nodes (4): f(), impl Dup for D, D, Dup

### Community 388 - "neg_104_dyn_returned.psm"
Cohesion: 0.39
Nodes (4): make(), impl Show for Dog, Dog, Show

### Community 390 - "neg_241_optional_impl_overlap.psm"
Cohesion: 0.32
Nodes (3): impl Dup for Int, impl Dup for T, Dup

### Community 391 - "neg_45_bound_not_satisfied.psm"
Cohesion: 0.39
Nodes (5): main(), maxOf(), impl Ord for Int, Point, Ord

### Community 392 - "neg_58_second_bound_not_trait.psm"
Cohesion: 0.39
Nodes (5): main(), scoreWith(), impl Scored for Int, Bag, Scored

### Community 393 - "neg_82_missing_supertrait.psm"
Cohesion: 0.32
Nodes (3): impl Described for String, Described, Named

### Community 394 - "neg_91_unknown_projection.psm"
Cohesion: 0.43
Nodes (5): main(), pick(), impl Container for Bag, Bag, Container

### Community 395 - "neg_92_equality_constraint.psm"
Cohesion: 0.43
Nodes (5): intOnly(), main(), impl Container for Sack, Sack, Container

### Community 396 - "test_01_variables.psm"
Cohesion: 0.36
Nodes (7): bump_global(), fail(), main(), test_arithmetic(), x, y, z

### Community 397 - "test_04_structs.psm"
Cohesion: 0.46
Nodes (7): punned_to_ptr(), fail(), main(), Counter, Point, Punned, Vector

### Community 398 - "test_100_reuse_token.psm"
Cohesion: 0.46
Nodes (7): Tree, Leaf, Node, exit(), main(), mapAdd(), rootValue()

### Community 399 - "test_100_string_append_reuse.psm"
Cohesion: 0.46
Nodes (7): contaminated_site(), fail(), formatted_append(), main(), repeated_append(), self_append(), view_append()

### Community 401 - "test_119_loop_range_guard.psm"
Cohesion: 0.57
Nodes (7): check(), filled(), main(), readWrite(), sumDown(), sumDownOffset(), sumUp()

### Community 402 - "test_156_index_store.psm"
Cohesion: 0.54
Nodes (7): arrays(), fail(), main(), strings(), throughParameter(), vectors(), Pt

### Community 403 - "test_188_stdin.psm"
Cohesion: 0.14
Nodes (16): 1 · The reader, io_stdin_has_line(), io_stdin_read_all(), io_stdin_take_line(), impl Iterator for StdinLines, impl Stdin, Stdin, StdinLines (+8 more)

### Community 404 - "test_235_channel_owned_messages.psm"
Cohesion: 0.61
Nodes (7): closedSendsRelease(), fail(), main(), receivedNotesRelease(), receivedVecsRelease(), shortStringsArriveIntact(), Note

### Community 405 - "test_248_enum_is_a_type.psm"
Cohesion: 0.21
Nodes (11): 3.1 Syntax, 3.2 Execution semantics, 3.3 Why not a data file, and why not a declarative pattern description, 3 · `workload` declaration, Color, Blue, Green, Red (+3 more)

### Community 406 - "test_29_overloads.psm"
Cohesion: 0.36
Nodes (5): choose(), combine(), combine(), fail(), main()

### Community 408 - "test_50_scalar_lists.psm"
Cohesion: 0.46
Nodes (7): bools_survive(), check(), float_round_trip(), grows_past_capacity(), main(), overwrite(), sum_ints()

### Community 409 - "test_80_data_view_conversion.psm"
Cohesion: 0.57
Nodes (7): columnCount(), columnsAreReadable(), fail(), main(), mutateColumns(), Pair, Sample

### Community 410 - "A binding that escapes through a callee's return was freed under its caller"
Cohesion: 0.24
Nodes (14): 1 · The defect, 2 · Which escape routes were already guarded, and which was not, 3 · The fix, 4 · Before / after, 6 · Sources, A binding that escapes through a callee's return was freed under its caller, Two things that were measured, not reasoned, band() (+6 more)

### Community 412 - "How to use it"
Cohesion: 0.33
Nodes (5): AIF and memory gap tracker, G-002 — ownership annotations are not part of trait conformance, G-003 — return-position ownership is not part of trait conformance, G-004 — a node field assigned a local String, and a field overwritten while aliased, How to use it

### Community 413 - "A general affine index matcher, built and reverted"
Cohesion: 0.29
Nodes (7): A general affine index matcher, built and reverted, What it measured, What was built, What would actually be needed, Why: a hypothesis, and the two experiments that refuted it, benchKnapsack(), benchMatrixMultiply()

### Community 415 - "main"
Cohesion: 0.10
Nodes (33): 2 · What 0.1 ships, 4 · Limits in 0.1, 5 · For 0.2: needs design first, Collection methods, clone(), concat(), extend(), fill() (+25 more)

### Community 416 - "Null empty variants for boxed recursive enums"
Cohesion: 0.29
Nodes (6): Allocation and validation evidence, Null empty variants for boxed recursive enums, Representation and safety boundaries, Reproduction, Result, Why the pass is restricted to recursive enums

### Community 418 - "AIF — Engine/Game Boundary Results (A2)"
Cohesion: 0.29
Nodes (7): 1 · Result, 2 · The boundary is cheap because the API is handle-based, 3 · Most of the sealing loss is recoverable with contracts, 4 · A prototype bug worth recording, 5 · Compiler bug found: `List<Int>` miscompiles, 6 · What this does not show, AIF — Engine/Game Boundary Results (A2)

### Community 421 - "M4.3c — mutable DataView round trip"
Cohesion: 0.25
Nodes (7): Correctness and closure gates, Is Prismio DataView hand-tuned?, M4.3c — mutable DataView round trip, Mutable g1 layout gate, side by side with Rust, Standard-corpus regression gate, What changed, data_view_column()

### Community 425 - "The generated release loops on its tail self field"
Cohesion: 0.29
Nodes (6): Discriminator, Gates, Lowering, Remaining boundary, Result, The generated release loops on its tail self field

### Community 428 - "AIF Prototype"
Cohesion: 0.29
Nodes (6): AIF Prototype, Approximations, Running, Two bugs found here, both worth remembering, Two roles, What it implements

### Community 430 - "2 · Fact domains"
Cohesion: 0.29
Nodes (7): 2.1 `E` — escape, 2.2 `A` — aliasing, 2.3 `T` — thread affinity, 2.4 `C` — cyclicity, 2.5 `L` — lifetime determinacy *(derived)*, 2.6 The product, 2 · Fact domains

### Community 434 - "Shape"
Cohesion: 0.38
Nodes (6): Shape, Circle, Dot, Rect, area(), main()

### Community 435 - "neg_44_impl_generic.psm"
Cohesion: 0.38
Nodes (3): impl Readable for Box, Box, Readable

### Community 437 - "neg_67_generic_trait_conformance.psm"
Cohesion: 0.43
Nodes (3): impl Choice for Box, Box, Choice

### Community 438 - "neg_69_generic_trait_method_parameter.psm"
Cohesion: 0.38
Nodes (3): impl Valued for Box, Box, Valued

### Community 439 - "neg_72_missing_bound_trait_argument.psm"
Cohesion: 0.43
Nodes (4): main(), requireFrom(), impl From for String, From

### Community 440 - "neg_73_trait_argument_bound_mismatch.psm"
Cohesion: 0.43
Nodes (4): main(), requireFromInt(), impl From for String, From

### Community 444 - "neg_80_where_bound_not_satisfied.psm"
Cohesion: 0.43
Nodes (4): main(), render(), impl Show for Int, Show

### Community 445 - "neg_89_missing_associated_type.psm"
Cohesion: 0.38
Nodes (3): impl Container for Bag, Bag, Container

### Community 446 - "neg_96_trait_inout_not_honoured.psm"
Cohesion: 0.38
Nodes (3): impl Update for Cell, Cell, Update

### Community 447 - "owned_return_depth2.psm"
Cohesion: 0.52
Nodes (6): str_with_capacity(), depthOne(), depthTwo(), main(), pieceDepthOne(), pieceDepthTwo()

### Community 448 - "owned_temporary_argument.psm"
Cohesion: 0.57
Nodes (6): abs(), band(), drive(), main(), simulate(), Band

### Community 449 - "recursive_enum_bindings_probe.psm"
Cohesion: 0.57
Nodes (6): Expr, Leaf, build(), buildMixed(), main(), sum()

### Community 450 - "test_122_loop_local_index_term.psm"
Cohesion: 0.62
Nodes (6): assignedInBody(), check(), filled(), localDecl(), main(), trulyInvariant()

### Community 451 - "test_124_whole_buffer_copy.psm"
Cohesion: 0.52
Nodes (6): check(), copyAll(), copyFrom(), digest(), filled(), main()

### Community 452 - "test_125_stencil_range_guard.psm"
Cohesion: 0.62
Nodes (6): check(), filled(), main(), neverRuns(), shiftedPastEnd(), stencil()

### Community 453 - "test_138_shadowing.psm"
Cohesion: 0.52
Nodes (6): compare(), concat(), fail(), isDigit(), main(), trim()

### Community 454 - "test_13_globals.psm"
Cohesion: 0.38
Nodes (6): fail(), main(), use_globals(), BUFFER_SIZE, global_counter, MAX_TOKENS

### Community 455 - "test_140_string_search.psm"
Cohesion: 0.57
Nodes (6): agrees(), checkAlphabet(), fail(), generate(), main(), naiveIndexOf()

### Community 456 - "test_14_multi_args.psm"
Cohesion: 0.67
Nodes (6): add3(), add4(), add5(), fail(), main(), nested_calls()

### Community 457 - "test_158_sized_arrays.psm"
Cohesion: 0.62
Nodes (6): copies(), fail(), fillThrough(), lengths(), main(), zeroed()

### Community 458 - "test_162_removal_parks_under_view.psm"
Cohesion: 0.67
Nodes (6): count(), early(), kept(), lent(), main(), word()

### Community 459 - "test_19_runtime_split.psm"
Cohesion: 0.52
Nodes (6): command_quote_arg(), executable_directory(), file_exists(), join_path(), fail(), main()

### Community 460 - "test_25_conventions.psm"
Cohesion: 0.67
Nodes (6): bump(), consume(), fail(), main(), peek(), Counter

### Community 461 - "test_38_scoping.psm"
Cohesion: 0.43
Nodes (6): fail(), main(), reads_global(), shadows_param(), counter, label

### Community 462 - "test_61_layout_cost_model.psm"
Cohesion: 0.67
Nodes (6): advance(), build(), main(), make(), settle(), Sample

### Community 464 - "ast.psm"
Cohesion: 0.17
Nodes (14): UmsAstStatementKind, ASSIGNMENT, CALL, UNKNOWN, UmsAstValueKind, ARRAY, BOOLEAN, IDENTIFIER (+6 more)

### Community 471 - "impl Int"
Cohesion: 0.11
Nodes (4): 1 · The lowering, 4 · Not done, std.math: Float's functions, and the three Float codegen bugs under them, impl Int

### Community 472 - "MEM-035: the stencil's offsets were never the problem — its condition was"
Cohesion: 0.33
Nodes (6): 1 · What the spec said, and what was actually there, 2 · The fix, 3 · Measured, 4 · A measurement that had to be thrown away first, MEM-035: the stencil's offsets were never the problem — its condition was, benchConvolution()

### Community 480 - "1. Architecture"
Cohesion: 0.33
Nodes (6): 1. Architecture, Do not place code in the nearest convenient file, Do not split into meaningless fragments, File size is a signal, not a law, Keep subsystem boundaries explicit, Modules own responsibilities

### Community 481 - "5. Ownership, handles, and globals"
Cohesion: 0.33
Nodes (6): 5. Ownership, handles, and globals, Globals holding handles need no initializer, Handles are `Ptr`, Strings and structs are affine, Test pointer absence with pointer helpers, The old string-punning invariant is retired

### Community 482 - "8. Comments"
Cohesion: 0.33
Nodes (6): 8. Comments, Bad comments explain, Comment density should be earned, Do not turn source files into the specification, Good comments explain, Preserve subtle bug explanations

### Community 483 - "test_fft_direct.psm"
Cohesion: 0.60
Nodes (5): cos(), sin(), benchFft(), benchFftTransform(), main()

### Community 485 - "neg_109_impl_trait_bound.psm"
Cohesion: 0.53
Nodes (4): main(), make(), NoShow, Show

### Community 486 - "neg_161_index_store_refused.psm"
Cohesion: 0.53
Nodes (4): main(), impl Squares, Cell, Squares

### Community 488 - "Color"
Cohesion: 0.40
Nodes (4): Color, Green, Red, Pen

### Community 489 - "Shape"
Cohesion: 0.47
Nodes (5): Shape, Circle, Dot, f(), main()

### Community 500 - "test_10_expressions.psm"
Cohesion: 0.60
Nodes (5): compare_expression(), eval_expression(), fail(), main(), nested_expressions()

### Community 501 - "test_142_sort_patterns.psm"
Cohesion: 0.73
Nodes (5): checkInts(), fail(), main(), rnd(), shape()

### Community 502 - "test_143_string_compare.psm"
Cohesion: 0.67
Nodes (5): agrees(), fail(), main(), referenceOrder(), sign()

### Community 503 - "test_16_arrays.psm"
Cohesion: 0.60
Nodes (5): array_edges(), array_sum(), fail(), main(), matrix_diagonal()

### Community 504 - "test_174_slice_mut.psm"
Cohesion: 0.60
Nodes (5): fail(), head(), main(), poke(), total()

### Community 505 - "test_217_vec_filled.psm"
Cohesion: 0.60
Nodes (4): fail(), main(), impl Copy for Point, Point

### Community 506 - "test_21_loops.psm"
Cohesion: 0.60
Nodes (5): count_to(), fail(), main(), nested(), skip_evens()

### Community 507 - "test_26_borrow_reuse.psm"
Cohesion: 0.73
Nodes (5): fail(), main(), read1(), read2(), Res

### Community 508 - "test_73_recursive_release_depth.psm"
Cohesion: 0.47
Nodes (5): Chain, End, Link, buildChain(), main()

### Community 509 - "test_88_single_loop_inline.psm"
Cohesion: 0.60
Nodes (5): cold(), crowded_a(), crowded_b(), hot(), main()

### Community 510 - "The G2 / G6 benchmark set"
Cohesion: 0.40
Nodes (4): Fidelity, The G2 / G6 benchmark set, What it found, What the variants are

### Community 513 - "AIF — Cross-Language Comparison Suite"
Cohesion: 0.11
Nodes (24): 1 · The thesis, stated so it can be killed, 2 · Fairness rules, 3 · The suite, 4 · Isolating the memory-model tax, 5 · Where AIF is predicted to lose, 6 · Predicted results, 7 · Reporting, AIF — Cross-Language Comparison Suite (+16 more)

### Community 517 - "build_tree"
Cohesion: 0.50
Nodes (3): build_tree(), tree_sum(), tree_traversal()

### Community 520 - "aif_concurrency_shared.psm"
Cohesion: 0.80
Nodes (4): count_items(), main(), shared_element_crosses(), Item

### Community 521 - "extern_alias_escape.psm"
Cohesion: 0.70
Nodes (4): prismio_expect(), main(), make(), passthru()

### Community 525 - "neg_187_bare_type_function.psm"
Cohesion: 0.70
Nodes (3): main(), impl Config, Config

### Community 526 - "Color"
Cohesion: 0.40
Nodes (3): Color, Green, Red

### Community 527 - "Color"
Cohesion: 0.40
Nodes (3): Color, Green, Red

### Community 528 - "Result"
Cohesion: 0.50
Nodes (4): Result, Err, Ok, main()

### Community 530 - "scoreWith"
Cohesion: 0.70
Nodes (3): main(), scoreWith(), Scored

### Community 534 - "neg_81_where_bound_not_trait.psm"
Cohesion: 0.50
Nodes (3): main(), render(), Show

### Community 535 - "pointer_return_temp.psm"
Cohesion: 0.70
Nodes (4): main(), make(), wrap(), Box

### Community 536 - "recursive_optional_probe.psm"
Cohesion: 0.80
Nodes (4): main(), make(), total(), Node

### Community 537 - "test_02_if_else.psm"
Cohesion: 0.70
Nodes (4): fail(), main(), max(), test_nested_if()

### Community 538 - "test_03_while_loops.psm"
Cohesion: 0.70
Nodes (4): factorial(), fail(), main(), sum_to_n()

### Community 539 - "test_06_recursion.psm"
Cohesion: 0.70
Nodes (4): fail(), fibonacci(), gcd(), main()

### Community 540 - "test_07_booleans.psm"
Cohesion: 0.70
Nodes (4): fail(), is_between(), main(), test_equal()

### Community 541 - "test_08_mutability.psm"
Cohesion: 0.70
Nodes (4): fail(), main(), test_complex_mutation(), test_mutation()

### Community 542 - "test_11_returns.psm"
Cohesion: 0.70
Nodes (4): classify_number(), early_return(), fail(), main()

### Community 543 - "test_149_list_literal.psm"
Cohesion: 0.70
Nodes (4): fail(), main(), total(), Job

### Community 544 - "test_161_removal_releases_now.psm"
Cohesion: 0.70
Nodes (4): churn(), churnWord(), digits(), main()

### Community 545 - "test_18_floats.psm"
Cohesion: 0.70
Nodes (4): blended(), comparisons(), fail(), main()

### Community 546 - "test_206_nested_loop_breaks.psm"
Cohesion: 0.70
Nodes (4): fail(), firstAtLeast(), main(), rounds()

### Community 547 - "test_23_move.psm"
Cohesion: 0.80
Nodes (4): fail(), main(), sum(), Point

### Community 548 - "test_33_unary_operators.psm"
Cohesion: 0.60
Nodes (4): fail(), identity(), main(), neg_global

### Community 550 - "test_41_punned_slot_bytes.psm"
Cohesion: 0.80
Nodes (4): node_to_ptr(), main(), reads_as_empty(), Slot

### Community 551 - "test_93_data_view_from_helper.psm"
Cohesion: 0.80
Nodes (4): advance(), buildRows(), main(), Row

### Community 552 - "test_95_literal_tbaa.psm"
Cohesion: 0.70
Nodes (4): fail(), main(), Assigned, Initialised

### Community 554 - "g9_bands.psm"
Cohesion: 1.00
Nodes (3): main(), simulate(), Band

### Community 555 - "Conversions: the release gate, run on a packaged RC"
Cohesion: 0.50
Nodes (3): Conversions: the release gate, run on a packaged RC, Not covered, Two defects in the gate's own harness

### Community 557 - "aif_loop_bracket.psm"
Cohesion: 0.83
Nodes (3): main(), perIteration(), wholeCall()

### Community 558 - "fixture_slice_escape.psm"
Cohesion: 0.83
Nodes (3): escaping_slice(), main(), Item

### Community 559 - "neg_05_drop_borrow.psm"
Cohesion: 1.00
Nodes (3): leak(), main(), Res

### Community 563 - "neg_160_empty_literal_untyped.psm"
Cohesion: 0.83
Nodes (3): count(), countAny(), main()

### Community 566 - "neg_198_array_type_argument.psm"
Cohesion: 0.83
Nodes (3): boxed(), main(), Box

### Community 567 - "neg_22_push_borrowed_element.psm"
Cohesion: 1.00
Nodes (3): hold(), main(), Item

### Community 568 - "use_it"
Cohesion: 1.00
Nodes (3): main(), use_it(), Wide

### Community 569 - "neg_24_unique_aliased_args.psm"
Cohesion: 1.00
Nodes (3): bump(), main(), Buf

### Community 570 - "neg_25_pin_refuted.psm"
Cohesion: 0.83
Nodes (3): leaks(), main(), Node

### Community 571 - "neg_26_placement_pin_refuted.psm"
Cohesion: 0.83
Nodes (3): main(), make(), Cmd

### Community 573 - "neg_48_bound_not_a_trait.psm"
Cohesion: 1.00
Nodes (3): main(), passthrough(), Bag

### Community 578 - "neg_97_nonterminating_instantiation.psm"
Cohesion: 0.67
Nodes (3): grow(), main(), Box

### Community 579 - "target_cross.psm"
Cohesion: 0.83
Nodes (3): main(), Mixed, Span

### Community 580 - "test_133_string_dispatch.psm"
Cohesion: 0.83
Nodes (3): check(), classify(), main()

### Community 581 - "test_134_print_arguments.psm"
Cohesion: 0.83
Nodes (3): fail(), main(), step()

### Community 582 - "test_139_string_chain_append.psm"
Cohesion: 0.83
Nodes (3): digitsOf(), fail(), main()

### Community 583 - "test_145_list_set_within_list.psm"
Cohesion: 0.83
Nodes (3): fail(), main(), Pt

### Community 584 - "test_159_vec_binding_empty.psm"
Cohesion: 0.83
Nodes (3): fail(), main(), Item

### Community 585 - "test_160_i32_alias.psm"
Cohesion: 0.83
Nodes (3): main(), twice(), Point

### Community 586 - "test_180_descending_ranges.psm"
Cohesion: 0.83
Nodes (3): fail(), main(), trail()

### Community 588 - "test_24_drop.psm"
Cohesion: 0.83
Nodes (3): fail(), main(), Point

### Community 589 - "test_28_list.psm"
Cohesion: 0.83
Nodes (3): fail(), main(), Item

### Community 590 - "test_31_strings_in_control_flow.psm"
Cohesion: 0.83
Nodes (3): fail(), label_for(), main()

### Community 591 - "test_32_sized_int_modulo.psm"
Cohesion: 0.67
Nodes (3): fail(), main(), greeting

### Community 592 - "test_40_annotated_arrays.psm"
Cohesion: 0.83
Nodes (3): exit(), fail(), main()

### Community 593 - "test_53_memory_budget.psm"
Cohesion: 1.00
Nodes (3): main(), use_it(), Wide

### Community 596 - "refresh_seed.sh"
Cohesion: 0.67
Nodes (3): die(), PRISMIO_SEED_IR, refresh_seed.sh script

## Knowledge Gaps
- **1221 isolated node(s):** `Empty`, `Node`, `Value`, `Empty`, `None` (+1216 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2572 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **129 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `verify()` connect `setup_llvm.py` to `AIF — Measurement and Falsification Plan`, `rt_alloc`, `1 · AIF core — genuinely ours`, `AIF — Design Rationale`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Why does `__builtin_string_len()` connect `__builtin_string_len` to `ptr_to_node`, `bridge.psm`, `std/io.psm`, `aifReportPlacementPin`, `TypeInfo`, `impl String`, `imports.psm`, `ASTNode`, `model.psm`, `nodeIsNull`, `compile.psm`, `display.psm`, `rangeEmitConditionBound`, `string.psm`, `report.psm`, `project.psm`, `The 2026-09-30 `--verify` sweep`, `ums_cli.psm`, `unicode.psm`, `ownership.psm`, `module.psm`, `aif_concurrency.psm`, `Option`, `str_with_capacity`, `test_72_reassigned_ownership.psm`, `test_74_reinit_assignment.psm`, `relations.psm`, `scanner.psm`, `maphash.psm`, `aifWalk`, `use_it`, `Which std functions are properties`, `aifCallSites`, `manifest_writer.psm`, `unicode_conformance.psm`, `validation.psm`, `aifEmitManifest`, `test_19_runtime_split.psm`, `rt_alloc`, `aif_tiers.psm`, `targets/target.psm`, `symbols.psm`, `test_53_memory_budget.psm`, `UmsDiagnostic`, `key-before.psm`, `.charAt`, `sort_strings`, `workspace.psm`, `host.psm`, `dump.psm`, ``Int` width — the decision, and the three measurements that made it`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Why does `ASTNode` connect `ASTNode` to `ptr_to_node`, `bridge.psm`, `TypeInfo`, `impl Parser`, `imports.psm`, `model.psm`, `nodeIsNull`, `compile.psm`, `rangeEmitConditionBound`, `report.psm`, `ranges.psm`, `module.psm`, `ownership.psm`, `NodeKind`, `src/main.psm`, `relations.psm`, `forDirection`, `aifEmitManifest`, `symbols.psm`, `dbm.psm`, `dump.psm`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Are the 244 inferred relationships involving `__builtin_string_len()` (e.g. with `keyHashBytes()` and `6 · Verdict`) actually correct?**
  _`__builtin_string_len()` has 244 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Empty`, `Node`, `Value` to the rest of the system?**
  _1221 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ptr_to_node` be split into smaller, more focused modules?**
  _Cohesion score 0.03000582970405679 - nodes in this community are weakly interconnected._
- **Should `bridge.psm` be split into smaller, more focused modules?**
  _Cohesion score 0.015710135129697145 - nodes in this community are weakly interconnected._
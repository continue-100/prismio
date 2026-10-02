# Graph Report - prismio  (2026-10-02)

## Corpus Check
- 927 files · ~1,283,520 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 47 file(s) not represented in the graph (top: .asm 21, (none) 18, .css 3)

## Summary
- 11849 nodes · 31824 edges · 642 communities (506 shown, 136 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 4759 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `876d7ff4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- checker.psm
- bridge.psm
- std/io.psm
- symbols.psm
- aif_support.c
- string.psm
- imports.psm
- decl.psm
- llvm-api-backend.c
- model.psm
- ptr_to_node
- compile.psm
- display.psm
- setup.py
- program_support.c
- context.psm
- Language surface
- strCopyRangeInto
- __builtin_string_len
- lang_runtime.c
- std/vec.psm
- resolve_value
- commands.psm
- test_98_multiple_trait_bounds.psm
- unicode.psm
- build_driver.c
- ranges.psm
- module.psm
- process.psm
- main
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
- field_release_of
- relations.psm
- list_new_with_capacity
- aifWalk
- bracket_place
- scanner.psm
- rt_base_alloc
- nominal_find
- walk.psm
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
- TypeKind
- Architecture direction — what to build next, and what the literature already settled
- .equals
- adversarial.psm
- setup_llvm.py
- build_curated_module
- unicode_conformance.psm
- relVisitAccess
- block_done
- subprocess
- backend_fail
- aifEmitManifest
- BoundedQueue
- arena_census.py
- rt_alloc
- report.psm
- run_command
- An owned call result consumed directly as an argument now has an owner
- targets/target.psm
- ASTNode
- UmsTokenKind
- algorithms.cpp
- algorithms.psm
- UmsDiagnostic
- kv-adaptive-hash-2026-09-06/ceiling.c
- M1.0 — why `-flto` declines the inline
- list_release_element
- ir_intern
- cleanup_files
- key-before.psm
- copy.psm
- test_101_generic_trait_impl.psm
- test_103_default_trait_methods.psm
- AIF — Workload Declaration, Cost Model, and Layout Search
- adversarial.cpp
- benchRun
- Code Style
- g6_bench.c
- fn_may_return_param
- The loop range guard was not sound, and the bound it used was one too loose
- time.psm
- os
- di_type_for
- test_127_enum_null_variant.psm
- g1_particles.psm
- README.md
- prismio_llvm.h
- adversarial.rs
- workspace.psm
- release_gate.py
- The cross-language benchmark — current standing and historical session-3 report
- ums_cli.psm
- TokenType
- test_169_loop_range_proofs.psm
- Process
- algorithms.rs
- dump.psm
- run_debug_info_test
- World
- aifEmitBrackets
- test_107_associated_types.psm
- test_116_trait_objects.psm
- World
- preexisting-ownership-repro.psm
- project.psm
- Engine
- ownership.psm
- Plain-data channels copy through the ring
- test_runner.py
- impl Parser
- src/main.psm
- stdio
- shorthash.c
- aif.py
- re
- test_104_where_clauses.psm
- test_118_impl_trait.psm
- Single-probe updates and direct entry lookup
- 1 · AIF core — genuinely ours
- retain
- AIF — The Inference Engine
- test_105_supertraits.psm
- test_164_array_fields.psm
- test_71_nonlexical_extent.psm
- LiveProgress
- rangeEmitConditionBound
- cyc_enter
- run
- .charAt
- find_binding
- struct_entry
- Cross-language results — Prismio vs Rust vs Swift
- test_232_channel_copies.psm
- arena_state
- aifReportPlacementPin
- common.psm
- neg_195_callable_bound.psm
- Which std functions are properties
- aif_concurrency.psm
- .concat
- assert
- test_115_trait_imports.psm
- test_92_field_view_provenance.psm
- test_map_update.psm
- Decisions
- g5_asset_cache.psm
- Result
- math.psm
- elide_middle
- E1: the push check belongs in the preheader, and the profile it was said to need does not exist
- layout.py
- AIF — The T4 Cycle Collector
- compute.rs
- site_arena_scope
- bits_test
- strLength
- M6 slice 2 — ordinary struct-path TBAA, and the g2 regression it caused
- main
- release.py
- test_100_generic_inherent_impl.psm
- test_240_overload_exactness.psm
- test_70_struct_field_release.psm
- impl I64
- verify
- stdlib
- .solve
- workload.psm
- prismio
- Toolchain layout
- manifest_records
- test_111_blanket_impls.psm
- test_128_enum_null_reserved.psm
- test_69_task_results.psm
- named_struct
- Model
- bench.py
- decl_entry
- The 2026-09-30 `--verify` sweep
- AIF — Gap Analysis
- g2_cull_probe.c
- manifest_writer.psm
- .toString
- aif_tiers.psm
- test_108_trait_method_namespaces.psm
- test_109_trait_ownership.psm
- test_58_region_serves.psm
- Profile
- PIR — Prism Semantic IR
- tokenization
- memory.rs
- The loop range guard: one precondition per loop, and both checks are gone
- memory.cpp
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
- test_113_std_eq_and_display.psm
- neg_107_impl_trait_return_mismatch.psm
- test_163_array_return.psm
- test_154_extern_globals.psm
- test_130_list_alias_scopes.psm
- test_177_type_functions.psm
- LAYOUT 6's candidate space, measured against what this compiler can emit
- test_248_enum_is_a_type.psm
- command.psm
- ceiling-knapsack.c
- benchPrint
- cost.c
- .sites_of
- flow.psm
- test_64_generics.psm
- main
- test_155_vec_methods.psm
- g2_bench.c
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
- Codegen
- test_73_recursive_release.psm
- vg-ceiling-2026-09-06/ceiling.c
- AIF — The Target Workload
- AIF — Adaptive Inference Framework
- Channels: what 0.1 needs, and the production design after it
- 5 · A staged path
- BenchSphere
- neg_65_generic_trait_impl_bound.psm
- neg_84_transitive_supertrait.psm
- test_148_struct_index.psm
- test_167_frame_struct_fields.psm
- test_238_scalar_optionals.psm
- test_66_payload_enums.psm
- test_86_impl_blocks.psm
- g2_bench_arena.c
- test_47_aif_minimal_cause.psm
- layout_repr.c
- relCollectNode
- `key_value_update`: the hash was the cost, and four other things were not
- test_62_split_release.psm
- list_get
- test_72_reassigned_ownership.psm
- io.rs
- Debugging Prismio programs
- install.sh
- namelist_contains
- neg_66_overlapping_generic_trait_impl.psm
- neg_93_ambiguous_trait_method.psm
- neg_94_wrong_trait_qualifier.psm
- test_05_enums.psm
- test_106_associated_constants.psm
- run_corpus_test
- test_129_enum_null_ownership.psm
- test_179_proved_index_nsw.psm
- test_231_cold_functions.psm
- test_51_optional_refs.psm
- test_52_aif_cycle_collector.psm
- join
- test_74_reinit_assignment.psm
- M5.1 — allocator evaluation
- AIF — Evaluation as a General-Purpose Memory Model
- test_63_placement_pin.psm
- LLVMModuleRef
- test_88_map_keys.psm
- `list_new` allocates nothing until the first push
- impl U32
- A payload-free enum variant allocated uninitialised memory
- maphash.psm
- AIF — Adaptive Inference Framework
- AIF — Layout Results (A1)
- M2.0 — release on reassignment, and the M2 gate restated
- 16. A practical review checklist
- test_181_std_math.psm
- test_193_map_methods.psm
- test_48_aif_shared_elements.psm
- test_56_list_capacity.psm
- test_57_pin_tiers.psm
- test_59_bracket_summary.psm
- test_84_task_release.psm
- test_96_channels.psm
- test_94_selective_imports.psm
- Genuinely-cold compilation
- Prismio performance benchmarks
- test_143_string_compare.psm
- 8.4 Views — slices and element references
- 2 · Where it stands
- 11 · Known weaknesses
- Map probing and full-width key hashing
- 15. Working with agents
- Debug-mode integer overflow checking
- A `spawn`ed call's owned temporary argument now has an owner
- test_120_min_max_abs.psm
- 3. Before changing code
- 5 · Annotations
- Security Policy
- 2 · Fact domains
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
- test_253_void_closure.psm
- test_79_slices.psm
- bootstrap.sh
- AIF Corpus
- g2_frame_loop.psm
- get_directory
- g2_bench.psm
- g7_particles.psm
- neg_78_default_body_unknown_call.psm
- test_map_probe.psm
- node_args_find
- Counted scalar fills and struct-list initialization
- noise floor that decided it
- test_30_diamond_imports.psm
- evidence/README.md
- test_212_bidi_escapes.psm
- test_175_variant_from_context.psm
- test_39_typed_arrays.psm
- The relational tier, byte-sized Bool elements, and three gaps read from disassembly
- 7. Functions and control flow
- text.psm
- edit_distance
- 4 · Transfer rules
- 5 · The fixed-point algorithm
- compiler_plib_interface
- neg_95_trait_sink_not_honoured.psm
- 7 · Specialisation strategy and dedup
- aif_ledger_init
- test_35_short_circuit.psm
- owned-key-existing-leak.psm
- neg_20_pin_refuted.psm
- suite.rs
- ir_jit_run_file
- range_proof_entry
- Releasing Prismio
- test_204_unicode_case.psm
- test_245_checked_conversions.psm
- A general affine index matcher, built and reverted
- `key_value_update`: one probe in `mapSet`, and a loop guard that is a net loss
- MEM-035: the stencil's offsets were never the problem — its condition was
- v0.1 release candidate — the complete local gate
- neg_101_dyn_self_not_object_safe.psm
- neg_104_dyn_returned.psm
- impl I8
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
- A field read is a view of the object it was read from
- M4.1 — first-class `Slice<T>`
- test_156_index_store.psm
- test_188_stdin.psm
- test_235_channel_owned_messages.psm
- min/max/abs, and the call that used to cost 1.79x
- test_29_overloads.psm
- 8 · Annotations as axioms and constraints
- test_50_scalar_lists.psm
- test_80_data_view_conversion.psm
- A binding that escapes through a callee's return was freed under its caller
- 3 · The tier ladder
- How to use it
- aifEmitPackingAdvice
- impl Key for PathKey
- `Vec<T>` is used through methods
- Null empty variants for boxed recursive enums
- run_struct_path_tbaa_test
- AIF — Engine/Game Boundary Results (A2)
- 6 · Ownership contexts
- neg_191_property_spelling.psm
- M4.3c — mutable DataView round trip
- test_176_match_diverges.psm
- binder_return_probe.psm
- test_200_unicode_identifiers.psm
- The generated release loops on its tail self field
- run_negative_test
- irCallReleasesTemporaries
- AIF Prototype
- test_147_platform.psm
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
- impl Int
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
- test_10_expressions.psm
- test_142_sort_patterns.psm
- test_16_arrays.psm
- test_174_slice_mut.psm
- test_217_vec_filled.psm
- test_21_loops.psm
- test_26_borrow_reuse.psm
- test_73_recursive_release_depth.psm
- test_88_single_loop_inline.psm
- The G2 / G6 benchmark set
- AIF — Cross-Language Comparison Suite
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
8. `generateCall()` - 138 edges
9. `ptr_null()` - 115 edges
10. `ir_get_temp_name()` - 105 edges

## Surprising Connections (you probably didn't know these)
- `Current limitations` --references--> `release()`  [INFERRED]
  ums/ARCHITECTURE.md → aif/corpus/g5_asset_cache.psm
- `Manifest syntax` --references--> `release()`  [INFERRED]
  ums/README.md → aif/corpus/g5_asset_cache.psm
- `Public API, by phase` --references--> `reserve()`  [INFERRED]
  docs/CHANNELS_PLAN.md → aif/evidence/vg-ceiling-2026-09-06/vgphase.psm
- `5 · What was rejected` --references--> `gcd_lcm()`  [INFERRED]
  aif/evidence/RESULTS-knapsack-flat-set.md → benchmarks/cpp/algorithms.cpp
- `3 · The benchmark sweep` --references--> `tree_traversal()`  [INFERRED]
  aif/evidence/RESULTS-push-predication.md → benchmarks/cpp/algorithms.cpp

## Import Cycles
- None detected.

## Communities (642 total, 136 thin omitted)

### Community 0 - "checker.psm"
Cohesion: 0.04
Nodes (250): The surface, 15. Concurrency / task model — **DONE, 2026-08-19**, 4. Optional / nullable reference fields — **DONE, 2026-08-07; return position 2026-08-19**, nodeIsProperty(), ptr_to_type(), type_to_ptr(), nodeSetType(), typeArray() (+242 more)

### Community 1 - "bridge.psm"
Cohesion: 0.02
Nodes (259): What changed, The AIF oracle, aif_layout_field(), resolveImports(), ir_add_checked(), ir_add_nsw(), ir_alloc_cycle(), ir_alloc_object() (+251 more)

### Community 2 - "std/io.psm"
Cohesion: 0.02
Nodes (123): prismio_rt_eprint_float(), prismio_rt_eprintln_float(), prismio_rt_print_float(), prismio_rt_println_float(), str_with_capacity(), eprint(), eprint(), eprint() (+115 more)

### Community 3 - "symbols.psm"
Cohesion: 0.06
Nodes (55): 1.1 What was actually quadratic, A struct crossing a `.plib` read its fields one slot late, 16. Fix superlinear compile time — **DONE, 2026-08-17**, aifLayoutFixStandardLibrary(), ir_extern_decl_record(), ir_index_decl(), ir_reset_decl_index(), indexModuleDeclarations() (+47 more)

### Community 4 - "aif_support.c"
Cohesion: 0.02
Nodes (69): aif_arena_range_first(), aif_arena_range_last(), aif_auto_arena_at_node(), aif_call_edge(), aif_call_opaque(), aif_check_placement_pins(), aif_con_arg(), aif_con_bind() (+61 more)

### Community 5 - "string.psm"
Cohesion: 0.02
Nodes (86): Verification of the final compiler, semaReadLiteralAs(), str_double_valid(), str_double_value(), str_find_byte_pair(), str_find_byte(), str_find_needle(), str_from_double_fixed() (+78 more)

### Community 6 - "imports.psm"
Cohesion: 0.11
Nodes (37): diag_finish(), compiler_plib_error(), compiler_plib_interface(), current_directory(), executable_directory(), file_exists(), get_directory(), join_path() (+29 more)

### Community 7 - "decl.psm"
Cohesion: 0.05
Nodes (114): ptr_is_null(), nodeList(), nodeListPush(), nodeMarkCold(), nodeMarkProperty(), NodeList, diag_error_at_code(), appendTraitRefTo() (+106 more)

### Community 8 - "llvm-api-backend.c"
Cohesion: 0.04
Nodes (61): assign_partitions(), check_llvm_version(), codegen_partition_count(), codegen_thread_budget(), debug_dispose(), default_target_cpu(), emit_trace_enabled(), emit_trace_ms() (+53 more)

### Community 9 - "model.psm"
Cohesion: 0.03
Nodes (107): aif_argv_begin(), aif_argv_count(), aif_argv_end(), aif_argv_get(), aif_argv_push(), aif_call_edge(), aif_call_opaque(), aif_check_pins() (+99 more)

### Community 10 - "ptr_to_node"
Cohesion: 0.03
Nodes (283): Kept from the attempt, 4 · Guards the new bindings needed, which user bindings needed already, 3 · What it was, quicksort: 1.12x -> 1.02-1.03x of C++, 7 · What is left, measured, Found on the way, What was built, 8 · A binding returned on one path leaked on the others (+275 more)

### Community 11 - "compile.psm"
Cohesion: 0.08
Nodes (46): aif_layout_force_applied(), aif_layout_forced_count(), aif_layout_forced_hot(), aif_layout_forced_type(), diag_add_file(), diag_error_count(), diag_file_content(), diag_progress_begin() (+38 more)

### Community 12 - "display.psm"
Cohesion: 0.03
Nodes (50): impl Display for Bool, impl Display for Char, impl Display for Float, impl Display for I16, impl Display for I64, impl Display for I8, impl Display for Int, impl Display for Isize (+42 more)

### Community 13 - "setup.py"
Cohesion: 0.09
Nodes (33): blocked(), Check, check_disk(), check_git(), check_llvm(), check_network(), check_platform(), check_python() (+25 more)

### Community 14 - "program_support.c"
Cohesion: 0.04
Nodes (47): spawn_and_wait(), prismio_memory_thread_enter(), append_module_name(), current_directory(), directory_exists(), fs_lines_close(), fs_lines_has_line(), fs_lines_open() (+39 more)

### Community 15 - "context.psm"
Cohesion: 0.03
Nodes (67): aif_arena_range_first(), aif_arena_range_last(), aif_arg_copies_view(), aif_auto_arena_at_node(), aif_call_arg_outlives_call(), aif_call_arg_retained(), aif_elem_literal_copies_only(), aif_elem_owner_at_node() (+59 more)

### Community 16 - "Language surface"
Cohesion: 0.07
Nodes (51): 6 · What is left, 11 · A `break` in a nested loop is that loop's, 1 · The tables came from the interpreter, and the interpreter was wrong, 2 · Conformance, against the UCD's own tests, 3 · Representation: readable, after one codegen fix, 5 · Identifiers: UAX #31, 6 · Verification, 9 · Case mapping: a search per scalar was 5.4× Rust (+43 more)

### Community 17 - "strCopyRangeInto"
Cohesion: 0.05
Nodes (22): charIsSpace(), strClone(), strCopyRangeInto(), strInsert(), strIsBlank(), strJoin(), strLines(), strPadCenter() (+14 more)

### Community 18 - "__builtin_string_len"
Cohesion: 0.06
Nodes (68): What was refuted: the flat guard for `loop` and `for`, strAllChars(), strBytes(), strChars(), __builtin_string_len(), main(), fail(), main() (+60 more)

### Community 19 - "lang_runtime.c"
Cohesion: 0.04
Nodes (52): arena_current_slot(), data_view_add_column(), data_view_begin(), data_view_check_index(), data_view_finish(), data_view_release(), data_view_to_list(), list_new() (+44 more)

### Community 20 - "std/vec.psm"
Cohesion: 0.04
Nodes (18): listHeapSort(), listInsertionSort(), listPartialInsertionSort(), listPartitionLeft(), listPartitionRight(), listSiftDown(), listSort2(), listSort3() (+10 more)

### Community 21 - "resolve_value"
Cohesion: 0.07
Nodes (69): array_base(), array_copy_bytes(), array_slot(), coerce_for(), existing_global_of_type(), global_named(), intern_value(), ir_alloca() (+61 more)

### Community 22 - "commands.psm"
Cohesion: 0.12
Nodes (39): compiler_spawn_arg(), compiler_spawn_wait(), compileOptions(), CompileOptions, compiler_program_on_path(), listUmsProjectCommands(), prismioBuiltinCommandList(), prismioBuiltinCommands() (+31 more)

### Community 23 - "test_98_multiple_trait_bounds.psm"
Cohesion: 0.28
Nodes (8): activeScore(), checkedScore(), main(), impl Enabled for Int, impl Scored for Int, Gate, Enabled, Scored

### Community 24 - "unicode.psm"
Cohesion: 0.06
Nodes (56): 4 · std.unicode, before and after, scalarWidth(), strDisplayWidth(), strEqualsNormalized(), strGraphemeCount(), strGraphemes(), strGraphemeWidthAt(), strNormalizeNfc() (+48 more)

### Community 25 - "build_driver.c"
Cohesion: 0.04
Nodes (76): accept_if_exists(), append_joined_argument(), append_quoted_argument(), build_trace_enabled(), clang_identity(), compiler_binary_hash(), compiler_check_executable(), compiler_check_host_abi() (+68 more)

### Community 26 - "ranges.psm"
Cohesion: 0.09
Nodes (60): generateWhileRangeGuard(), rangeApplyUpdate(), rangeBitCount(), rangeBodyDeclares(), rangeCanRelate(), rangeClassify(), rangeClassifyChain(), rangeClearCoefs() (+52 more)

### Community 27 - "module.psm"
Cohesion: 0.03
Nodes (139): nodeIsCold(), ir_is_struct_type_name(), floatBuiltinArity(), floatBuiltinOp(), floatBuiltinPrefix(), floatBuiltinSymbol(), ir_blank_line(), ir_call_indirect_ptr() (+131 more)

### Community 28 - "process.psm"
Cohesion: 0.05
Nodes (45): Conversions: the release gate, run on a packaged RC, Not covered, Two defects in the gate's own harness, main(), StreamMode, Inherit, proc_close(), proc_env_get() (+37 more)

### Community 29 - "main"
Cohesion: 0.05
Nodes (19): 6 · Fails open, and the test that stops it failing open quietly, A constant shared across the seam has one spelling everywhere, find_prismio_exe(), main(), parse_runner_args(), run_bootstrap_cache_key_test(), run_channel_copies_test(), run_curated_closure_test() (+11 more)

### Community 30 - "generate_unicode_tables.py"
Cohesion: 0.07
Nodes (35): array_rows(), case_column(), case_folding(), case_tables(), compositions(), confusables(), data_lines(), decompositions() (+27 more)

### Community 31 - "mapSet"
Cohesion: 0.13
Nodes (44): clock_gettime(), intProbe(), main(), now(), stringProbe(), wideProbe(), Stamp, main() (+36 more)

### Community 32 - "run.py"
Cohesion: 0.05
Nodes (41): The verdict rule (benchmarks/run.py `verdict`, schema 3), build_all(), build_key(), collect_environment(), color_enabled(), command_text(), elimination_benchmarks(), elimination_cell() (+33 more)

### Community 33 - "Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs"
Cohesion: 0.50
Nodes (3): Findings worth keeping, Loop range proofs: multi-counter bounds, guard-certified `nsw`, typed GEPs, Numbers (scale 4)

### Community 34 - "Option"
Cohesion: 0.15
Nodes (12): BENCH_MOD, BenchTree, Option, None, Some, impl Option, fail(), findLiteral() (+4 more)

### Community 35 - "fs.psm"
Cohesion: 0.06
Nodes (59): 4 · The toolchain object cache, 5 · Why `std.input` and not `std.io`, and the workload link, rt_workload_stub(), current_directory(), delete_file(), directory_exists(), executable_directory(), file_exists() (+51 more)

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
Nodes (32): Checklist, mapBucketOfEntry(), mapClear(), mapEmpty(), mapFromEntries(), mapGet(), mapHashOf(), mapIndexOf() (+24 more)

### Community 40 - "Key"
Cohesion: 0.13
Nodes (42): mapGet(), mapGetOr(), mapHas(), mapIndexOf(), mapInitialCapacity(), mapKeyAt(), mapLen(), mapNew() (+34 more)

### Community 41 - "LLVMValueRef"
Cohesion: 0.09
Nodes (36): apply_param_attrs(), attach_cold(), attach_cold_rc(), build_bswap64(), build_fmuladd(), build_three_way(), data_view_tbaa_tag(), debug_clear_location() (+28 more)

### Community 42 - "field_release_of"
Cohesion: 0.07
Nodes (53): 3 · The mechanism, Not delivered, and why, 1 · What was wrong, 2 · The rule that replaced it, 3 · Measured, 4 · The two failures on the way, both instructive, 5 · Known limits, measured or explicitly not, 6 · Timing (+45 more)

### Community 43 - "relations.psm"
Cohesion: 0.10
Nodes (67): dbmAssign(), dbmAssumeLE(), dbmClose(), dbmCopy(), dbmCopyInto(), dbmForget(), dbmGet(), dbmIsBottom() (+59 more)

### Community 44 - "list_new_with_capacity"
Cohesion: 0.11
Nodes (20): Boxed `List` replacement ownership, Discriminator, Gates, Why an exclusive operation, 13. Generic containers — `Map<K,V>`, growable `Vec<T>` — **PARTLY DONE, 2026-08-19**, 17. `Int` ↔ `Float` conversion **[minor]**, 18. Struct size / layout introspection **[minor]**, 1. Affine collections — `String`, `List<T>`, arrays become move-only **[done, 2026-08-07]** (+12 more)

### Community 45 - "aifWalk"
Cohesion: 0.07
Nodes (37): aif_con_at(), aif_con_live_in(), aif_con_return_binding(), aif_con_return(), aif_con_spawn(), aif_con_store(), aif_field_access(), aif_is_struct() (+29 more)

### Community 46 - "bracket_place"
Cohesion: 0.05
Nodes (63): 9 · Call-site placement, landed *(2026-08-16, second session)*, 0. What this session was asked to do, and why it did something else, 1. The census, before, 2. The recorded blocker was a circularity, not a missing obligation, 3. A latent soundness hole, found by turning the feature on, 4. What it buys, measured, 5. Where it does not fire, and why each is correct, 6. Gate (+55 more)

### Community 47 - "scanner.psm"
Cohesion: 0.17
Nodes (50): charCode(), exit(), byteText(), createLexer(), hexDigitValue(), isHexDigit(), isRadixDigit(), isTwoCharOperator() (+42 more)

### Community 48 - "rt_base_alloc"
Cohesion: 0.06
Nodes (32): 11.2 · What the corpus actually still called, and the false lead, 11.3 · The answer: outline the growth path, 11.4 · Measured, through the driver, 11.5 · The split is invisible with the feature off, 11 · M1.3 — the deeper form, decided by measurement, Method, 3 · Throughput, 4 · Reproducing (+24 more)

### Community 49 - "nominal_find"
Cohesion: 0.05
Nodes (50): aif_con_pin_region(), aif_elem_key(), aif_enum_new(), aif_extern_contract(), aif_extern_contract_set(), aif_field_access(), aif_field_has_range(), aif_field_range_bytes() (+42 more)

### Community 50 - "walk.psm"
Cohesion: 0.20
Nodes (17): aif_con_pin(), aif_con_pin_region(), aif_con_unique(), aif_stmt_at(), aifApplyAnnotations(), aifBlockChain(), aifChainEscapesUnjoined(), aifChainJoins() (+9 more)

### Community 51 - "key.psm"
Cohesion: 0.07
Nodes (20): 5 · So the table checks its own hash, keyHashBytes(), keyMixInt(), keyMixWide(), keyStrengthen(), impl Key for Bool, impl Key for Char, impl Key for I64 (+12 more)

### Community 52 - "diagnostics.c"
Cohesion: 0.08
Nodes (43): 10 · Trojan Source and UTS #39, tested, diag_add_file(), diag_detect_color(), diag_digits(), diag_elapsed(), diag_emit(), diag_emit_json(), diag_emit_json_summary() (+35 more)

### Community 53 - "option.psm"
Cohesion: 0.07
Nodes (30): 14. Error handling — tagged unions, `Option` / `Result` — **DONE, 2026-08-19**, optionOr(), resultErrOr(), resultIsErr(), resultIsOk(), resultOr(), findLiteral(), main() (+22 more)

### Community 54 - "test_102_generic_trait_arguments.psm"
Cohesion: 0.08
Nodes (28): impl ScaleBy for String, acceptsWrapped(), crossTag(), fail(), main(), make(), sameTag(), scaleWithBool() (+20 more)

### Community 55 - "main"
Cohesion: 0.13
Nodes (5): impl U16, impl U64, impl U8, fail(), main()

### Community 56 - "ir_symbols.c"
Cohesion: 0.05
Nodes (12): drop_index(), ir_drop_kind(), ir_drop_slot(), ir_drop_type(), ir_loop_break_label_named(), ir_loop_continue_label_named(), ir_loop_drop_floor(), ir_loop_drop_floor_named() (+4 more)

### Community 57 - "alpha.psm"
Cohesion: 0.08
Nodes (27): main(), main(), main(), main(), fail(), main(), main(), main() (+19 more)

### Community 59 - "bits_set"
Cohesion: 0.09
Nodes (48): 1 · One allocation site, every call's answer, aif_oom(), bits_clear(), bits_count_at_least_two(), bits_ensure(), bits_free(), bits_is_empty(), bits_or() (+40 more)

### Community 60 - "Ord"
Cohesion: 0.06
Nodes (28): impl Ord for Char, impl Ord for Float, impl Ord for I16, impl Ord for I64, impl Ord for I8, impl Ord for Int, impl Ord for Isize, impl Ord for String (+20 more)

### Community 61 - "Default"
Cohesion: 0.08
Nodes (23): impl Default for Bool, impl Default for Char, impl Default for Float, impl Default for I16, impl Default for I64, impl Default for I8, impl Default for Int, impl Default for Isize (+15 more)

### Community 62 - "TypeKind"
Cohesion: 0.11
Nodes (18): TypeKind, ARRAY, CHAR, DATAELEMENT, DATAVIEW, ENUM, FLOAT, FUNCTION (+10 more)

### Community 63 - "Architecture direction — what to build next, and what the literature already settled"
Cohesion: 0.17
Nodes (12): 0 · The diagnosis, and the one thing everybody had backwards, 1 · Close the runtime seam — built, with one deployment decision left, 2 · Reuse analysis — useful only where the program has its trigger shape, 3 · Regions: go non-lexical and polymorphic, 4 · Views and slices — bounded views and mutable data views shipped, 5 · The allocator — measured and closed for the current workload, 6 · The ranked plan, 7 · Measured dead ends — do not re-derive these (+4 more)

### Community 64 - ".equals"
Cohesion: 0.10
Nodes (32): 2 · What it was not, 5 · What is still open, 1 · The blocker, as recorded and as measured, aifCallIsSummarised(), aifCompilerBuiltinContract(), aifDeclaredContract(), aifDeclaredReturnIsAlias(), aifDeclaredReturnIsProduce() (+24 more)

### Community 65 - "adversarial.psm"
Cohesion: 0.13
Nodes (25): benchAdversarialNext(), benchAllocationEscape(), benchAosVsSoa(), benchBranchMispredict(), benchConsumeAdversarialObject(), benchDeadCodeElimination(), benchDeadKernel(), benchDependencyChain() (+17 more)

### Community 66 - "setup_llvm.py"
Cohesion: 0.12
Nodes (25): adopt(), build_zstd(), compile_one(), download(), exe(), extract(), is_bitcode(), llvm_config() (+17 more)

### Community 67 - "build_curated_module"
Cohesion: 0.09
Nodes (58): 8.2 · What landed, build_curated_module(), build_trace_ms(), build_trace_stage(), codegen_uses_clang(), compare_dotted_versions(), compile_ir_to_object(), compile_native_sources() (+50 more)

### Community 68 - "unicode_conformance.psm"
Cohesion: 0.11
Nodes (31): 7 · The ASCII regression was the caller's loop, not `toUpper`'s, identifierSkeleton(), semaArticle(), builderPiece(), strFromScalar(), impl StringBuilder, StringBuilder, firstByte() (+23 more)

### Community 69 - "relVisitAccess"
Cohesion: 0.21
Nodes (17): ir_icmp_sge(), ir_icmp_sle(), ir_range_proof_mark(), ir_range_proof_marked(), rangeDataFor(), rangeEmitAccess(), rangeFold(), rangeFoldVar() (+9 more)

### Community 70 - "block_done"
Cohesion: 0.14
Nodes (35): block_done(), block_for(), element_from_memory(), element_memory_type(), element_to_memory(), flat_element_address(), ir_br_numbered(), ir_call_indirect_ptr() (+27 more)

### Community 71 - "subprocess"
Cohesion: 0.04
Nodes (44): build(), copy_project(), main(), scenario(), touch(), digest(), main(), run() (+36 more)

### Community 72 - "backend_fail"
Cohesion: 0.07
Nodes (36): apply_borrow_attrs(), backend_fail(), const_from_text(), grow_table(), ir_array_literal_elem(), ir_br(), ir_call_begin(), ir_call_end() (+28 more)

### Community 73 - "aifEmitManifest"
Cohesion: 0.07
Nodes (30): aif_arena_high_water(), aif_arena_unsized_sites(), aif_layout_best(), aif_layout_cand_bytes(), aif_layout_cand_hot(), aif_layout_cand_ratio(), aif_layout_hot_count(), aif_layout_rank() (+22 more)

### Community 74 - "BoundedQueue"
Cohesion: 0.16
Nodes (7): BoundedQueue, cap_, closed_, mu_, not_empty_, not_full_, queue_

### Community 75 - "arena_census.py"
Cohesion: 0.16
Nodes (8): blockers_for(), main(), manifest_symbols(), programs(), summary_brackets(), main(), programs(), under_neutral_name()

### Community 76 - "rt_alloc"
Cohesion: 0.08
Nodes (35): 2 · The leak, 0 · Why this file exists, 1 · The measurement, 2 · What was wrong: `str_substring` rescans the whole buffer, 3 · The compiler itself, 4 · What did *not* move, and why that is the finding, 5 · What this changes about the ranking, 1 · What was actually true before (+27 more)

### Community 77 - "report.psm"
Cohesion: 0.07
Nodes (65): aif_alias_name(), aif_arena_blockers(), aif_cause_build(), aif_cause_col(), aif_cause_domain_for(), aif_cause_file(), aif_cause_line(), aif_cause_rule() (+57 more)

### Community 78 - "run_command"
Cohesion: 0.05
Nodes (22): emitted_layout_for(), run_aif_human_report_test(), run_aif_loop_bracket_test(), run_aif_minimal_cause_test(), why(), run_aif_test(), run_bracket_summary_test(), bracket_lines() (+14 more)

### Community 79 - "An owned call result consumed directly as an argument now has an owner"
Cohesion: 0.25
Nodes (8): 1 · The defect, 2 · The fix, and the three conditions on it, 3 · Before / after, 4 · The discriminator, 5 · What this does not reach, An owned call result consumed directly as an argument now has an owner, `spawn` is excluded structurally, and that is required, The retention guard that was asked for does not exist and is not needed

### Community 80 - "targets/target.psm"
Cohesion: 0.10
Nodes (31): join_path(), umsBuildPlanCreate(), umsBuildProfileValid(), umsPlannedOutput(), UmsLinkKind, FRAMEWORK, LIBRARY, RESPONSE_FILE (+23 more)

### Community 81 - "ASTNode"
Cohesion: 0.03
Nodes (251): 2 · The defect, 3 · The fix, Two missing edges, and a missing type, 5.1 g3's 4095 — and the recorded cause was wrong, Answer: Prismio chooses after substitution, 3 · How, aifArgTypeAt(), aifAlignUp() (+243 more)

### Community 82 - "UmsTokenKind"
Cohesion: 0.09
Nodes (35): UmsAstStatementKind, ASSIGNMENT, CALL, UNKNOWN, UmsAstValueKind, ARRAY, BOOLEAN, IDENTIFIER (+27 more)

### Community 83 - "algorithms.cpp"
Cohesion: 0.10
Nodes (25): 2 · What it is worth, which is almost nothing here, 3 · Step 2 of the task was not attempted, and why, MEM-033: the cycle collector stops locking when there is nothing to lock against, `s_expression_parse`'s arms are not the same program, build_one_sexpr(), build_tree(), eval_sexpr_ast(), fibonacci() (+17 more)

### Community 84 - "algorithms.psm"
Cohesion: 0.09
Nodes (34): 2 · Pass-throughs, also asked of sites, 3 · A temporary the callee hands a view of back, 5 · What moved, 6 · Still open, Who owns a call's result: asked of the call, not of its allocation site, BenchSExpr, Empty, Num (+26 more)

### Community 85 - "UmsDiagnostic"
Cohesion: 0.36
Nodes (8): umsDiagnosticAdd(), UmsDiagnostic, umsDependencyScope(), umsLowerDocument(), umsSpanOf(), impl UmsProjectModel, UmsAstDocument, UmsAstStatement

### Community 86 - "kv-adaptive-hash-2026-09-06/ceiling.c"
Cohesion: 0.16
Nodes (24): fm_get_or(), fm_init(), fm_probe(), fm_rehash(), fm_set(), im_get_or(), im_init(), im_probe() (+16 more)

### Community 87 - "M1.0 — why `-flto` declines the inline"
Cohesion: 0.08
Nodes (26): 0 · The answer, 10.1 · Emptying a function body without a `deleteBody`, 10.2 · Checked against the tool it replaces, 10.3 · It is also cheaper, 10.4 · The corpus, re-measured after the port, 10 · The merge moves in process, and the last blocker goes, 1 · Why the `llvm-link` merge escaped this and LTO did not, 2 · The part that decides how M1.1 is built: the match must be exact (+18 more)

### Community 88 - "list_release_element"
Cohesion: 0.20
Nodes (15): 1. `mixed_map_removal` — P0 — done 2026-09-25, API to settle before implementation, list_check_insert_index(), list_discard_slot(), list_insert(), list_insert_inline(), list_insert_inline_scalar(), list_insert_str() (+7 more)

### Community 89 - "ir_intern"
Cohesion: 0.10
Nodes (31): diag_file_module(), find_struct(), ir_caller_can_access_extern(), ir_caller_extern_hidden_level(), ir_extern_decl_record(), ir_file_declares_extern(), ir_file_imports_module(), ir_get_enum_variant() (+23 more)

### Community 90 - "cleanup_files"
Cohesion: 0.06
Nodes (16): cleanup_files(), run_aif_drop_emission_test(), run_aif_layout_test(), run_aif_rc_test(), run_aif_stack_slot_test(), run_aif_struct_field_test(), run_aif_view_test(), run_check_command_test() (+8 more)

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
Cohesion: 0.08
Nodes (21): edit_distance: not a code gap, graph_bfs: not a code gap, large_buffer_copy: still 1.14-1.16x, and why, mandelbrot: 1.12x -> 0.99x of C++ (and Rust is 1.25x), quicksort and graph_bfs: what the gap was, 2026-10-01, fail(), greetThrough(), main() (+13 more)

### Community 95 - "AIF — Workload Declaration, Cost Model, and Layout Search"
Cohesion: 0.10
Nodes (20): 10.1 The cache model has no associativity and no conflict misses, 10.2 `HandleCost` is a placeholder, 10.3 Profiles age, 10.4.1 A fabricated instance count decides the cache tier, and therefore the layout, 10.4 Static frequency estimation is crude, 10.5 One profile, one target, 10 · Known weaknesses, 1 · The key reframing (+12 more)

### Community 96 - "adversarial.cpp"
Cohesion: 0.10
Nodes (34): adversarial_next(), AdversarialObject, a, b, c, d, allocation_escape(), aos_vs_soa() (+26 more)

### Community 97 - "benchRun"
Cohesion: 0.10
Nodes (38): 5 · Measured, benchBinarySearch(), benchLz4Compress(), benchPrimeSieve(), benchSortStrings(), benchRandom(), BenchBand, benchBandSum() (+30 more)

### Community 98 - "Code Style"
Cohesion: 0.06
Nodes (31): 10. State and cleanup, 11. CLI architecture, 12. FFI and native boundaries, 13. Performance, 14. Testing and validation, 17. The governing principles, 1. Architecture, 2. Production-code standard (+23 more)

### Community 99 - "g6_bench.c"
Cohesion: 0.19
Nodes (23): apply_orders(), arena_alloc(), arena_reserve(), arena_reset(), list_free_all(), list_new(), list_push(), main() (+15 more)

### Community 100 - "fn_may_return_param"
Cohesion: 0.07
Nodes (34): Why neither existing fact caught it, 1. Every program that printed a number leaked, Measured, What landed, Where it was, 1 · The defect, 2 · Why it did not need a fixed point, 3 · Before / after (+26 more)

### Community 101 - "The loop range guard was not sound, and the bound it used was one too loose"
Cohesion: 0.07
Nodes (29): 1 · What the loop was paying, 4 · What it measured, 5 · What was rejected, 6 · The regression that was kept, 7 · What is left, One `list_set` was declining a loop of eligible reads, 1 · The bug, 2 · The fix, in three parts (+21 more)

### Community 102 - "time.psm"
Cohesion: 0.16
Nodes (12): main(), time_monotonic_nanos(), time_sleep_nanos(), time_unix_nanos(), sleep(), unixTime(), impl Duration, impl Instant (+4 more)

### Community 103 - "os"
Cohesion: 0.10
Nodes (21): compare(), main(), parse_bracketing(), parse_compiler(), parse_oracle(), parse_threads(), run(), under_neutral_name() (+13 more)

### Community 104 - "di_type_for"
Cohesion: 0.20
Nodes (27): diag_file_count(), diag_file_path(), di_basic(), di_cache(), di_cached(), di_data_element_type(), di_enum_type(), di_field_type_name() (+19 more)

### Community 105 - "test_127_enum_null_variant.psm"
Cohesion: 0.15
Nodes (27): Maybe, None, Some, Reversed, Empty, Value, Three, First (+19 more)

### Community 106 - "g1_particles.psm"
Cohesion: 0.31
Nodes (12): build_system(), count_alive(), fade(), integrate(), main(), spawn_particle(), Particle, 2.1 · It was built on 2026-08-17, and the corpus does not reproduce the 0.87× (+4 more)

### Community 107 - "README.md"
Cohesion: 0.08
Nodes (18): 1 · `tools/release_gate.py`, The v0.1 gate and benchmark matrix on the branch head, 2026-09-25, Code style, graphify, Runtime surface, Where the project's state lives, Checking one file of a program, Current boundary (+10 more)

### Community 108 - "prismio_llvm.h"
Cohesion: 0.07
Nodes (12): LLVMOpaqueAttributeRef, LLVMOpaqueBasicBlock, LLVMOpaqueBuilder, LLVMOpaqueContext, LLVMOpaqueError, LLVMOpaqueMetadata, LLVMOpaqueModule, LLVMOpaquePassBuilderOptions (+4 more)

### Community 109 - "adversarial.rs"
Cohesion: 0.12
Nodes (21): adversarial_next(), AdversarialObject, allocation_escape(), branch_mispredict(), consume_adversarial_object(), dead_code_elimination(), dead_kernel(), function_call_overhead() (+13 more)

### Community 110 - "workspace.psm"
Cohesion: 0.15
Nodes (16): impl UmsDiagnostic, get_directory(), join_path(), read_file(), umsBootstrapPrefixLength(), umsHostExecutable(), umsProjectHost(), umsProjectOwnsHost() (+8 more)

### Community 111 - "release_gate.py"
Cohesion: 0.32
Nodes (21): bad(), bootstrap(), check_corpus(), check_cross_target(), check_differential(), check_environment_switch(), check_fixpoint(), check_generations() (+13 more)

### Community 112 - "The cross-language benchmark — current standing and historical session-3 report"
Cohesion: 0.08
Nodes (26): 0 · The one-paragraph answer, 10 · Reproducing, 1 · The full matrix, 2 · Prediction → session-3 measurement → now, per axis, 3 · The claim, stated the way the numbers support it, 4 · `region` on g2: session 3's sharpest negative result is fixed, 5.1 · The residual — the only design number, and it held, 5.2 · Executable size — still a large win, and it grew (+18 more)

### Community 113 - "ums_cli.psm"
Cohesion: 0.09
Nodes (47): diag_styled_err(), compiler_check_executable(), compiler_check_host_abi(), compiler_emit_local_toolchain(), compiler_forward_cli(), compiler_host_stamp_matches(), compiler_host_stamp_write(), compiler_promote_executable() (+39 more)

### Community 114 - "TokenType"
Cohesion: 0.08
Nodes (26): TokenType, AMPERSAND, ARITHMETIC_OPERATOR, ARROW, ASSIGNMENT_OPERATOR, BITWISE_OR, BOOL_LITERAL, CHAR_LITERAL (+18 more)

### Community 115 - "test_169_loop_range_proofs.psm"
Cohesion: 0.19
Nodes (25): Slot, At, Empty, ascending(), binderShadow(), bisect(), bisectSum(), check() (+17 more)

### Community 116 - "Process"
Cohesion: 0.29
Nodes (6): Not verified, Results: the subprocess API (2026-09-12 to 2026-09-16), Two defects the fixture found, Validation of the final tree, What the design had to work around, Process()

### Community 117 - "algorithms.rs"
Cohesion: 0.10
Nodes (16): build_one_sexpr(), build_tree(), eval_sexpr_ast(), gcd_lcm(), gcd_value(), merge_range(), mergesort_work(), parse_sexpr_ast() (+8 more)

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
Cohesion: 0.11
Nodes (24): aif_bracket_callee(), aif_bracket_count(), aif_bracket_scope(), aif_bracket_served(), aif_bracketable_region_call_sites(), aif_budget_count(), aif_call_edge_count(), aif_fn_count() (+16 more)

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

### Community 127 - "project.psm"
Cohesion: 0.14
Nodes (21): joinPath(), UmsDependencyScope, API, IMPLEMENTATION, TEST_IMPLEMENTATION, UNKNOWN, umsDependencyFind(), umsDependencyScopeName() (+13 more)

### Community 129 - "ownership.psm"
Cohesion: 0.09
Nodes (35): 2 · Order of work and status, ir_clear_var_types(), ir_declare_named_type(), ir_reset_fn_return_types(), ir_reset_globals(), ir_reset_named_types(), ir_var_is_inout(), ir_var_is_mutable() (+27 more)

### Community 130 - "Plain-data channels copy through the ring"
Cohesion: 0.22
Nodes (7): Plain-data channels copy through the ring, Reproduce, The pointer path's ledger (same day), Tried, and not levers, chan_bytes_ready(), chan_recv_copy(), chan_send_copy()

### Community 131 - "test_runner.py"
Cohesion: 0.10
Nodes (14): compile_prismio_file(), preserved_project_host(), project_host_lock(), run_byte_loop_vectorise_test(), run_identifier_security_test(), run_overflow_checks_test(), run_program(), run_test() (+6 more)

### Community 132 - "impl Parser"
Cohesion: 0.28
Nodes (6): exit(), parserCreate(), parserDescribe(), startsConstruct(), impl Parser, Parser

### Community 133 - "src/main.psm"
Cohesion: 0.10
Nodes (39): aif_layout_force(), diag_error_code(), diag_print_help(), ir_target_data_layout(), ir_target_is_explicit(), ir_target_pointer_bits(), ir_target_select(), ir_target_triple() (+31 more)

### Community 134 - "stdio"
Cohesion: 0.16
Nodes (9): key_of(), main(), mg(), mi(), mix(), mp(), mr(), ms() (+1 more)

### Community 135 - "shorthash.c"
Cohesion: 0.22
Nodes (20): bench_next_random(), cost_ns(), displacement(), keys_ids(), keys_sort_strings(), main(), mix_a(), mix_b() (+12 more)

### Community 136 - "aif.py"
Cohesion: 0.12
Nodes (11): base_type(), bracket_masks(), elem_key(), elem_spelling_resolved(), main(), measure_masks(), scan(), report() (+3 more)

### Community 137 - "re"
Cohesion: 0.10
Nodes (11): explain(), main(), parse(), Record, artifact_symbols(), declared_externs(), Failure, main() (+3 more)

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
Nodes (34): 1 · Headline, 2 · The finding: one decision accounts for the entire residue, 3 · What the game corpus showed that the compiler could not, 3a · Handles appear to eliminate T3 in engine code, 4.1 `retain_in(k)` is missing from FFI.md's contract vocabulary, 4.2 The cycle collector has no program that can exercise it, 4 · Two spec gaps the run found, 5 · Secondary measurements (+26 more)

### Community 143 - "AIF — The Inference Engine"
Cohesion: 0.25
Nodes (8): 10 · Worked example, 1 · Architecture, 3.1 Nodes, 3.2 Edges, 3.3 Node ordering (normative), 3 · The fact graph, 9 · Incrementality, AIF — The Inference Engine

### Community 144 - "test_105_supertraits.psm"
Cohesion: 0.17
Nodes (12): describeAny(), fail(), main(), impl Described for Item, impl Named for Item, impl Reported for Item, impl Sized for Item, Item (+4 more)

### Community 145 - "test_164_array_fields.psm"
Cohesion: 0.19
Nodes (17): Shape, Cells, Empty, corners(), fail(), fourDown(), main(), makeGrid() (+9 more)

### Community 146 - "test_71_nonlexical_extent.psm"
Cohesion: 0.23
Nodes (20): build_a(), build_b0(), build_b(), build_c0(), build_c(), build_d0(), build_d(), build_e() (+12 more)

### Community 148 - "rangeEmitConditionBound"
Cohesion: 0.18
Nodes (26): ir_add(), ir_sub(), generateForRangeGuard(), rangeAddVar(), rangeBinaryInterval(), rangeBoundingVar(), rangeBoundSideOk(), rangeClassifyUpdate() (+18 more)

### Community 149 - "cyc_enter"
Cohesion: 0.19
Nodes (22): 1 · What was built, 2.2 · Correctness of the runtime model, cyc_alloc(), cyc_buffer(), cyc_collect(), cyc_collect_now(), cyc_collect_white(), cyc_collections_run() (+14 more)

### Community 150 - "run"
Cohesion: 0.14
Nodes (52): The benchmark matrix, 2026-09-25, The table, Full Suite Comparison (All 34 Workloads), Target Workloads, Benchmarks, 4 · The regression the exact bound exposed, and why it was not the bound's fault, 2 · Benchmark matrix, 3 · What would actually collect the 9% (+44 more)

### Community 151 - ".charAt"
Cohesion: 0.12
Nodes (23): 2 · The measurement, and the probe that lied, 3 · Why this rules the builtin route out for these four, 4 · Migrating the call sites, 5 · The guard, and why the fixture alone is not one, The String operators lower to methods, and the prefixed names are gone, umsAbsolutePath(), umsHostIsProjectBuildOutput(), file_exists() (+15 more)

### Community 152 - "find_binding"
Cohesion: 0.10
Nodes (20): find_binding(), ir_binding_owns_slot(), ir_binding_predates_loop(), ir_get_var_data(), ir_get_var_slot(), ir_get_var_type(), ir_has_var_type(), ir_is_list_exclusive() (+12 more)

### Community 153 - "struct_entry"
Cohesion: 0.17
Nodes (17): ir_get_struct_field_count(), ir_get_struct_field_type_at(), ir_is_struct_type_name(), ir_alloc_cycle(), ir_alloc_stack(), ir_enum_null_tag(), ir_enum_reserve_null(), ir_enum_set_null_tag() (+9 more)

### Community 154 - "Cross-language results — Prismio vs Rust vs Swift"
Cohesion: 0.11
Nodes (16): 0.1 · Re-measured 2026-08-17, first pass since the `allocs` fix — and the spreads are the finding, 0 · The one-paragraph answer, 1 · The headline table, 2 · Prediction vs measurement, per axis, 2a · "Allocator churn 0.2–0.5×" was wrong about the baseline, not about AIF, 2b · Peak RSS was wrong in our favour, and for the opposite reason to the one assumed, 2c · The tail held, and with the optimiser on it is indistinguishable from Rust's, 3.1 · The optimiser — found here, fixed in this branch (+8 more)

### Community 155 - "test_232_channel_copies.psm"
Cohesion: 0.26
Nodes (19): closeWakesReceiver(), double(), fail(), keptAcrossIterations(), main(), next(), notesStayBoxed(), produceCount() (+11 more)

### Community 156 - "arena_state"
Cohesion: 0.13
Nodes (25): 4. What the IR diff is, all of it, Verified discriminating, by mutating the compiler and rebuilding it, Automatic arena placement — **DONE, 2026-08-07**, 19. Memory budget reporting — **DONE, 2026-08-07**, 7.1 Arena placement, 7.2 Layout selection, 7 · The search, aif_ledger_enter() (+17 more)

### Community 157 - "aifReportPlacementPin"
Cohesion: 0.11
Nodes (25): aif_fn_bracket_blockers(), aif_fn_call_sites(), aif_fn_calls_in_region(), aif_fn_name(), aif_fn_symbol(), aif_site_col(), aif_site_derived_tier(), aif_site_file() (+17 more)

### Community 158 - "common.psm"
Cohesion: 0.21
Nodes (15): benchPrintln(), benchPrintln(), benchPrintln(), benchWrite(), BenchBucket, BenchTree, benchAllocationMutation(), benchBuildMemoryTree() (+7 more)

### Community 159 - "neg_195_callable_bound.psm"
Cohesion: 0.39
Nodes (6): Maybe, Just, Nothing, apply(), main(), impl Maybe

### Community 160 - "Which std functions are properties"
Cohesion: 0.09
Nodes (12): Which std functions are properties, Architecture, X86_64, Environment, GNU, Platform, Windows, impl PlatformQuery (+4 more)

### Community 161 - "aif_concurrency.psm"
Cohesion: 0.16
Nodes (31): cli_arg(), register_forever(), break_is_absorbed_by_its_loop(), join_on_both_paths(), joined_stays_local(), loop_between_spawn_and_join(), main(), no_task_at_all() (+23 more)

### Community 162 - ".concat"
Cohesion: 0.14
Nodes (22): Channel, EAST, NORTH, SOUTH, channelOf(), checkpointTotal(), describe(), main() (+14 more)

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

### Community 169 - "Result"
Cohesion: 0.15
Nodes (12): 1 · The shapes, 3 · What moved, 4 · Pinned, Three ownership shapes that freed memory that was not live, Result, Err, Ok, impl Result (+4 more)

### Community 170 - "math.psm"
Cohesion: 0.13
Nodes (3): impl I16, impl Isize, impl Usize

### Community 171 - "elide_middle"
Cohesion: 0.09
Nodes (9): elide_middle(), run_cold_function_test(), run_crlf_triple_string_test(), run_jit_test(), run_ownership_probes_test(), run_single_loop_inline_test(), run_source_not_utf8_test(), run_string_dispatch_codegen_test() (+1 more)

### Community 172 - "E1: the push check belongs in the preheader, and the profile it was said to need does not exist"
Cohesion: 0.29
Nodes (6): 1 · The distinction that was missing, 2 · The g6 test, which is the whole point, 3 · The benchmark sweep, 4 · Why the two targets did not move, which is the finding worth keeping, 5 · What the guard promises, and what it does not, E1: the push check belongs in the preheader, and the profile it was said to need does not exist

### Community 173 - "layout.py"
Cohesion: 0.23
Nodes (11): candidates(), field_align(), field_width(), Layout, main(), min_size(), mu_for(), record_size() (+3 more)

### Community 174 - "AIF — The T4 Cycle Collector"
Cohesion: 0.12
Nodes (17): 10 · What still needs measurement, 1 · What is actually in scope, 2 · The headline result, 3.1 Why trial deletion and not tracing, 3 · Algorithm, 4 · The cyclic-edge restriction, 5 · Object header, 6.1 Trigger (+9 more)

### Community 175 - "compute.rs"
Cohesion: 0.07
Nodes (18): binary_search_work(), dijkstra_shortest_path(), lz4_compress(), sort_strings(), next_random(), band_sum(), BenchSphere, blake3_chunk() (+10 more)

### Community 176 - "site_arena_scope"
Cohesion: 0.11
Nodes (20): 1 · The headline, 2 · Why an escape-lattice change does not move this, 3 · The measurement that was wrong twice, and why, 4 · `region` measured on g2, 5 · What a region *can* serve, 6 · `list_new_with_capacity`, the one speed result, 7 · What would actually close this, 8 · How much call-site bracketing could reach *(2026-08-16)* (+12 more)

### Community 177 - "bits_test"
Cohesion: 0.09
Nodes (27): Left, with what the next attempt should know, bits_test(), aif_compute_type_acyclic(), aif_layout_all_fields_sequential(), aif_layout_cand_bytes(), aif_layout_cand_field_hot(), aif_layout_field(), aif_layout_rank() (+19 more)

### Community 178 - "strLength"
Cohesion: 0.22
Nodes (7): main(), makeView(), main(), Resolved in 1.1 — was open in v1.0, strLength(), strRepeat(), strSubstring()

### Community 179 - "M6 slice 2 — ordinary struct-path TBAA, and the g2 regression it caused"
Cohesion: 0.33
Nodes (5): All-g old/new — `build/tbaa3` → `build/m6-rc`, Commands, Five-arm standing, Gate, M6 slice 2 — ordinary struct-path TBAA, and the g2 regression it caused

### Community 180 - "main"
Cohesion: 0.13
Nodes (18): binarySearch(), isSorted(), reverse(), sort(), main(), fail(), fill(), grow() (+10 more)

### Community 181 - "release.py"
Cohesion: 0.23
Nodes (11): bootstrap(), build_release_compiler(), check_floor(), die(), host_platform(), llvm_objdump(), macos_minos(), main() (+3 more)

### Community 182 - "test_100_generic_inherent_impl.psm"
Cohesion: 0.18
Nodes (9): fail(), main(), impl Box, impl Cell, impl Score for Int, Box, Cell, Pair (+1 more)

### Community 183 - "test_240_overload_exactness.psm"
Cohesion: 0.16
Nodes (8): fail(), main(), twice(), impl Dup for Int, impl Dup for T, impl Name for U8, Dup, Name

### Community 184 - "test_70_struct_field_release.psm"
Cohesion: 0.29
Nodes (17): check(), crate_inventory_again(), main(), make_crate(), make_crate_inventory(), make_inventory(), nested_owner_again(), nested_owner() (+9 more)

### Community 186 - "verify"
Cohesion: 0.04
Nodes (63): release(), 1 · The methodological point that matters most, 2.1 Definitions, 2.2 The claim under test, 2.3 False sharing from field insensitivity, 2 · Primary metric: tier distribution, 3.1 B1 is a weak headline and should not be the first result, 3.2 Baselines (+55 more)

### Community 187 - "stdlib"
Cohesion: 0.23
Nodes (11): ch_close(), ch_init(), main(), recv(), relax(), s1(), s2(), send() (+3 more)

### Community 189 - "workload.psm"
Cohesion: 0.20
Nodes (18): 7.1 Fixed, 2026-08-17 (compile time), 7 · `tools/ir_snapshot.py` reports a false difference when anything else compiles the same tree, aifCommand(), compiler_build_executable(), compiler_publish_file(), compiler_run_workload(), compiler_set_verify_mode(), compiler_set_workload_mode() (+10 more)

### Community 190 - "prismio"
Cohesion: 0.05
Nodes (40): Checks, IR, Results: LLVM 22.1.8 to 23.1.1 (2026-09-17), What changed in the code, What the upgrade showed about the toolchain, Before opening a pull request, Building the compiler, Code of Conduct (+32 more)

### Community 191 - "Toolchain layout"
Cohesion: 0.12
Nodes (11): `sort()` from a packaged `.plib`, Known issues, Ownership, Platform, Toolchain layout, Traits, plib_sections(), run_aif_verify_test() (+3 more)

### Community 192 - "manifest_records"
Cohesion: 0.11
Nodes (9): aif_records(), aif_thread_records(), manifest_records(), run_aif_annotation_test(), run_aif_concurrency_test(), run_aif_widening_test(), run_pin_tier_test(), run_placement_pin_test() (+1 more)

### Community 193 - "test_111_blanket_impls.psm"
Cohesion: 0.19
Nodes (11): fail(), main(), viaBound(), impl Pretty for T, impl Show for Cat, impl Show for Dog, Cat, Dog (+3 more)

### Community 194 - "test_128_enum_null_reserved.psm"
Cohesion: 0.20
Nodes (16): Exposed, Empty, Node, Generic, None, Some, OptionalTree, Empty (+8 more)

### Community 195 - "test_69_task_results.psm"
Cohesion: 0.32
Nodes (16): print(), println(), acknowledge(), check(), count_span(), int_result(), main(), name_span() (+8 more)

### Community 196 - "named_struct"
Cohesion: 0.17
Nodes (16): byte_gep(), ir_const_str(), ir_copy_struct(), ir_global_str_var(), ir_str_from_int(), ir_str_inline(), ir_str_inline_concat2(), ir_str_inline_concat3() (+8 more)

### Community 197 - "Model"
Cohesion: 0.13
Nodes (3): ann_leaf_name(), Model, Scopes

### Community 198 - "bench.py"
Cohesion: 0.31
Nodes (5): main(), pct(), PROCESS_MEMORY_COUNTERS, run_once(), suite()

### Community 199 - "decl_entry"
Cohesion: 0.14
Nodes (14): add_binding(), decl_entry(), guard_safe_entry(), hash_str(), ir_decl_at(), ir_decl_count(), ir_get_fn_return_type(), ir_index_decl() (+6 more)

### Community 200 - "The 2026-09-30 `--verify` sweep"
Cohesion: 0.09
Nodes (51): Measured, Internal linkage changes inlining, both ways, 3 · The fix, and why only one of the three, 5 · What this opens up, Boundary, Code shape, Gates, Measurement (+43 more)

### Community 201 - "AIF — Gap Analysis"
Cohesion: 0.17
Nodes (12): 1 · Headline findings, 2.1 The invariant needs a boundary the spec does not currently draw, 2.2 Structs are affine references, not values, 2 · Frozen items, one by one, 3.1 What isn't behind the seam at all, 3 · The seam, precisely, 4.2 Scope-based drop, 4.3 Prismio cannot express its own solver (+4 more)

### Community 202 - "g2_cull_probe.c"
Cohesion: 0.27
Nodes (8): a_hdr_pair(), a_hdr_scalar(), a_reg_pair(), a_reg_scalar(), best_ms(), main(), slot_header(), slot_reg()

### Community 203 - "manifest_writer.psm"
Cohesion: 0.30
Nodes (15): umsManifestAddDependency(), umsManifestAppendDependencyBlock(), umsManifestChildIndent(), umsManifestDependencyBlock(), umsManifestDependencyText(), umsManifestEscape(), umsManifestIndentAt(), umsManifestInsertDependency() (+7 more)

### Community 204 - ".toString"
Cohesion: 0.20
Nodes (15): fail(), find(), label(), lengthOf(), main(), make(), named(), spelled() (+7 more)

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
Cohesion: 0.22
Nodes (23): 2. g6 was not blocked on the obligation the notes said it was, 2b. Shared-body bit on bodies that allocate nothing, 2c. Every `List` in the program shared one element node, 3. The corpus, 4. Four tests changed meaning, and why that is the system working, 6. What is still open, Measured, The integer-print leak, and g6's arena (+15 more)

### Community 209 - "Profile"
Cohesion: 0.18
Nodes (4): Profile, walk(), find_gets(), Traversal

### Community 210 - "PIR — Prism Semantic IR"
Cohesion: 0.14
Nodes (16): 1 · Why bodies must ship, 2.1 Not LLVM IR, 2 · Content model, 3 · Deterministic emission, 4 · Merging, 5.1 Sealed surfaces SHALL publish ownership contracts, 5 · Sealed functions, 6.1 Format versioning (+8 more)

### Community 211 - "tokenization"
Cohesion: 0.17
Nodes (15): -O3 for program builds, and the measurement that had gone stale, Result, The claim that was there, The fairness half, What it measures now, What it costs and what it buys, alpha(), byte_sum() (+7 more)

### Community 212 - "memory.rs"
Cohesion: 0.19
Nodes (5): build_memory_tree(), memory_tree_sum(), MemoryParticle, recursive_tree_rebuild(), tree_add()

### Community 213 - "The loop range guard: one precondition per loop, and both checks are gone"
Cohesion: 0.20
Nodes (9): 2 · What it measured, 3 · The bug that made a correct analysis measure 1.29x slower, 4 · Two predictions from the C model, and how they held, 5 · What was rejected, 6 · Where the remaining gap actually is, 7 · The bug that hid all of this, 8 · What is left, 9 · The benchmark was fixed, and what that is worth on its own (+1 more)

### Community 214 - "memory.cpp"
Cohesion: 0.21
Nodes (11): build_memory_tree(), large_buffer_copy(), memory_tree_sum(), MemoryParticle, life, vx, vy, x (+3 more)

### Community 215 - "lexCheckIdentifierSecurity"
Cohesion: 0.18
Nodes (15): diag_warning_at_code(), identifierIndex(), identifierWarnConfusable(), identifierWarnRestricted(), lexCheckIdentifierSecurity(), confusablePrototype(), identifierRangeRow(), isDefaultIgnorable() (+7 more)

### Community 216 - "test_165_ranges_repeat_labels.psm"
Cohesion: 0.08
Nodes (26): 1 · The reader, io_stdin_has_line(), io_stdin_read_all(), io_stdin_take_line(), impl Iterator for StdinLines, impl Stdin, Stdin, StdinLines (+18 more)

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
Cohesion: 0.27
Nodes (10): fail(), main(), maxOf(), pickLarger(), sortInPlace(), impl Ord for Int, impl Ord for String, impl Ord for Version (+2 more)

### Community 224 - "check_source_lists.py"
Cohesion: 0.26
Nodes (9): bootstrap_ps1_list(), bootstrap_sh_list(), Failure, macos_floors(), main(), manifest_native_sources(), package_runtime_bitcode(), read() (+1 more)

### Community 225 - "g4_ecs_world.psm"
Cohesion: 0.38
Nodes (13): main(), make_world(), spawn(), system_movement(), system_physics(), system_regen(), system_render(), Health (+5 more)

### Community 226 - "test_113_std_eq_and_display.psm"
Cohesion: 0.28
Nodes (9): describe(), fail(), main(), same(), impl Display for Colour, impl Eq for Colour, impl Ord for Version, Colour (+1 more)

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

### Community 232 - "LAYOUT 6's candidate space, measured against what this compiler can emit"
Cohesion: 0.17
Nodes (11): 1 · Handles did not land, and two dimensions depend on them, 3 · Bit-packing is blocked by the specification, not by codegen, 4.1 · Both blockers are gone, and the remaining piece is a search loop, 4 · Empirical validation (LAYOUT §8) is behind §7.2, not behind the runner, 5.1 Restricted to what codegen can emit, the model picks the measured cut, 5.2 A linked split is not an indexed split, and the prototype cannot tell them apart, 5.3 What this does and does not unblock, 5 · The cost model is ported, and it could not have ranked the cut it was ported for (+3 more)

### Community 233 - "test_248_enum_is_a_type.psm"
Cohesion: 0.21
Nodes (11): 3.1 Syntax, 3.2 Execution semantics, 3.3 Why not a data file, and why not a declarative pattern description, 3 · `workload` declaration, Color, Blue, Green, Red (+3 more)

### Community 234 - "command.psm"
Cohesion: 0.23
Nodes (12): UmsCommandStepKind, BUILD, RUN, SHELL, UNKNOWN, umsCommand(), umsCommandArgument(), umsCommandFind() (+4 more)

### Community 235 - "ceiling-knapsack.c"
Cohesion: 0.30
Nodes (13): knap_slow_tail(), main(), now_ns(), v0(), v1(), v2(), v3(), v4() (+5 more)

### Community 236 - "benchPrint"
Cohesion: 0.13
Nodes (23): main(), phaseLargeBufferCopy(), main(), phaseKeyValueUpdate(), main(), run(), 2 · Three bugs the library could not be written over, 1 · The benchmark is a serial modulo chain, not a container benchmark (+15 more)

### Community 237 - "cost.c"
Cohesion: 0.31
Nodes (11): bench_next_random(), main(), measure(), mix_d(), mix_e(), mix_h(), mix_i(), now_ns() (+3 more)

### Community 238 - ".sites_of"
Cohesion: 0.15
Nodes (5): ffi_arena_cannot_serve(), Site, vs_sites(), vs_union(), vs_view_of()

### Community 239 - "flow.psm"
Cohesion: 0.29
Nodes (10): loopBodyOf(), semaBlockBreaksOut(), semaBlockDiverges(), semaCallNeverReturns(), semaCheckJumps(), semaCheckJumpsAt(), semaCheckJumpsIn(), semaFailureBuiltinApplies() (+2 more)

### Community 240 - "test_64_generics.psm"
Cohesion: 0.36
Nodes (8): boxUp(), fail(), firstOr(), identity(), main(), Box, Node, Pair

### Community 241 - "main"
Cohesion: 0.09
Nodes (32): clone(), concat(), extend(), fill(), filter(), find(), indexWhere(), max() (+24 more)

### Community 242 - "test_155_vec_methods.psm"
Cohesion: 0.35
Nodes (10): get(), fail(), ints(), jobs(), main(), points(), strings(), impl Copy for Job (+2 more)

### Community 243 - "g2_bench.c"
Cohesion: 0.64
Nodes (6): build_scene(), cull(), list_init(), list_push(), main(), submit()

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
Cohesion: 0.12
Nodes (29): check(), filled(), main(), readWrite(), sumDown(), sumDownOffset(), sumUp(), check() (+21 more)

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
Cohesion: 0.26
Nodes (16): build_hierarchy(), count_visible(), identity_transform(), link_child(), main(), make_node(), propagate(), unit_bounds() (+8 more)

### Community 253 - "benchmarks.hpp"
Cohesion: 0.13
Nodes (8): large_buffer_copy(), main(), now_ns(), BenchTree, left, right, value, main()

### Community 254 - "Compile time — where it goes, and what it scales like"
Cohesion: 0.20
Nodes (9): 1 · The frontend was quadratic in module size, and is now linear, 2.1 AIF's whole fixed point is 18 ms, 2 · The frontend is 4% of a cold build, 3.0 What a small build is now made of, 3.1 The compiler's own self-build, 3 · Cold and incremental, 5 · Pricing the per-module split, without building one, 6 · Reproducing (+1 more)

### Community 255 - "`Int` width — the decision, and the three measurements that made it"
Cohesion: 0.11
Nodes (15): 1 · What the literature actually claims, 2 · Index width is free. Measured, on both targets., 3 · Making overflow UB buys nothing. Measured, on real Prismio programs., 4 · Data width costs 1.33×. Measured, in Prismio., 5 · The cost, stated plainly, 6 · Verdict, 7 · Re-examined 2026-09-24: the whole benchmark suite, 8 · Adaptive width: `Int` means 64 bits, AIF stores it narrow (2026-09-24) (+7 more)

### Community 256 - "Codegen"
Cohesion: 0.09
Nodes (22): Inlining the flat push: rejected, and why the obvious gate does not save it, The finding that motivated it, What was kept, What would make it viable, Where it went wrong, and the gate that did not work, Why it was rejected, 10 · Task 1.3 (MEM-011), curating `list_push_slot`: it works, and it loses, Cost (+14 more)

### Community 257 - "test_73_recursive_release.psm"
Cohesion: 0.40
Nodes (9): Tree, Leaf, Node, depth(), fail(), main(), makeDeep(), makeTree() (+1 more)

### Community 258 - "vg-ceiling-2026-09-06/ceiling.c"
Cohesion: 0.57
Nodes (6): main(), now_ns(), vgrow(), vinit(), vpush(), vpush_out()

### Community 259 - "AIF — The Target Workload"
Cohesion: 0.17
Nodes (12): 0.1 · Engine and game remain two workloads, 0 · The actual stack, 1 · The two halves, 2.1 The annotations belong to the engine layer, 2.2 T3 lives in the engine, T0–T2 in the game, 2.3 The engine/game boundary is where whole-program analysis must hold, 2.4 The manifest becomes a contract between teams, 2.5 Optimisation level has to be **per module**, not per build (+4 more)

### Community 260 - "AIF — Adaptive Inference Framework"
Cohesion: 0.10
Nodes (21): 0 · Conformance language, 10.1 FFI, 10.2 Library distribution, 10 · Boundaries, 12 · What this model gives up *(informative)*, 1.1 What the invariant does not cover, 1 · The invariant, 2.1 Allocation site (+13 more)

### Community 261 - "Channels: what 0.1 needs, and the production design after it"
Cohesion: 0.05
Nodes (41): The measurement, The remaining tuned-g9 gap is not the channel topology, Two hypotheses, both refuted, What the handoff expected, What this leaves, Why the proposed slice cannot close it either, 2 · Why the ordinary release point is wrong here, A data race in `--verify` itself (+33 more)

### Community 262 - "5 · A staged path"
Cohesion: 0.10
Nodes (21): 1 · The four, by fixture, 2 · The fifth was not fixed; it was never a gate failure, 3 · What the four have that test_62 does not, 4 · Why this cannot be fixed by adding the missing disposition, 4a · What is inferred rather than measured, 5 · Reproducing, `PRISMIO_INLINE_ELEMS=0` fails four fixtures, and the fifth was never one, 5 · A staged path (+13 more)

### Community 263 - "BenchSphere"
Cohesion: 0.25
Nodes (8): BenchSphere, cb, cg, cr, r, x, y, z

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
Cohesion: 0.27
Nodes (8): 6.1 Purpose, 6.2 Format, 6.3 Diff semantics, 6 · The tier manifest, fail(), main(), impl Point, Point

### Community 271 - "g2_bench_arena.c"
Cohesion: 0.42
Nodes (9): arena_alloc(), arena_reserve(), arena_reset(), build_scene(), cull(), list_init(), list_push(), main() (+1 more)

### Community 272 - "test_47_aif_minimal_cause.psm"
Cohesion: 0.54
Nodes (7): str_concat(), boxed(), check(), direct(), local(), main(), Box

### Community 273 - "layout_repr.c"
Cohesion: 0.31
Nodes (8): now_ms(), run_boxed_aos(), run_boxed_split(), run_chunked_inline(), run_chunked_split(), run_inline_aos(), run_inline_split(), run_soa()

### Community 274 - "relCollectNode"
Cohesion: 0.25
Nodes (11): ir_var_is_global(), rangeBindsInPattern(), rangeBindsInPatternChain(), rangeIsStableList(), relAddVar(), relBump(), relCollect(), relCollectChain() (+3 more)

### Community 275 - "`key_value_update`: the hash was the cost, and four other things were not"
Cohesion: 0.22
Nodes (8): 1 · The design was already at the C ceiling, 3 · What it is: a scrambling hash throws away locality, 4 · The fold, and why it is not just the identity, 6 · The result, 7 · Verification, 8 · For the next agent, `key_value_update`: the hash was the cost, and four other things were not, Reproduce

### Community 276 - "test_62_split_release.psm"
Cohesion: 0.61
Nodes (7): build(), cold_sum(), count_ids(), main(), make_body(), step(), Body

### Community 277 - "list_get"
Cohesion: 0.05
Nodes (47): 2 · Four things that are not the cost, 1 · The measured design space, 2 · The recorded plan is worth nothing, 3 · Why the header reloads, and what actually fixes it, 4 · Why no LLVM pass will do this for us, 5 · The design that follows, 6 · If the induction-variable analysis is too much, 7 · Sources (+39 more)

### Community 278 - "test_72_reassigned_ownership.psm"
Cohesion: 0.36
Nodes (10): borrow_reassign(), callee_accumulator(), cloned_literal_keeps_length(), literal_mid_loop(), local_accumulator(), main(), makePiece(), returned_accumulator() (+2 more)

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

### Community 287 - "test_106_associated_constants.psm"
Cohesion: 0.29
Nodes (7): fail(), main(), impl Bounded for Dial, impl Bounded for Gauge, Dial, Gauge, Bounded

### Community 288 - "run_corpus_test"
Cohesion: 0.20
Nodes (7): 7 · Coverage, 6 · Reproducers, progress(), run_corpus_test(), build_and_run(), run_parallel(), test_jobs()

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

### Community 294 - "join"
Cohesion: 0.25
Nodes (9): 1 · Why the item existed, 2.1 The mechanism, and it is not a wash, 2 · Where Prismio stands, 3 · What the program found immediately, 5 · Defect 2 — a callee-allocated argument still leaks, and it is not about spawn. Open., 6 · Gates, The concurrency axis, benchStringJoin() (+1 more)

### Community 295 - "test_74_reinit_assignment.psm"
Cohesion: 0.17
Nodes (17): 1 · The baseline, 2 · What was refuted, 3 · Mechanism 1 — self-recursion collapses the root onto a child site, 4 · Mechanism 2 — one parameter-returning path vetoes the whole return set, 5 · What this changes about the plan, `g8_tree_rebuild` leaks 12,282 of 12,284, and it is two mechanisms, not one, What moved, Tree (+9 more)

### Community 296 - "M5.1 — allocator evaluation"
Cohesion: 0.25
Nodes (8): Direct mimalloc result, Direct rpmalloc result, Final gate and decision, Initial dynamic-interposition result, M5.1 — allocator evaluation, Question and acceptance rule, Research choice, Rust standing

### Community 297 - "AIF — Evaluation as a General-Purpose Memory Model"
Cohesion: 0.20
Nodes (10): 1 · The finding that should drive planning, 2 · What holds up as general-purpose, 3 · Where the spec is over-fitted — the 80/20 budget rule, 4 · Regions generalise better than layout, and are under-emphasised, 5 · The biggest hole: closures, 6 · PIR is a heavier liability for general-purpose than for games, 7 · Honest scorecard, 8 · What I would change (+2 more)

### Community 298 - "test_63_placement_pin.psm"
Cohesion: 0.61
Nodes (7): arena_objects(), bracketed_make(), bracketed_pin(), fail(), lexical_pin(), main(), Cmd

### Community 299 - "LLVMModuleRef"
Cohesion: 0.06
Nodes (38): A bug worth remembering, Binary size and compile time against C++ and Rust (2026-09-28), Residuals, measured and not fixed, Second round, Verification, What changed, Where it stands, Where it stood (+30 more)

### Community 300 - "test_88_map_keys.psm"
Cohesion: 0.36
Nodes (4): fail(), impl Copy for Point, impl Key for Point, Point

### Community 301 - "`list_new` allocates nothing until the first push"
Cohesion: 0.33
Nodes (5): Host noise, for whoever measures next, `list_new` allocates nothing until the first push, The defect, The measurement, and why it says nothing, Why keep it

### Community 303 - "A payload-free enum variant allocated uninitialised memory"
Cohesion: 0.50
Nodes (4): 1 · What the matrix saw, and what this host did not, 4 · Before / after, 5 · What to check next, A payload-free enum variant allocated uninitialised memory

### Community 304 - "maphash.psm"
Cohesion: 0.40
Nodes (9): clock_gettime(), write(), distinctKeys(), main(), nextRandom(), now(), say(), vocabulary() (+1 more)

### Community 305 - "AIF — Adaptive Inference Framework"
Cohesion: 0.20
Nodes (10): AIF — Adaptive Inference Framework, Conformance is graded, Contents, Running the prototype, Start here, Status, The model in one screen, Two things to know before extending this (+2 more)

### Community 306 - "AIF — Layout Results (A1)"
Cohesion: 0.17
Nodes (12): 1 · Headline, 2 · The static profile is exact, 4 · Spec defect found: LAYOUT §5.4's total could go negative, 6 · What to do next, AIF — Layout Results (A1), Reproducing, Particle, life (+4 more)

### Community 307 - "M2.0 — release on reassignment, and the M2 gate restated"
Cohesion: 0.20
Nodes (9): 1 · What this closes, 2 · The defect was documented, deliberate, and had stopped being true, 4 · The two things that cost the most to find, 5 · The fixture, and how it nearly measured nothing, 6 · Timing, Appendix — M2's closing state, 2026-08-23, Delivered, M2.0 — release on reassignment, and the M2 gate restated (+1 more)

### Community 308 - "16. A practical review checklist"
Cohesion: 0.33
Nodes (6): 16. A practical review checklist, Architecture, Code, Comments, Correctness, Performance

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
Cohesion: 0.51
Nodes (10): 4 · Defect 1 — the task handle had no owner. Fixed., print(), println(), check(), copied_handle(), join_inside_a_loop(), main(), many_frames() (+2 more)

### Community 316 - "test_96_channels.psm"
Cohesion: 0.49
Nodes (9): capacity_and_length(), fail(), main(), pool_round_trip(), serial_round_trip(), step(), worker(), Answer (+1 more)

### Community 317 - "test_94_selective_imports.psm"
Cohesion: 0.47
Nodes (3): shoutUpper(), fail(), main()

### Community 318 - "Genuinely-cold compilation"
Cohesion: 0.25
Nodes (7): 1 · What the standing entry actually named, 2.1 One invocation producing both was measured and rejected, 2 · Why the first step only got half of it, 3 · What is left, and why it is left, 4 · Result, 5 · Gates, Genuinely-cold compilation

### Community 319 - "Prismio performance benchmarks"
Cohesion: 0.10
Nodes (17): Coverage, Currently Unsupported by Prismio, Infrastructure changes, Prismio performance benchmarks, Run, The three arms must be the same program, What `results.json` records, When a difference counts (+9 more)

### Community 320 - "test_143_string_compare.psm"
Cohesion: 0.67
Nodes (5): agrees(), fail(), main(), referenceOrder(), sign()

### Community 321 - "8.4 Views — slices and element references"
Cohesion: 0.20
Nodes (10): 8.1 Handles, 8.2 The compiler owns layout, 8.3 The static region, 8.4 Views — slices and element references, 8 · Representation, Cost, stated plainly, Element references are views too — the deep consequence, Invalidation, without a borrow checker (+2 more)

### Community 322 - "2 · Where it stands"
Cohesion: 0.52
Nodes (7): The result, benchChannelPipeline(), stage1(), stage2(), Msg, WorkConfig, 2 · Where it stands

### Community 323 - "11 · Known weaknesses"
Cohesion: 0.29
Nodes (7): 11.1 Field sensitivity is object-insensitive, 11.2 The context set is discovered from facts that are still moving, 11.3 Loops are handled by the lattice, not by a loop analysis, 11.4 There is no interprocedural path sensitivity, 11.5 ~~The `⊤` context is a cliff~~ — resolved in 1.2, 11.6 Everything here assumes whole-program PIR, 11 · Known weaknesses

### Community 324 - "Map probing and full-width key hashing"
Cohesion: 0.22
Nodes (8): Changes that shipped, Maintained benchmark results, Map probing and full-width key hashing, Memory cost, Rejected experiments and research, Remaining critical gaps, Supplemental workloads, Validation and reproduction

### Community 325 - "15. Working with agents"
Cohesion: 0.40
Nodes (5): 15. Working with agents, Do not leave partial modularization, Do not solve architecture problems with comments, Do not solve architecture problems with one-off wrappers, Prefer one coherent refactor over many cosmetic edits

### Community 326 - "Debug-mode integer overflow checking"
Cohesion: 0.20
Nodes (10): 1 · The measurement that changed the plan, 2 · What it actually costs on real programs, 3 · Implementation, 4 · A parser defect this found, 5 · The gate, 6 · What this does not do, 7 · Also in this change: the benchmark clock, 8 · Sources (+2 more)

### Community 328 - "A `spawn`ed call's owned temporary argument now has an owner"
Cohesion: 0.22
Nodes (8): 1 · The defect, 3 · The release point, and its licence, 4 · What it costs the benchmark set: nothing, 5 · Two stale claims found on the way, 6 · Reproducing, 7 · Still open in this area, A `spawn`ed call's owned temporary argument now has an owner, prismio_task_release()

### Community 329 - "test_120_min_max_abs.psm"
Cohesion: 0.70
Nodes (4): check(), clampSum(), clampSumInline(), main()

### Community 330 - "3. Before changing code"
Cohesion: 0.40
Nodes (5): 3. Before changing code, Judge changes by emitted behavior, Self-hosting comes first, Two generations before trusting a compiler change, Understand the existing boundary first

### Community 331 - "5 · Annotations"
Cohesion: 0.13
Nodes (15): 5.0.1 Annotations are assertions, not directives *(normative)*, 5.0 Why exactly these four *(normative rationale)*, 5.1 `unique`, 5.2.1.1 Call-site placement, and which regime it uses *(normative)*, 5.2.1.2 Non-lexical extent, and what it does to the obligations *(normative)*, 5.2.1 A region only reaches allocations in its own function *(normative limitation)*, 5.2 `region { … }`, 5.3 `workload(…)` (+7 more)

### Community 332 - "Security Policy"
Cohesion: 0.25
Nodes (7): Acknowledgements, Reporting a Vulnerability, Response Timeline, Responsible Disclosure, Scope, Security Policy, Supported Versions

### Community 333 - "2 · Fact domains"
Cohesion: 0.29
Nodes (7): 2.1 `E` — escape, 2.2 `A` — aliasing, 2.3 `T` — thread affinity, 2.4 `C` — cyclicity, 2.5 `L` — lifetime determinacy *(derived)*, 2.6 The product, 2 · Fact domains

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

### Community 346 - "test_253_void_closure.psm"
Cohesion: 0.39
Nodes (7): forEach(), add(), each(), fail(), main(), twice(), total

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

### Community 351 - "get_directory"
Cohesion: 0.22
Nodes (10): absolute_directory(), compiler_prepare_output_path(), ensure_directory_exists(), file_content_hash(), native_deps_current(), native_deps_path(), native_object_entry(), object_cache_dir() (+2 more)

### Community 352 - "g2_bench.psm"
Cohesion: 0.54
Nodes (7): build_scene(), cull(), main(), submit(), DrawCmd, Renderable, Stats

### Community 353 - "g7_particles.psm"
Cohesion: 0.61
Nodes (7): alive(), build(), main(), make_particle(), step(), Particle, Vec3

### Community 355 - "test_map_probe.psm"
Cohesion: 0.43
Nodes (3): impl Copy for CollidingKey, impl Key for CollidingKey, CollidingKey

### Community 356 - "node_args_find"
Cohesion: 0.25
Nodes (8): aif_arg_copies_view(), aif_call_arg_outlives_call(), aif_call_arg_retained(), aif_note_arg_aliased(), aif_note_arg_copied(), aif_note_arg_retained(), aif_note_call_args(), node_args_find()

### Community 357 - "Counted scalar fills and struct-list initialization"
Cohesion: 0.29
Nodes (6): Counted scalar fills and struct-list initialization, Interpretation and remaining work, Measurement Results (25-run interleaved comparison), Mechanisms, Reproduction and evidence, Research grounding

### Community 358 - "noise floor that decided it"
Cohesion: 0.25
Nodes (7): Hoisting the List header out of the loop: what worked, what did not, and the, noise floor that decided it, Note on measuring g5 at all, The finding, What the measurement said, What this leaves for the real fix, What was tried

### Community 359 - "test_30_diamond_imports.psm"
Cohesion: 0.44
Nodes (5): left_value(), right_value(), shared_double(), fail(), main()

### Community 360 - "evidence/README.md"
Cohesion: 0.04
Nodes (31): AIF Evidence, Before quoting any number, Judgement, Projected, not measured, 1 · The defect, 4 · The fix, and the line it must not cross, 5 · Result, 6 · Cost: none, and it is provable rather than measured (+23 more)

### Community 362 - "test_175_variant_from_context.psm"
Cohesion: 0.36
Nodes (8): Outcome, Bad, Good, fail(), main(), nothing(), orZero(), Slot

### Community 364 - "The relational tier, byte-sized Bool elements, and three gaps read from disassembly"
Cohesion: 0.33
Nodes (5): Findings worth keeping, Numbers (scale 4), Tests, The relational tier, byte-sized Bool elements, and three gaps read from disassembly, What changed

### Community 365 - "7. Functions and control flow"
Cohesion: 0.40
Nodes (5): 7. Functions and control flow, Do not repeat ownership-sensitive work, One responsibility per function, Prefer early returns, Use `loop` for unconditional loops

### Community 366 - "text.psm"
Cohesion: 0.13
Nodes (15): Found while building this, not caused by it, Measurement 1 — the `+` chain had to be flattened, Measurement 2 — a property may not allocate, The cost: 64 claimed global names, The String surface: operators, properties, iteration, Verification, What landed, 1 · Left for 0.1 (+7 more)

### Community 367 - "edit_distance"
Cohesion: 0.14
Nodes (31): Bugs found on the way, Changes, Method, Results: the string-benchmark gap (2026-09-11), Root causes, Still open, The suite, before and after, Block partitioning in `sort` (+23 more)

### Community 368 - "4 · Transfer rules"
Cohesion: 0.25
Nodes (8): 4.1 Escape module, 4.2 Aliasing module, 4.3 Thread module, 4.4 Cyclicity module, 4.5 Closure capture, 4.6 Dynamic dispatch, 4.7 Generics and ownership contexts, 4 · Transfer rules

### Community 369 - "5 · The fixed-point algorithm"
Cohesion: 0.25
Nodes (8): 5.1 Iteration strategy (normative), 5.2 The algorithm, 5.3 The give-up condition — and why you cannot simply stop, 5.4 Determinism (normative), 5.5 Termination, 5.6 Minimal cause, 5.7 Optimisation levels, 5 · The fixed-point algorithm

### Community 370 - "compiler_plib_interface"
Cohesion: 0.38
Nodes (6): compiler_plib_interface(), plib_empty(), plib_read_sections(), read_u32_le(), read_u64_le(), FILE

### Community 372 - "7 · Specialisation strategy and dedup"
Cohesion: 0.25
Nodes (8): 7.0.1 Three strategies, 7.0.2 Dedup still applies, 7.0 The ownership-divergence ratio, 7.1 Layer 1 — the relevant-parameter mask *(pre-instantiation, cheapest, does the most work)*, 7.2 Layer 2 — semantic equivalence *(pre-codegen)*, 7.3 Layer 3 — structural dedup *(post-codegen)*, 7.4 Budget-driven collapse, 7 · Specialisation strategy and dedup

### Community 373 - "aif_ledger_init"
Cohesion: 0.60
Nodes (3): aif_ledger_init(), cyc_lock_init(), BOOL

### Community 374 - "test_35_short_circuit.psm"
Cohesion: 0.32
Nodes (7): 2.1 Contents, 2.2 Format, 2 · The access profile, fail(), main(), touched(), side_effects

### Community 375 - "owned-key-existing-leak.psm"
Cohesion: 0.43
Nodes (3): impl Copy for ProbeKey, impl Key for ProbeKey, ProbeKey

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

### Community 383 - "A general affine index matcher, built and reverted"
Cohesion: 0.29
Nodes (6): A general affine index matcher, built and reverted, What it measured, What was built, What would actually be needed, Why: a hypothesis, and the two experiments that refuted it, benchKnapsack()

### Community 384 - "`key_value_update`: one probe in `mapSet`, and a loop guard that is a net loss"
Cohesion: 0.29
Nodes (6): `key_value_update`: one probe in `mapSet`, and a loop guard that is a net loss, Reproduce, Verification, What is left, and where it is, What was built: `mapSet` stops asking a question the probe answered, Where the time is

### Community 385 - "MEM-035: the stencil's offsets were never the problem — its condition was"
Cohesion: 0.33
Nodes (6): 1 · What the spec said, and what was actually there, 2 · The fix, 3 · Measured, 4 · A measurement that had to be thrown away first, MEM-035: the stencil's offsets were never the problem — its condition was, benchConvolution()

### Community 386 - "v0.1 release candidate — the complete local gate"
Cohesion: 0.29
Nodes (6): Five-arm standing, Sanitizers, Timings, v0.1 release candidate — the complete local gate, What is *not* proved here, What the gate ran

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

### Community 400 - "A field read is a view of the object it was read from"
Cohesion: 0.33
Nodes (5): A field read is a view of the object it was read from, Scope, The defect, Verification, What it costs

### Community 401 - "M4.1 — first-class `Slice<T>`"
Cohesion: 0.33
Nodes (5): Discriminating gates, M4.1 — first-class `Slice<T>`, Ownership result, Surface and representation, Verification and measurement

### Community 402 - "test_156_index_store.psm"
Cohesion: 0.54
Nodes (7): arrays(), fail(), main(), strings(), throughParameter(), vectors(), Pt

### Community 403 - "test_188_stdin.psm"
Cohesion: 0.46
Nodes (7): check(), childFirstThenRest(), childLengths(), childLines(), fail(), main(), run()

### Community 404 - "test_235_channel_owned_messages.psm"
Cohesion: 0.61
Nodes (7): closedSendsRelease(), fail(), main(), receivedNotesRelease(), receivedVecsRelease(), shortStringsArriveIntact(), Note

### Community 405 - "min/max/abs, and the call that used to cost 1.79x"
Cohesion: 0.33
Nodes (5): 1 · Why this existed, 2 · What was built, 3 · What it is worth, 5 · What is still declined, min/max/abs, and the call that used to cost 1.79x

### Community 406 - "test_29_overloads.psm"
Cohesion: 0.36
Nodes (5): choose(), combine(), combine(), fail(), main()

### Community 407 - "8 · Annotations as axioms and constraints"
Cohesion: 0.33
Nodes (6): 8.1 Seeding and cutting, 8.2 `unique` — verification is complete, 8.3 `region` — verification is sound, and imprecision costs only performance, 8.4 `pin`, 8.5 Verification under budget, 8 · Annotations as axioms and constraints

### Community 408 - "test_50_scalar_lists.psm"
Cohesion: 0.46
Nodes (7): bools_survive(), check(), float_round_trip(), grows_past_capacity(), main(), overwrite(), sum_ints()

### Community 409 - "test_80_data_view_conversion.psm"
Cohesion: 0.57
Nodes (7): columnCount(), columnsAreReadable(), fail(), main(), mutateColumns(), Pair, Sample

### Community 410 - "A binding that escapes through a callee's return was freed under its caller"
Cohesion: 0.24
Nodes (14): 1 · The defect, 2 · Which escape routes were already guarded, and which was not, 3 · The fix, 4 · Before / after, 6 · Sources, A binding that escapes through a callee's return was freed under its caller, Two things that were measured, not reasoned, band() (+6 more)

### Community 411 - "3 · The tier ladder"
Cohesion: 0.33
Nodes (6): 3 · The tier ladder, T0 — Value / stack, T1 — Region / arena, T2 — Unique owned, T3 — Shared, non-atomic reference counting, T4 — Managed residue

### Community 412 - "How to use it"
Cohesion: 0.29
Nodes (6): AIF and memory gap tracker, G-001 — `aif_rc` asserts a proxy that no longer tracks its property, G-002 — ownership annotations are not part of trait conformance, G-003 — return-position ownership is not part of trait conformance, G-004 — a node field assigned a local String, and a field overwritten while aliased, How to use it

### Community 413 - "aifEmitPackingAdvice"
Cohesion: 0.33
Nodes (6): aif_field_has_range(), aif_field_range_bytes(), aif_field_range_hi(), aif_field_range_lo(), aif_profile_is_measured(), aifEmitPackingAdvice()

### Community 414 - "impl Key for PathKey"
Cohesion: 0.40
Nodes (3): impl Copy for PathKey, impl Key for PathKey, PathKey

### Community 415 - "`Vec<T>` is used through methods"
Cohesion: 0.09
Nodes (26): Landing, Properties are declared: `prop`, Still open, The rule before, The rule now, 2 · What 0.1 ships, 4 · Limits in 0.1, 5 · For 0.2: needs design first (+18 more)

### Community 416 - "Null empty variants for boxed recursive enums"
Cohesion: 0.29
Nodes (6): Allocation and validation evidence, Null empty variants for boxed recursive enums, Representation and safety boundaries, Reproduction, Result, Why the pass is restricted to recursive enums

### Community 418 - "AIF — Engine/Game Boundary Results (A2)"
Cohesion: 0.29
Nodes (7): 1 · Result, 2 · The boundary is cheap because the API is handle-based, 3 · Most of the sealing loss is recoverable with contracts, 4 · A prototype bug worth recording, 5 · Compiler bug found: `List<Int>` miscompiles, 6 · What this does not show, AIF — Engine/Game Boundary Results (A2)

### Community 419 - "6 · Ownership contexts"
Cohesion: 0.40
Nodes (5): 6.1 What a context is, 6.2 Context ordering, 6.3 Discovery (demand-driven), 6.4 The context cap, 6 · Ownership contexts

### Community 420 - "neg_191_property_spelling.psm"
Cohesion: 0.60
Nodes (3): main(), impl Square, Square

### Community 421 - "M4.3c — mutable DataView round trip"
Cohesion: 0.25
Nodes (7): Correctness and closure gates, Is Prismio DataView hand-tuned?, M4.3c — mutable DataView round trip, Mutable g1 layout gate, side by side with Rust, Standard-corpus regression gate, What changed, data_view_column()

### Community 422 - "test_176_match_diverges.psm"
Cohesion: 0.70
Nodes (4): code(), firstPositive(), main(), orZero()

### Community 423 - "binder_return_probe.psm"
Cohesion: 0.83
Nodes (3): findLiteral(), main(), payloadOr()

### Community 424 - "test_200_unicode_identifiers.psm"
Cohesion: 0.83
Nodes (3): main(), 合計(), Точка

### Community 425 - "The generated release loops on its tail self field"
Cohesion: 0.29
Nodes (6): Discriminator, Gates, Lowering, Remaining boundary, Result, The generated release loops on its tail self field

### Community 427 - "irCallReleasesTemporaries"
Cohesion: 0.67
Nodes (3): aif_fn_may_return_param(), aif_fn_may_return_view_of_param(), irCallReleasesTemporaries()

### Community 428 - "AIF Prototype"
Cohesion: 0.29
Nodes (6): AIF Prototype, Approximations, Running, Two bugs found here, both worth remembering, Two roles, What it implements

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

### Community 471 - "impl Int"
Cohesion: 0.10
Nodes (4): 1 · The lowering, 4 · Not done, std.math: Float's functions, and the three Float codegen bugs under them, impl Int

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
Cohesion: 0.20
Nodes (10): 1 · The thesis, stated so it can be killed, 2 · Fairness rules, 3 · The suite, 4 · Isolating the memory-model tax, 5 · Where AIF is predicted to lose, 6 · Predicted results, 7 · Reporting, AIF — Cross-Language Comparison Suite (+2 more)

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
- **1225 isolated node(s):** `Empty`, `Node`, `Value`, `Empty`, `None` (+1220 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2598 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **136 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ASTNode` connect `ASTNode` to `checker.psm`, `bridge.psm`, `ownership.psm`, `symbols.psm`, `impl Parser`, `imports.psm`, `decl.psm`, `model.psm`, `ptr_to_node`, `compile.psm`, `relCollectNode`, `rangeEmitConditionBound`, `ranges.psm`, `module.psm`, `aifEmitPackingAdvice`, `NodeKind`, `relations.psm`, `walk.psm`, `workload.psm`, `.equals`, `relVisitAccess`, `aifEmitManifest`, `report.psm`, `flow.psm`, `dump.psm`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Why does `release()` connect `verify` to `AIF — Cross-Language Comparison Suite`, `AIF — The Target Workload`, `Decisions`, `g5_asset_cache.psm`, `LAYOUT 6's candidate space, measured against what this compiler can emit`, `5 · The fixed-point algorithm`, `algorithms.cpp`, `g3_scene_graph.psm`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Why does `__builtin_string_len()` connect `__builtin_string_len` to `checker.psm`, `bridge.psm`, `ownership.psm`, `symbols.psm`, `std/io.psm`, `src/main.psm`, `imports.psm`, `decl.psm`, `string.psm`, `ptr_to_node`, `display.psm`, `Language surface`, `strCopyRangeInto`, `test_47_aif_minimal_cause.psm`, `rangeEmitConditionBound`, `commands.psm`, `.charAt`, `unicode.psm`, `test_72_reassigned_ownership.psm`, `module.psm`, `aif_concurrency.psm`, `.concat`, `str_with_capacity`, `test_74_reinit_assignment.psm`, `relations.psm`, `aifWalk`, `scanner.psm`, `maphash.psm`, `walk.psm`, `strLength`, `use_it`, `.equals`, `unicode_conformance.psm`, `The 2026-09-30 `--verify` sweep`, `aifEmitManifest`, `test_19_runtime_split.psm`, `rt_alloc`, `report.psm`, `aif_tiers.psm`, `manifest_writer.psm`, `targets/target.psm`, `ASTNode`, `test_53_memory_budget.psm`, `UmsDiagnostic`, `key-before.psm`, `text.psm`, `workspace.psm`, `ums_cli.psm`, `dump.psm`, `project.psm`, ``Int` width — the decision, and the three measurements that made it`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 244 inferred relationships involving `__builtin_string_len()` (e.g. with `keyHashBytes()` and `6 · Verdict`) actually correct?**
  _`__builtin_string_len()` has 244 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Empty`, `Node`, `Value` to the rest of the system?**
  _1225 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `checker.psm` be split into smaller, more focused modules?**
  _Cohesion score 0.03933279039604259 - nodes in this community are weakly interconnected._
- **Should `bridge.psm` be split into smaller, more focused modules?**
  _Cohesion score 0.015403374309461006 - nodes in this community are weakly interconnected._
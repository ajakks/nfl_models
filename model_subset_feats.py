#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:34:00 2022

@author: tomb
"""

df = pd.read_csv('/home/tomb/nfl_models/modeling_data/nfl_spreads_all9.csv')


begin_year=2014
cutoff_week=4
val_year_cutoff=2021
cur_week=9

df['spread_abs']=df['spread_favorite']*-1
df['line']=df['over_under_line']
df['theWeek']=df['schedule_week']
df['spread_sqrd']=df['spread_abs']**2
df['spread_int_line']=df['spread_abs']*df['line']


df = df[df['fav_cover'] != 'push']


#create target fields
df['cover_int']=0
df['cover_int'][(df['fav_cover']=='cover')]=1

df.replace(np.nan, 0.01, inplace=True)

cols = ['rec_depth_center_behind_los_interceptions_rec_depth_dog',
'pass_under_pressure_blitz_grades_hands_drop_pass_pressure_fav',
'pass_concept_no_screen_grades_coverage_defense_pass_conc_fav',
'pass_under_pressure_no_pressure_grades_coverage_defense_pass_pressure_dog',
'pass_under_pressure_blitz_grades_coverage_defense_pass_pressure_dog',
'pass_concept_screen_grades_hands_drop_pass_conc_dog',
'pass_under_pressure_blitz_grades_coverage_defense_pass_pressure_fav',
'pass_concept_screen_grades_hands_drop_pass_conc_fav',
'pass_under_pressure_blitz_grades_hands_drop_pass_pressure_dog',
'pass_under_pressure_no_pressure_grades_coverage_defense_pass_pressure_fav',
'pass_concept_no_screen_grades_coverage_defense_pass_conc_dog',
'pass_under_pressure_blitz_sacks_pass_pressure_fav',
'off_dvoa_fav',
'run_block_zone_snap_counts_run_block_run_block_fav',
'run_block_zone_snap_counts_run_play_run_block_fav',
'block_summary_snap_counts_lg_block_dog',
'def_coverage_summary_snap_counts_coverage_def_cov_summ_fav',
'pass_time_more_avg_time_to_throw_time_pocket_dog',
'rec_depth_behind_los_grades_hands_drop_rec_depth_dog',
'run_block_zone_snap_counts_run_block_percent_run_block_fav',
'run_block_gap_snap_counts_run_block_percent_run_block_fav',
'def_coverage_summary_snap_counts_pass_play_def_cov_summ_fav',
'special_teams_tgs_fav',
'rec_concept_screen_contested_catch_rate_rec_concept_dog',
'rec_summary_caught_percent_rec_fav',
'pass_under_pressure_blitz_sacks_pass_pressure_dog',
'rec_depth_behind_los_drop_rate_rec_depth_fav',
'off_rush_dvoa_fav',
'rec_depth_behind_los_drops_rec_depth_dog',
'total_dvoa_fav',
'rec_depth_short_first_downs_rec_depth_dog',
'pass_depth_medium_avg_time_to_throw_passdepth_fav',
'kicking_pat_percent_dog',
'rec_depth_medium_fumbles_rec_depth_fav',
'pass_under_pressure_no_blitz_avg_time_to_throw_pass_pressure_dog',
'draft_yr_passing_dog',
'kicking_pat_percent_fav',
'run_block_penalties_run_block_fav',
'punting_snaps_dog',
'rec_depth_short_yards_rec_depth_dog',
'punting_attempts_with_hangtime_dog',
'pass_rush_true_pass_set_pass_rush_win_rate_pass_rush_summ_fav',
'block_summary_block_percent_block_fav',
'pass_under_pressure_no_blitz_dropbacks_percent_pass_pressure_dog',
'punting_attempts_dog',
'rec_depth_behind_los_contested_catch_rate_rec_depth_fav',
'off_dvoa_dog',
'pressure_source_hurries_allowed_pass_allow_pressure_fav',
'pass_under_pressure_blitz_dropbacks_percent_pass_pressure_dog',
'def_coverage_scheme_zone_yards_per_coverage_snap_def_cov_schem_dog',
'height_clean_passing_dog',
'rec_depth_medium_touchdowns_rec_depth_dog',
'def_summary_grades_defense_penalty_def_stats_dog',
'pass_depth_deep_grades_pass_passdepth_fav',
'pass_under_pressure_blitz_sack_percent_pass_pressure_fav',
'block_summary_non_spike_pass_block_percentage_block_fav',
'def_coverage_summary_tackles_def_cov_summ_fav',
'rush_summary_routes_rush_dog',
'rec_depth_medium_caught_percent_rec_depth_fav',
'def_coverage_summary_yards_per_coverage_snap_def_cov_summ_dog',
'pass_concept_no_screen_grades_pass_route_pass_conc_fav',
'pass_depth_deep_avg_depth_of_target_passdepth_fav',
'def_coverage_summary_stops_def_cov_summ_fav',
'rec_depth_short_yards_per_reception_rec_depth_fav',
'kicking_thirty_attempts_fav',
'pass_rush_pass_rush_win_rate_pass_rush_summ_fav',
'pass_depth_medium_first_downs_passdepth_fav',
'rec_depth_deep_targeted_qb_rating_rec_depth_fav',
'pass_depth_medium_drop_rate_passdepth_fav',
'pass_under_pressure_blitz_dropbacks_pass_pressure_dog',
'height_clean_rush_fav',
'pass_depth_behind_los_grades_pass_passdepth_dog',
'run_defense_grades_defense_penalty_run_def_summ_dog',
'def_slot_coverage_qb_rating_against_slot_cov_fav',
'punting_total_hangtime_dog',
'rec_depth_short_yards_after_catch_rec_depth_dog',
'pass_rush_true_pass_set_snap_counts_pass_play_pass_rush_summ_dog',
'block_summary_pass_block_percent_block_fav',
'punting_yards_dog',
'def_coverage_summary_targets_def_cov_summ_fav',
'rec_depth_medium_routes_rec_depth_dog',
'pass_under_pressure_pressure_grades_pass_route_pass_pressure_fav',
'draft_yr_passing_fav',
'rush_summary_scrambles_rush_dog',
'pass_summary_grades_run_passing_dog',
'pass_depth_medium_accuracy_percent_passdepth_fav',
'rec_depth_short_targets_rec_depth_dog',
'rec_depth_medium_targets_rec_depth_dog',
'rec_depth_right_deepcaught_percent_rec_depth_fav',
'punting_total_net_yards_dog',
'pass_under_pressure_blitz_passing_snaps_pass_pressure_dog',
'kicks_fav',
'rec_scheme_zone_yards_after_catch_per_reception_rec_schem_dog',
'rec_depth_short_drops_rec_depth_dog',
'rec_depth_medium_targets_percent_rec_depth_dog',
'pass_depth_short_yards_passdepth_dog',
'rec_depth_short_routes_rec_depth_dog',
'rush_summary_elu_recv_mtf_rush_dog',
'def_coverage_summary_touchdowns_def_cov_summ_fav',
'rec_depth_behind_los_drops_rec_depth_fav',
'def_summary_snap_counts_dl_def_cov_fav',
'def_summary_snap_counts_dl_outside_t_def_cov_fav',
'rec_concept_screen_contested_receptions_rec_concept_dog',
'rush_summary_zone_attempts_rush_fav',
'pass_under_pressure_no_pressure_grades_run_pass_pressure_dog',
'rec_scheme_zone_interceptions_rec_schem_fav',
'rec_depth_medium_contested_catch_rate_rec_depth_fav',
'punting_out_of_bounds_fav',
'rush_summary_scramble_yards_rush_dog',
'rec_concept_screen_fumbles_rec_concept_fav',
'pass_concept_screen_grades_pass_pass_conc_dog',
'punting_inside_twenties_dog',
'pass_under_pressure_grades_run_pass_pressure_dog',
'pass_under_pressure_no_blitz_touchdowns_pass_pressure_dog',
'shuttle_passing_dog',
'def_summary_snap_counts_dl_a_gap_def_cov_dog',
'rec_concept_screen_pass_block_rate_rec_concept_dog',
'rec_concept_slot_caught_percent_rec_concept_dog',
'rec_depth_short_yards_after_catch_per_reception_rec_depth_fav',
'pass_depth_medium_drops_passdepth_fav',
'pass_under_pressure_blitz_grades_pass_route_pass_pressure_fav',
'pass_depth_penalties_passdepth_dog',
'pass_summary_sack_percent_passing_fav',
'rec_depth_center_deep_interceptions_rec_depth_fav',
'pass_concept_no_screen_grades_run_pass_conc_dog',
'pass_concept_declined_penalties_pass_conc_fav',
'pass_under_pressure_blitz_btt_rate_pass_pressure_fav',
'pass_under_pressure_blitz_def_gen_pressures_pass_pressure_dog',
'pass_concept_screen_twp_rate_pass_conc_fav',
'rec_depth_short_targets_percent_rec_depth_dog',
'pass_depth_medium_bats_passdepth_dog',
'pass_depth_behind_los_sacks_passdepth_dog',
'def_summary_grades_defense_penalty_def_cov_dog',
'pass_depth_deep_spikes_passdepth_fav',
'pass_depth_deep_passing_snaps_passdepth_fav',
'rush_summary_grades_pass_rush_fav',
'pass_depth_behind_los_sack_percent_passdepth_fav',
'def_coverage_summary_missed_tackle_rate_def_cov_summ_dog',
'rec_depth_right_deepyprr_rec_depth_fav',
'rec_depth_declined_penalties_rec_depth_dog',
'rec_scheme_penalties_rec_schem_fav',
'run_defense_missed_tackles_run_def_summ_fav',
'def_coverage_summary_receptions_def_cov_summ_fav',
'rec_depth_short_pass_plays_rec_depth_dog',
'def_summary_hurries_def_cov_fav',
'pass_depth_behind_los_pressure_to_sack_rate_passdepth_fav',
'def_coverage_summary_snap_counts_coverage_def_cov_summ_dog',
'kicking_one_percent_fav',
'pass_depth_deep_spikes_passdepth_dog',
'run_block_gap_snap_counts_run_play_run_block_fav',
'def_coverage_summary_grades_defense_penalty_def_cov_summ_dog',
'rec_concept_declined_penalties_rec_concept_dog',
'def_coverage_scheme_penalties_def_cov_schem_dog',
'rec_summary_interceptions_rec_fav',
'def_summary_missed_tackle_rate_def_stats_fav',
'pass_under_pressure_blitz_interceptions_pass_pressure_dog',
'kicking_grades_fgep_kicker_dog',
'def_coverage_summary_catch_rate_def_cov_summ_dog',
'pass_concept_no_screen_first_downs_pass_conc_fav',
'rec_depth_right_behind_los_pass_block_rate_rec_depth_dog',
'pass_depth_short_hit_as_threw_passdepth_dog',
'pass_depth_medium_sacks_passdepth_dog',
'tackling_tgs_fav',
'pressure_source_penalties_pass_allow_pressure_fav',
'pass_concept_screen_btt_rate_pass_conc_fav',
'rec_depth_short_longest_rec_depth_dog',
'rec_concept_slot_drop_rate_rec_concept_fav',
'pass_depth_deep_thrown_aways_passdepth_dog',
'rec_depth_right_deepcontested_catch_rate_rec_depth_fav',
'run_block_gap_snap_counts_run_block_run_block_fav',
'rec_concept_slot_touchdowns_rec_concept_dog',
'pass_concept_screen_big_time_throws_pass_conc_fav',
'pass_depth_behind_los_bats_passdepth_dog',
'rec_summary_wide_rate_rec_dog',
'rec_depth_right_behind_los_touchdowns_rec_depth_dog',
'pressure_source_penalties_pass_allow_pressure_dog',
'pass_concept_no_screen_grades_defense_pass_conc_dog',
'pass_depth_short_sacks_passdepth_fav',
'pass_depth_behind_los_btt_rate_passdepth_fav',
'pass_depth_medium_btt_rate_passdepth_dog',
'pass_depth_short_completion_percent_passdepth_dog',
'pass_under_pressure_no_pressure_grades_defense_penalty_pass_pressure_fav',
'pass_under_pressure_pressure_avg_depth_of_target_pass_pressure_fav',
'rec_scheme_penalties_rec_schem_dog',
'rec_depth_medium_pass_plays_rec_depth_dog',
'rec_depth_behind_los_route_rate_rec_depth_dog',
'rec_depth_right_behind_los_contested_catch_rate_rec_depth_dog',
'pass_depth_medium_scrambles_passdepth_fav',
'rec_depth_right_short_avoided_tackles_rec_depth_dog',
'pass_concept_screen_big_time_throws_pass_conc_dog',
'rec_depth_medium_yprr_rec_depth_fav',
'pass_depth_declined_penalties_passdepth_fav',
'rec_depth_right_behind_los_interceptions_rec_depth_dog',
'rec_concept_penalties_rec_concept_fav',
'rec_depth_right_behind_los_touchdowns_rec_depth_fav',
'pass_concept_penalties_pass_conc_dog',
'def_summary_snap_counts_dl_b_gap_def_cov_fav',
'pass_depth_behind_los_hit_as_threw_passdepth_dog',
'pass_depth_deep_sacks_passdepth_fav',
'pass_depth_behind_los_spikes_passdepth_fav',
'pass_depth_medium_touchdowns_passdepth_dog',
'pass_depth_short_scrambles_passdepth_dog',
'pass_depth_deep_bats_passdepth_fav',
'pass_concept_no_screen_grades_defense_penalty_pass_conc_fav',
'pass_depth_deep_hit_as_threw_passdepth_fav',
'pass_depth_medium_bats_passdepth_fav',
'def_coverage_summary_qb_rating_against_def_cov_summ_fav',
'pass_rush_snap_counts_pass_play_pass_rush_summ_dog',
'rec_depth_penalties_rec_depth_fav',
'pass_depth_behind_los_btt_rate_passdepth_dog',
'def_summary_pass_break_ups_def_stats_fav',
'rec_depth_behind_los_drop_rate_rec_depth_dog',
'rec_depth_penalties_rec_depth_dog',
'run_defense_grades_defense_run_def_summ_fav',
'pass_depth_behind_los_big_time_throws_passdepth_dog',
'pass_time_more_spikes_time_pocket_dog',
'run_defense_missed_tackle_rate_run_def_summ_fav',
'rec_concept_penalties_rec_concept_dog',
'pass_time_more_spikes_time_pocket_fav',
'pass_depth_deep_yards_passdepth_dog',
'rec_depth_left_behind_los_contested_catch_rate_rec_depth_fav',
'rec_depth_center_deep_avoided_tackles_rec_depth_dog',
'pass_depth_behind_los_big_time_throws_passdepth_fav',
'rec_depth_behind_los_caught_percent_rec_depth_fav',
'pass_depth_short_thrown_aways_passdepth_fav',
'rec_depth_left_deep_fumbles_rec_depth_fav',
'pass_depth_medium_sacks_passdepth_fav',
'rec_depth_right_deepavg_depth_of_target_rec_depth_fav',
'pass_depth_short_sack_percent_passdepth_dog',
'def_slot_coverage_interceptions_slot_cov_fav',
'rec_scheme_zone_yards_per_reception_rec_schem_dog',
'rec_depth_center_behind_los_pass_blocks_rec_depth_fav',
'pass_depth_deep_thrown_aways_passdepth_fav',
'pass_depth_medium_sack_percent_passdepth_dog',
'pass_depth_short_sack_percent_passdepth_fav',
'pass_concept_no_screen_grades_defense_pass_conc_fav',
'pass_depth_behind_los_thrown_aways_passdepth_dog',
'rec_depth_right_behind_los_contested_receptions_rec_depth_fav',
'pass_depth_deep_scrambles_passdepth_fav',
'def_summary_missed_tackles_def_stats_fav',
'rec_depth_left_behind_los_fumbles_rec_depth_dog',
'pass_depth_medium_scrambles_passdepth_dog',
'pass_depth_deep_hit_as_threw_passdepth_dog',
'rec_depth_deep_targets_percent_rec_depth_fav',
'pass_depth_behind_los_sack_percent_passdepth_dog',
'rec_depth_right_behind_los_contested_catch_rate_rec_depth_fav',
'pass_under_pressure_pressure_spikes_pass_pressure_fav',
'pass_depth_short_scrambles_passdepth_fav',
'rec_depth_short_receptions_rec_depth_dog',
'rec_depth_declined_penalties_rec_depth_fav',
'pass_concept_no_screen_grades_run_defense_pass_conc_fav',
'pass_concept_screen_hit_as_threw_pass_conc_fav',
'pass_depth_behind_los_scrambles_passdepth_fav',
'pass_depth_penalties_passdepth_fav',
'overall_performance_tgs_fav',
'punting_downeds_dog',
'rec_depth_left_behind_los_interceptions_rec_depth_dog',
'pass_concept_declined_penalties_pass_conc_dog',
'pass_depth_behind_los_pressure_to_sack_rate_passdepth_dog',
'rec_concept_screen_interceptions_rec_concept_fav',
'rec_depth_right_deepfumbles_rec_depth_dog',
'rec_depth_left_behind_los_contested_receptions_rec_depth_fav',
'rec_depth_center_behind_los_pass_block_rate_rec_depth_fav',
'pass_depth_short_completions_passdepth_dog',
'pass_under_pressure_no_pressure_hit_as_threw_pass_pressure_dog',
'pass_depth_behind_los_hit_as_threw_passdepth_fav',
'def_coverage_scheme_penalties_def_cov_schem_fav',
'pass_concept_no_screen_avg_depth_of_target_pass_conc_fav',
'pass_under_pressure_blitz_grades_defense_pass_pressure_dog',
'pass_under_pressure_blitz_grades_defense_pass_pressure_fav',
'pass_depth_medium_spikes_passdepth_dog',
'pass_under_pressure_pressure_grades_pass_route_pass_pressure_dog',
'rec_scheme_declined_penalties_rec_schem_dog',
'pass_concept_no_screen_grades_defense_penalty_pass_conc_dog',
'rec_depth_deep_avg_depth_of_target_rec_depth_fav',
'rec_depth_center_deep_grades_pass_route_rec_depth_dog',
'rec_depth_left_behind_los_contested_targets_rec_depth_fav',
'def_summary_total_pressures_def_cov_fav',
'def_summary_hits_passrush_dog',
'def_coverage_scheme_zone_snap_counts_pass_play_def_cov_schem_dog',
'pass_depth_behind_los_spikes_passdepth_dog',
'kicking_one_percent_dog',
'pass_under_pressure_no_pressure_grades_defense_pass_pressure_dog',
'pass_concept_no_screen_grades_run_defense_pass_conc_dog',
'rec_depth_right_medium_fumbles_rec_depth_fav',
'pass_depth_short_hit_as_threw_passdepth_fav',
'rec_concept_slot_fumbles_rec_concept_fav',
'pass_under_pressure_no_pressure_grades_defense_penalty_pass_pressure_dog',
'rec_depth_behind_los_caught_percent_rec_depth_dog',
'pass_depth_medium_pressure_to_sack_rate_passdepth_dog',
'def_coverage_scheme_zone_snap_counts_coverage_def_cov_schem_dog',
'rec_depth_right_deep_grades_pass_route_rec_depth_fav',
'rec_depth_right_behind_los_interceptions_rec_depth_fav',
'def_coverage_summary_snap_counts_pass_play_def_cov_summ_dog',
'pass_depth_behind_los_bats_passdepth_fav',
'kicking_total_attempts_fav',
'pressure_source_declined_penalties_pass_allow_pressure_dog',
'def_coverage_summary_yards_def_cov_summ_fav',
'pass_concept_penalties_pass_conc_fav',
'pass_depth_deep_sack_percent_passdepth_dog',
'pass_concept_screen_spikes_pass_conc_fav',
'rec_depth_left_deep_fumbles_rec_depth_dog',
'pass_depth_medium_pressure_to_sack_rate_passdepth_fav',
'pass_depth_deep_scrambles_passdepth_dog',
'pass_depth_medium_completions_passdepth_fav',
'pass_depth_short_bats_passdepth_fav',
'pass_under_pressure_no_pressure_def_gen_pressures_pass_pressure_dog',
'pass_depth_behind_los_sacks_passdepth_fav',
'def_summary_forced_fumbles_def_cov_dog',
'rec_depth_behind_los_grades_hands_drop_rec_depth_fav',
'pass_concept_screen_grades_offense_pass_conc_dog',
'pass_depth_short_avg_time_to_throw_passdepth_dog',
'pass_under_pressure_blitz_grades_defense_penalty_pass_pressure_dog',
'pass_under_pressure_no_blitz_pressure_to_sack_rate_pass_pressure_fav',
'defense_tgs_fav',
'pass_depth_short_spikes_passdepth_dog',
'pass_depth_medium_sack_percent_passdepth_fav',
'pass_depth_behind_los_thrown_aways_passdepth_fav',
'pass_depth_medium_thrown_aways_passdepth_fav',
'arm_length_rec_dog',
'pass_time_less_spikes_time_pocket_fav',
'pass_under_pressure_no_blitz_sacks_pass_pressure_fav',
'def_coverage_scheme_declined_penalties_def_cov_schem_fav',
'rec_scheme_declined_penalties_rec_schem_fav',
'rec_depth_right_short_grades_hands_drop_rec_depth_fav',
'rec_depth_center_behind_los_interceptions_rec_depth_fav',
'pass_depth_deep_sacks_passdepth_dog',
'pass_depth_medium_thrown_aways_passdepth_dog',
'def_summary_sacks_def_stats_fav',
'pass_depth_short_pressure_to_sack_rate_passdepth_dog',
'def_coverage_scheme_declined_penalties_def_cov_schem_dog',
'pass_depth_declined_penalties_passdepth_dog',
'pass_depth_short_thrown_aways_passdepth_dog',
'bench_passing_dog',
'run_defense_stop_percent_run_def_summ_fav',
'rec_depth_short_pass_blocks_rec_depth_dog',
'pass_under_pressure_pressure_spikes_pass_pressure_dog',
'pass_depth_deep_sack_percent_passdepth_fav',
'pass_depth_medium_hit_as_threw_passdepth_dog',
'pass_depth_medium_hit_as_threw_passdepth_fav',
'pass_rush_pass_rush_percent_pass_rush_summ_dog',
'rec_depth_left_behind_los_contested_catch_rate_rec_depth_dog',
'rec_depth_right_deeplongest_rec_depth_fav',
'pass_under_pressure_pressure_interceptions_pass_pressure_fav',
'pass_concept_screen_scrambles_pass_conc_fav',
'def_summary_forced_fumbles_def_cov_fav',
'pass_depth_short_spikes_passdepth_fav',
'def_summary_pass_break_ups_def_cov_dog',
'pass_depth_deep_bats_passdepth_dog',
'pass_depth_short_bats_passdepth_dog',
'pass_depth_behind_los_scrambles_passdepth_dog',
'def_summary_touchdowns_def_cov_dog',
'pass_depth_short_pressure_to_sack_rate_passdepth_fav',
'pressure_source_ce_percent_pass_allow_pressure_dog',
'rec_summary_yards_per_reception_rec_fav',
'shuttle_rush_fav',
'def_coverage_scheme_zone_targets_def_cov_schem_dog',
'pass_concept_screen_thrown_aways_pass_conc_dog',
'pass_time_avg_ttt_attempts_time_pocket_dog',
'kicking_thirty_made_fav',
'def_summary_interceptions_run_def_dog',
'pass_under_pressure_no_pressure_def_gen_pressures_pass_pressure_fav',
'def_summary_grades_defense_def_stats_fav',
'pass_depth_short_sacks_passdepth_dog',
'pass_depth_deep_pressure_to_sack_rate_passdepth_fav',
'rec_depth_right_behind_los_pass_blocks_rec_depth_fav',
'pressure_source_declined_penalties_pass_allow_pressure_fav',
'def_summary_pass_break_ups_def_cov_fav',
'pass_under_pressure_no_pressure_grades_defense_pass_pressure_fav',
'pass_concept_screen_spikes_pass_conc_dog',
'pass_under_pressure_no_pressure_sacks_pass_pressure_fav',
'pass_under_pressure_blitz_def_gen_pressures_pass_pressure_fav',
'rec_depth_right_deepcontested_receptions_rec_depth_fav',
'pass_under_pressure_blitz_grades_defense_penalty_pass_pressure_fav',
'rec_depth_center_deep_avoided_tackles_rec_depth_fav',
'rec_depth_right_behind_los_contested_receptions_rec_depth_dog',
'def_summary_penalties_def_cov_fav',
'def_coverage_scheme_zone_missed_tackle_rate_def_cov_schem_dog',
'kicking_twenty_percent_fav',
'pass_under_pressure_blitz_attempts_pass_pressure_dog',
'pass_under_pressure_blitz_interceptions_pass_pressure_fav',
'rec_depth_left_deep_yards_per_reception_rec_depth_fav',
'pass_under_pressure_no_pressure_grades_hands_fumble_pass_pressure_dog',
'pressure_source_other_percent_pass_allow_pressure_dog',
'def_coverage_scheme_base_snap_counts_coverage_def_cov_schem_dog',
'rec_concept_declined_penalties_rec_concept_fav',
'rec_depth_right_behind_los_pass_blocks_rec_depth_dog',
'def_summary_grades_defense_penalty_run_def_dog',
'pass_depth_deep_pressure_to_sack_rate_passdepth_dog',
'rec_scheme_man_yards_after_catch_per_reception_rec_schem_fav',
'pass_time_less_spikes_time_pocket_dog',
'pass_concept_no_screen_def_gen_pressures_pass_conc_dog',
'pressure_source_allowed_pressure_dropbacks_pass_allow_pressure_fav',
'rec_depth_left_behind_los_interceptions_rec_depth_fav',
'pass_under_pressure_blitz_grades_pass_pass_pressure_dog',
'def_summary_declined_penalties_def_cov_fav',
'rec_depth_deep_pass_block_rate_rec_depth_fav',
'rec_summary_grades_pass_block_rec_dog',
'rec_depth_deep_pass_blocks_rec_depth_fav',
'pressure_source_pressures_off_pass_allow_pressure_fav',
'rec_depth_short_drop_rate_rec_depth_dog',
'rush_summary_fumbles_rush_dog',
'block_summary_snap_counts_rg_block_fav',
'rec_concept_screen_caught_percent_rec_concept_dog',
'block_summary_snap_counts_te_block_fav',
'rush_summary_zone_attempts_rush_dog',
'rec_depth_left_deep_longest_rec_depth_fav',
'run_block_gap_run_block_percent_run_block_fav',
'pass_under_pressure_no_blitz_sack_percent_pass_pressure_fav',
'def_coverage_summary_missed_tackles_def_cov_summ_dog',
'pass_depth_medium_spikes_passdepth_fav',
'rec_depth_left_deep_pass_blocks_rec_depth_fav',
'def_coverage_summary_avg_depth_of_target_def_cov_summ_dog',
'rush_summary_rec_yards_rush_dog',
'pass_depth_short_first_downs_passdepth_dog',
'rec_depth_left_short_contested_catch_rate_rec_depth_fav',
'pass_under_pressure_pressure_avg_time_to_throw_pass_pressure_dog',
'pressure_source_sacks_allowed_pass_allow_pressure_fav',
'rec_scheme_zone_contested_targets_rec_schem_fav',
'rec_depth_left_short_avg_depth_of_target_rec_depth_dog',
'pass_time_less_hit_as_threw_time_pocket_fav',
'pass_depth_medium_yards_passdepth_fav',
'pass_concept_no_screen_touchdowns_pass_conc_dog',
'rec_depth_short_interceptions_rec_depth_fav',
'pass_under_pressure_pressure_completion_percent_pass_pressure_dog',
'run_defense_penalties_run_def_summ_dog',
'rec_summary_yards_after_catch_per_reception_rec_fav',
'pass_time_less_first_downs_time_pocket_fav',
'pass_under_pressure_no_pressure_btt_rate_pass_pressure_fav',
'def_slot_coverage_interceptions_slot_cov_dog',
'rec_depth_medium_drops_rec_depth_fav',
'def_summary_missed_tackle_rate_passrush_fav',
'def_coverage_scheme_zone_yards_per_reception_def_cov_schem_dog',
'def_summary_missed_tackles_def_cov_fav',
'rec_depth_right_deepyards_rec_depth_fav',
'pass_time_less_grades_offense_penalty_time_pocket_dog',
'pass_time_less_turnover_worthy_plays_time_pocket_fav',
'rec_depth_deep_fumbles_rec_depth_dog',
'explosive_passing_fav',
'pass_concept_screen_turnover_worthy_plays_pass_conc_fav',
'round_passing_dog',
'pass_summary_avg_time_to_throw_passing_dog',
'pass_under_pressure_no_pressure_grades_offense_penalty_pass_pressure_fav',
'pass_under_pressure_blitz_thrown_aways_pass_pressure_dog',
'def_summary_catch_rate_passrush_fav',
'rec_summary_drop_rate_rec_fav',
'def_summary_hurries_def_cov_dog',
'def_coverage_summary_yards_after_catch_def_cov_summ_fav',
'pass_under_pressure_blitz_pressure_to_sack_rate_pass_pressure_fav',
'pass_depth_behind_los_drops_passdepth_fav',
'off_pass_dvoa_dog',
'rec_depth_right_behind_los_fumbles_rec_depth_dog',
'rec_concept_slot_longest_rec_concept_dog',
'pressure_source_pressures_other_pass_allow_pressure_dog',
'pass_under_pressure_blitz_first_downs_pass_pressure_dog',
'kicking_thirty_percent_fav',
'pass_depth_deep_btt_rate_passdepth_fav',
'def_coverage_summary_coverage_snaps_per_reception_def_cov_summ_fav',
'pass_time_less_thrown_aways_time_pocket_fav',
'pass_concept_screen_thrown_aways_pass_conc_fav',
'rec_depth_right_deeppass_plays_rec_depth_dog',
'rec_depth_short_contested_receptions_rec_depth_fav',
'pass_time_avg_time_to_throw_time_pocket_dog',
'pass_rush_pass_rush_opp_pass_rush_summ_fav',
'rush_summary_grades_hands_fumble_rush_dog',
'run_defense_grades_run_defense_run_def_summ_fav',
'def_summary_snap_counts_dl_def_cov_dog',
'pressure_source_ol_te_percent_pass_allow_pressure_dog',
'rec_depth_medium_first_downs_rec_depth_dog',
'def_summary_penalties_passrush_fav',
'pass_under_pressure_pressure_grades_hands_drop_pass_pressure_fav',
'pass_depth_deep_interceptions_passdepth_dog',
'def_summary_batted_passes_def_cov_dog',
'pass_under_pressure_blitz_scrambles_pass_pressure_dog',
'pass_depth_short_grades_pass_passdepth_dog',
'def_coverage_scheme_zone_coverage_snaps_per_reception_def_cov_schem_dog',
'rec_depth_behind_los_contested_targets_rec_depth_fav',
'arm_length_passing_dog',
'pass_summary_declined_penalties_passing_fav',
'def_summary_pass_break_ups_def_stats_dog',
'run_block_snap_counts_run_play_run_block_fav',
'rec_concept_slot_grades_pass_route_rec_concept_dog',
'special_teams_tgs_dog',
'run_block_snap_counts_run_block_run_block_fav',
'rec_depth_medium_receptions_rec_depth_dog',
'pass_under_pressure_no_pressure_sack_percent_pass_pressure_fav',
'speed_clean_rush_fav',
'kicking_total_made_fav',
'rec_depth_right_short_drops_rec_depth_fav',
'rec_scheme_man_yards_per_reception_rec_schem_fav',
'rec_depth_right_medium_yards_per_reception_rec_depth_dog',
'selection_passing_dog',
'def_coverage_scheme_zone_dropped_ints_def_cov_schem_fav',
'pass_depth_short_avg_depth_of_target_passdepth_fav',
'pass_time_more_def_gen_pressures_time_pocket_dog',
'pass_depth_medium_avg_depth_of_target_passdepth_fav',
'pass_under_pressure_blitz_aimed_passes_pass_pressure_dog',
'rec_scheme_man_avoided_tackles_rec_schem_fav',
'def_summary_hits_def_cov_fav',
'inj_count_db_fav',
'inj_count_dl_fav',
'inj_count_hb_fav',
'inj_count_lb_fav',
'inj_count_ol_fav',
'inj_count_qb_fav',
'inj_count_te_fav',
'inj_count_wr_fav',
'inj_grade_db_fav',
'inj_grade_dl_fav',
'inj_grade_hb_fav',
'inj_grade_lb_fav',
'inj_grade_ol_fav',
'inj_grade_qb_fav',
'inj_grade_te_fav',
'inj_grade_wr_fav',
'inj_plays_db_fav',
'inj_plays_dl_fav',
'inj_plays_hb_fav',
'inj_plays_lb_fav',
'inj_plays_ol_fav',
'inj_plays_qb_fav',
'inj_plays_te_fav',
'inj_plays_wr_fav',
'inj_count_db_dog',
'inj_count_dl_dog',
'inj_count_hb_dog',
'inj_count_lb_dog',
'inj_count_ol_dog',
'inj_count_qb_dog',
'inj_count_te_dog',
'inj_count_wr_dog',
'inj_grade_db_dog',
'inj_grade_dl_dog',
'inj_grade_hb_dog',
'inj_grade_lb_dog',
'inj_grade_ol_dog',
'inj_grade_qb_dog',
'inj_grade_te_dog',
'inj_grade_wr_dog',
'inj_plays_db_dog',
'inj_plays_dl_dog',
'inj_plays_hb_dog',
'inj_plays_lb_dog',
'inj_plays_ol_dog',
'inj_plays_qb_dog',
'inj_plays_te_dog',
'inj_plays_wr_dog',

'spread_sqrd',
'spread_int_line',
'line',
'spread_abs',
'team_id','cover_int','schedule_week','schedule_season','spread_favorite','over_under_line','home_matchup_id']

df = df[cols]


df.fillna(df.median(), inplace=True)
df.drop_duplicates(inplace=True)

targ='cover_int'

df.replace(np.inf, .01, inplace=True)
df.replace(-np.inf, -.01, inplace=True)
df.replace(np.nan, 0, inplace=True)

df=df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
df.dropna(axis=1, how='all', inplace=True)

df = df[df['schedule_season'] >= begin_year]
df = df[df['schedule_week'] >= cutoff_week]
test = df[(df['schedule_season'] >= val_year_cutoff)]
#test = df[(df['schedule_season'] >= val_year_cutoff) & (df['schedule_week'] >= 10)]
test_10 = test[(test['schedule_season'] == 2022) & (test['schedule_week'] == cur_week)]
test=test[~test.index.isin(test_10.index)]

y_test = test[targ]

data_Model = df[~df.index.isin(test.index)]
data_Model = data_Model[~data_Model.index.isin(test_10.index)]
data_Model = data_Model[(data_Model['schedule_week'] >= 4)|(df['schedule_season'] < val_year_cutoff)]
y_train = data_Model[targ]










pred_cols = [x for x in data_Model.columns if x not in ['team_id','fav_cover','cover_int','score_home_fav','score_away_fav',
                                                        'unique_team_id_y','home_matchup_id']]
                                                        
                                                        
                                                        
X_train = data_Model[pred_cols]
X_test = test[pred_cols]
cur_test = test_10[pred_cols]
print(cur_test)

                                                        
pipe_lr = Pipeline([('scl', MinMaxScaler()),
#('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False))),
('pca', PCA(n_components=X_train.shape[1]-10)),
('clf', LogisticRegression(penalty='l1', C=.1, solver='liblinear',random_state=42))])

pipe_lr2 = Pipeline([#('scl', MinMaxScaler()),
('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False))),
#('pca', PCA(n_components=X_train.shape[1]-150)),
('clf', LogisticRegression(penalty='l2', C=.1, solver='liblinear',random_state=42))])

pipe_dt = Pipeline([('scl', MinMaxScaler()),
#('feature_selection', SelectFromModel(LinearSVC(penalty="l1",C=.1, dual=False))),
('pca', PCA(n_components=X_train.shape[1]-10)),
('clf', LogisticRegression(penalty='l1', C=.5, solver='liblinear',random_state=42))])

pipe_svm = Pipeline([('scl', MinMaxScaler()),
('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False))),
#('pca', PCA(n_components=X_train.shape[1]-150)),
('clf', svm.SVC(probability=True, C=10, gamma=.001, kernel='rbf', random_state=42))])

pipe_svm2 = Pipeline([('scl', MinMaxScaler()),
#('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False))),
('pca', PCA(n_components=X_train.shape[1]-10)),
('clf', svm.SVC(probability=True, C=100, gamma=.01, kernel='rbf', random_state=42))])

pipe_xgb = Pipeline([('scl', MinMaxScaler()),
('feature_selection', SelectFromModel(LinearSVC(penalty="l1", C=.1, dual=False))),
#('pca', PCA(n_components=X_train.shape[1]-20)),
('clf', XGBClassifier(n_estimators=700, random_state=42))])


pipe_rf= Pipeline([#('scl', MinMaxScaler()),
('feature_selection', SelectFromModel(LinearSVC(penalty="l1", C=1, dual=False))),
#('pca', PCA(n_components=X_train.shape[1]-50)),
#('clf', svm.SVC(probability=True, C=50, gamma=.1, kernel='rbf', random_state=42))])
('clf', RandomForestClassifier(n_estimators=700, n_jobs=4, random_state=42))])

pipe_gbm= Pipeline([#('scl', MinMaxScaler()),
('feature_selection', SelectFromModel(LinearSVC(penalty="l1", C=.01, dual=False))),
('clf', XGBClassifier(n_estimators=500, random_state=42))])

pipe_gbm2= Pipeline([#('scl', MinMaxScaler()),
('feature_selection', SelectFromModel(LinearSVC(penalty="l1", C=.1, dual=False))),
#('pca', PCA(n_components=X_train.shape[1]-25)),
('clf', GradientBoostingClassifier(n_estimators=700, learning_rate=.01, random_state=42))])


# List of pipelines for ease of iteration
pipelines = [pipe_lr, pipe_lr2, pipe_dt, pipe_svm, pipe_svm2, pipe_xgb, pipe_rf, pipe_gbm, pipe_gbm2]

# Dictionary of pipelines and classifier types for ease of reference
pipe_dict = {0:'LR', 1:'lr2', 2:'lr3', 3:'svm', 4:'svm2', 5:'xgb', 6:'rForest', 7:'gbm', 8:'gbm2'}

# Fit the pipelines
for pipe in pipelines:
    pipe.fit(X_train, y_train)

# Compare accuracies
for idx, val in enumerate(pipelines):
    print('%s pipeline test accuracy: %.3f' % (pipe_dict[idx], val.score(X_test, y_test)))


# Identify the most accurate model on test data
best_acc = 0.0
best_clf = 0
best_pipe = ''
for idx, val in enumerate(pipelines):
    if val.score(X_test, y_test) > best_acc:
        best_acc = val.score(X_test, y_test)
        best_pipe = val
        best_clf = idx
        
from logitboost import LogitBoost

  
lboost = LogitBoost(n_estimators=500, random_state=0, bootstrap=True, learning_rate=.5)
lboost.fit(X_train, y_train)
        
y_pred_train = lboost.predict(X_train)
y_pred_test = lboost.predict(X_test)

accuracy_train = accuracy_score(y_train, y_pred_train)
accuracy_test = accuracy_score(y_test, y_pred_test)

report_train = classification_report(y_train, y_pred_train)
report_test = classification_report(y_test, y_pred_test)
print('Training\n%s' % report_train)
print('Testing\n%s' % report_test)


from pyglmnet import GLM, simulate_glm
# create an instance of the GLM class
glm = GLM(distr='poisson', score_metric='pseudo_R2', reg_lambda=0.01)

# fit the model on the training data
glm.fit(np.array(X_train), np.array(y_train))

# predict using fitted model on the test data
yhat = glm.predict(np.array(X_test))

# score the model on test data
pseudo_R2 = glm.score(np.array(X_test), np.array(y_test))
print('Pseudo R^2 is %.3f' % pseudo_R2)



result = pd.DataFrame((pipe_lr).predict_proba(X_test))
resultlr = result[[0]]
resultlr.columns = ['lr_preds']

result = pd.DataFrame((pipe_lr2).predict_proba(X_test))
resultlr2 = result[[0]]
resultlr2.columns = ['lr2_preds']

result = pd.DataFrame((pipe_dt).predict_proba(X_test))
resultlr3 = result[[0]]
resultlr3.columns = ['lr3_preds']

result = pd.DataFrame((pipe_svm).predict_proba(X_test))
resultsvm = result[[0]]
resultsvm.columns = ['svm_preds']

result = pd.DataFrame((pipe_xgb).predict_proba(X_test))
resultdt = result[[0]]
resultdt.columns = ['xgb_preds']

result = pd.DataFrame((pipe_svm2).predict_proba(X_test))
resultsvm2 = result[[0]]
resultsvm2.columns = ['svm2_preds']

result = pd.DataFrame((pipe_rf).predict_proba(X_test))
resultrf = result[[0]]
resultrf.columns = ['rf_preds']

result = pd.DataFrame((pipe_gbm).predict_proba(X_test))
resultgbm = result[[0]]
resultgbm.columns = ['gbm_preds']

result = pd.DataFrame((pipe_gbm2).predict_proba(X_test))
resultgbm2 = result[[0]]
resultgbm2.columns = ['gbm2_preds']

result = pd.DataFrame((best_pipe).predict(X_test))
result.columns = ['preds']
result_proba = pd.DataFrame((best_pipe).predict_proba(X_test))
result_proba.columns = ['cover_prob','no_cover_prob']
X_test.reset_index(inplace=True, drop=True)
y_test.reset_index(inplace=True, drop=True)
test_ids = test[['team_id','home_matchup_id','schedule_week','schedule_season','spread_favorite','over_under_line']].reset_index(drop=True)
data_conc = pd.concat([y_test, result, result_proba, resultlr, resultlr2, resultlr3, resultsvm, resultsvm2, resultdt, resultrf, resultgbm, resultgbm2, test_ids], axis=1)
data_conc['ens'] = (data_conc['gbm_preds']+data_conc['rf_preds'])/2

#    result_lr_reg = pd.DataFrame((pipe_lr_reg).predict(cur_test2))
#    result_lr_reg.columns = ['reg_lr']
#    
#    result_svr_reg = pd.DataFrame((pipe_svr_reg).predict(cur_test2))
#    result_svr_reg.columns = ['reg_svr']

result = pd.DataFrame((pipe_lr).predict_proba(cur_test))
resultlr = result[[0]]
resultlr.columns = ['lr_preds']

result = pd.DataFrame((pipe_lr2).predict_proba(cur_test))
resultlr2 = result[[0]]
resultlr2.columns = ['lr2_preds']

result = pd.DataFrame((pipe_dt).predict_proba(cur_test))
resultlr3 = result[[0]]
resultlr3.columns = ['lr3_preds']

result = pd.DataFrame((pipe_svm).predict_proba(cur_test))
resultsvm = result[[0]]
resultsvm.columns = ['svm_preds']

result = pd.DataFrame((pipe_xgb).predict_proba(cur_test))
resultdt = result[[0]]
resultdt.columns = ['xgb_preds']

result = pd.DataFrame((pipe_svm2).predict_proba(cur_test))
resultsvm2 = result[[0]]
resultsvm2.columns = ['svm2_preds']

result = pd.DataFrame((pipe_rf).predict_proba(cur_test))
resultrf = result[[0]]
resultrf.columns = ['rf_preds']

result = pd.DataFrame((pipe_gbm).predict_proba(cur_test))
resultgbm = result[[0]]
resultgbm.columns = ['gbm_preds']

result = pd.DataFrame((pipe_gbm2).predict_proba(cur_test))
resultgbm2 = result[[0]]
resultgbm2.columns = ['gbm2_preds']

result = pd.DataFrame((best_pipe).predict(cur_test))
result.columns = ['preds']
result_proba = pd.DataFrame((best_pipe).predict_proba(cur_test))
result_proba.columns = ['cover_prob','no_cover_prob']
cur_test.reset_index(inplace=True, drop=True)

test_ids = test_10[['team_id','home_matchup_id','schedule_week','schedule_season','spread_favorite','over_under_line']].reset_index(drop=True)
data_conc_cur = pd.concat([result, result_proba, resultlr, resultlr2, resultlr3, resultsvm,resultsvm2, resultdt, resultrf, resultgbm, resultgbm2, test_ids], axis=1)
data_conc_cur.insert(0, 'fav_cover', 'unknown')
#data_conc_cur['actual'] = np.where(data_conc_cur['fav_cover'] == 'over', 1, 0)
data_conc_cur['ens'] = (data_conc_cur['xgb_preds']+data_conc_cur['gbm2_preds'])/2


import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import classification_report

data_conc_2022 = data_conc[data_conc['schedule_season'] == 2022]

def conf_matrix(y_true, y_pred,
                classes,
                normalize=False,
                title='Confusion matrix',
                cmap=plt.cm.Reds):
    """
    Mostly stolen from: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
    
    Normalization changed, classification_report stats added below plot
    """
    
    cm = confusion_matrix(y_true, y_pred)
    
    # Configure Confusion Matrix Plot Aesthetics (no text yet)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=14)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.ylabel('True label', fontsize=12)
    plt.xlabel('Predicted label', fontsize=12)
    
    # Calculate normalized values (so all cells sum to 1) if desired
    if normalize:
        cm = np.round(cm.astype('float') / cm.sum(),2) #(axis=1)[:, np.newaxis]
    
    # Place Numbers as Text on Confusion Matrix Plot
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black",
                 fontsize=12)
    
    
    # Add Precision, Recall, F-1 Score as Captions Below Plot
    rpt = classification_report(y_true, y_pred)
    rpt = rpt.replace('avg / total', '      avg')
    rpt = rpt.replace('support', 'N Obs')
    
    plt.annotate(rpt,
                 xy = (0,-0.3),
                 xytext = (-50, -140),
                 xycoords='axes fraction', textcoords='offset points',
                 fontsize=12, ha='left')    
    
    # Plot
    plt.tight_layout()
    
data_conc_2022['preds']=data_conc_2022['preds'].astype(str)
data_conc_2022['cover_int']=data_conc_2022['cover_int'].astype(str)
conf_matrix(data_conc_2022['cover_int'], data_conc_2022['preds'], classes=['cover','no cover'], normalize=False, title='Conf_Matrix')

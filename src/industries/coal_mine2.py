from industry import IndustrySecondary, TileLocationCheck

spritelayout sprlay_iron_mine_00 {ground{sprite:2325;}}
spritelayout sprlay_iron_mine_01 {ground{sprite:2326;}}
spritelayout sprlay_iron_mine_02 {ground{sprite:2327;}}
spritelayout sprlay_iron_mine_03 {ground{sprite:2328;}}

spritelayout sprlay_iron_mine_10 {ground{sprite:2329;}}
spritelayout sprlay_iron_mine_11 {ground{sprite:2330;}}
spritelayout sprlay_iron_mine_12 {ground{sprite:2331;}}
spritelayout sprlay_iron_mine_13 {ground{sprite:2332;}}

spritelayout sprlay_iron_mine_20 {ground{sprite:2333;}}
spritelayout sprlay_iron_mine_21 {ground{sprite:2334;}}
spritelayout sprlay_iron_mine_22 {ground{sprite:2335;}}
spritelayout sprlay_iron_mine_23 {ground{sprite:2336;}}

spritelayout sprlay_iron_mine_30 {ground{sprite:2337;}}
spritelayout sprlay_iron_mine_31 {ground{sprite:2338;}}
spritelayout sprlay_iron_mine_32 {ground{sprite:2339;}}
spritelayout sprlay_iron_mine_33 {ground{sprite:2340;}}

item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_00) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_00;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_01) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_01;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_02) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_02;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_03) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_03;}}

item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_10) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_10;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_11) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_11;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_12) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_12;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_13) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_13;}}

item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_20) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_20;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_21) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_21;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_22) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_22;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_23) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_23;}}

item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_30) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_30;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_31) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_31;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_32) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_32;}}
item (FEAT_INDUSTRYTILES, ind_tile_iron_mine_33) {
property {substitute:	02; accepted_cargos: [[PASS, 8]];}
graphics {default:		sprlay_iron_mine_33;}}

tilelayout industry_layout_iron_mine {
	0,0:	ind_tile_iron_mine_00;	0,1:	ind_tile_iron_mine_01;	0,2:	ind_tile_iron_mine_02;	0,3:	ind_tile_iron_mine_03;
	1,0:	ind_tile_iron_mine_10;	1,1:	ind_tile_iron_mine_11;	1,2:	ind_tile_iron_mine_12;	1,3:	ind_tile_iron_mine_13;
	2,0:	ind_tile_iron_mine_20;	2,1:	ind_tile_iron_mine_21;	2,2:	ind_tile_iron_mine_22;	2,3:	ind_tile_iron_mine_23;
	3,0:	ind_tile_iron_mine_30;	3,1:	ind_tile_iron_mine_31;	3,2:	ind_tile_iron_mine_32;	3,3:	ind_tile_iron_mine_33;
}
industry = IndustryPrimaryExtractive(
    id="coal_mine2",
    prod_cargo_types_with_multipliers=[("COAL", 20)],
    prob_in_game="4",
    prob_map_gen="10",
    map_colour="1",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.75",
    name="TTD_STR_INDUSTRY_NAME_COAL_MINE",
    nearby_station_name="string(STR_STATION_COLLIERY)",
    fund_cost_multiplier="252",
    pollution_and_squalor_factor=1,
)


industry.economy_variations["BASIC_TEMPERATE"].enabled = True
industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].prob_map_gen = "10"

# industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True

}

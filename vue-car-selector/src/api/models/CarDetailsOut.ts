/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { CarBodyModelOut } from './CarBodyModelOut';
import type { CarImageOut } from './CarImageOut';
import type { CarsStats } from './CarsStats';
import type { ModelDetailsOut } from './ModelDetailsOut';

export type CarDetailsOut = {
    id?: string;
    model: ModelDetailsOut;
    name: string;
    badge?: string;
    body: CarBodyModelOut;
    doors?: number;
    seats?: number;
    transmission?: string;
    gears?: number;
    drive?: number;
    engine_location?: string;
    engine_size?: number;
    engine_configuration?: string;
    cylinders?: number;
    power_kw?: number;
    power_hp?: number;
    power_rpm?: string;
    torque_nm?: number;
    torque_rpm?: string;
    acceleration?: number;
    top_speed?: number;
    fuel_type?: number;
    fuel_capacity?: number;
    fuel_combined?: number;
    fuel_urban?: number;
    fuel_average_distance?: number;
    electric_range?: number;
    charging_time?: number;
    fast_charging_time?: number;
    fast_charging_max_kw?: number;
    max_fuel_distance?: number;
    min_fuel_distance?: number;
    length?: number;
    width?: number;
    height?: number;
    wheelbase?: number;
    tare_mass?: number;
    ground_clearance?: number;
    min_boot_space?: number;
    max_boot_space?: number;
    foldable_seats?: boolean;
    ancap?: number;
    warranty_years_au?: number;
    warranty_years_nz?: number;
    warranty_distance?: string;
    battery_warranty_years?: string;
    battery_warranty_distance?: string;
    compact?: boolean;
    medium?: boolean;
    large?: boolean;
    young_driver?: boolean;
    driver_23_45?: boolean;
    middle_aged_driver?: boolean;
    older_driver?: boolean;
    short_distance?: boolean;
    long_distance?: boolean;
    mixed_distance?: boolean;
    perfect_city_car?: boolean;
    solo_drive?: boolean;
    big_family?: boolean;
    occasionally_plus_one_adult?: boolean;
    regularly_plus_one_adult?: boolean;
    three_adults_back_seat?: boolean;
    children?: boolean;
    elderly_front_seat?: boolean;
    elderly_back_seat?: boolean;
    dogs?: boolean;
    flexible?: boolean;
    /**
     * percentage value (0-100)
     */
    safety_adult?: number;
    /**
     * percentage value (0-100)
     */
    safety_child?: number;
    /**
     * percentage value (0-100)
     */
    safety_road_user?: number;
    /**
     * percentage value (0-100)
     */
    safety_systems?: number;
    /**
     * range (1-10)
     */
    comfort?: number;
    /**
     * range (1-10)
     */
    practicality?: number;
    /**
     * range (1-10)
     */
    cabin?: number;
    /**
     * range (1-10)
     */
    style?: number;
    /**
     * range (1-10)
     */
    info_system?: number;
    /**
     * range (1-10)
     */
    sport_feel?: number;
    /**
     * range (1-10)
     */
    handling?: number;
    race_track?: number;
    light_off_road?: boolean;
    heavy_off_road?: boolean;
    all_drive?: boolean;
    first_time_drive?: boolean;
    tall_driver?: boolean;
    anna_cars?: boolean;
    anna_for_women?: boolean;
    price_au?: number;
    price_nz?: number;
    /**
     * Ready to publish?
     */
    ready?: boolean;
    /**
     * Data contains an error
     */
    error?: boolean;
    stats?: CarsStats;
    images?: Array<CarImageOut>;
};


/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { BudgetOut } from '../models/BudgetOut';
import type { CarBodyOut } from '../models/CarBodyOut';
import type { CarBrandOut } from '../models/CarBrandOut';
import type { CarDetailsOut } from '../models/CarDetailsOut';
import type { PaginatedResponseSchema_CarOut_ } from '../models/PaginatedResponseSchema_CarOut_';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class CarsService {

    /**
     * Send Feedback
     * @returns string OK
     * @throws ApiError
     */
    public static sendFeedback({
        feedback,
    }: {
        feedback: boolean,
    }): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/feedback/',
            query: {
                'feedback': feedback,
            },
        });
    }

    /**
     * Get Car Details
     * @returns CarDetailsOut OK
     * @throws ApiError
     */
    public static getCarDetails({
        carId,
    }: {
        carId: number,
    }): CancelablePromise<CarDetailsOut> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/cars/{car_id}',
            path: {
                'car_id': carId,
            },
        });
    }

    /**
     * Get Cars
     * @returns PaginatedResponseSchema_CarOut_ OK
     * @throws ApiError
     */
    public static getCars({
        annaForWomen,
        youngDriver,
        driver2345,
        middleAgedDriver,
        olderDriver,
        shortDistance,
        longDistance,
        mixedDistance,
        perfectCityCar,
        priceAuGte,
        priceAuLte,
        priceNzGte,
        priceNzLte,
        brandsIdIn,
        bodiesIdIn,
        compact,
        medium,
        large,
        petrol,
        diesel,
        phev,
        mhev,
        electric,
        twoDoors,
        fourDoors,
        seats,
        flexible,
        elderlyFrontSeat,
        children,
        regularlyPlusOneAdult,
        threeAdultsBackSeat,
        elderlyBackSeat,
        dogs,
        bootLte,
        bootGte,
        bootUte,
        fwd,
        rwd,
        awd,
        manual,
        automatic,
        comfort,
        overallStyle,
        min5YearsWarranty,
        practicalityCabin,
        premiumCabin,
        foldingBackSeats,
        highTechInfoSystem,
        adultSafe,
        childrenSafe,
        otherRoadUsersSafe,
        assistanceSystem,
        sportFeel,
        handlingDynamics,
        raceTrack,
        kmRangeGte,
        kmRangeLte,
        fuelEconomyGte,
        fuelEconomyLte,
        powerGte,
        accelerationLte,
        engineGte,
        page = 1,
        pageSize = 10,
    }: {
        annaForWomen?: boolean,
        youngDriver?: boolean,
        driver2345?: boolean,
        middleAgedDriver?: boolean,
        olderDriver?: boolean,
        shortDistance?: boolean,
        longDistance?: boolean,
        mixedDistance?: boolean,
        perfectCityCar?: boolean,
        priceAuGte?: number,
        priceAuLte?: number,
        priceNzGte?: number,
        priceNzLte?: number,
        brandsIdIn?: Array<number>,
        bodiesIdIn?: Array<number>,
        compact?: boolean,
        medium?: boolean,
        large?: boolean,
        petrol?: boolean,
        diesel?: boolean,
        phev?: boolean,
        mhev?: boolean,
        electric?: boolean,
        twoDoors?: boolean,
        fourDoors?: boolean,
        seats?: number,
        flexible?: boolean,
        elderlyFrontSeat?: boolean,
        children?: boolean,
        regularlyPlusOneAdult?: boolean,
        threeAdultsBackSeat?: boolean,
        elderlyBackSeat?: boolean,
        dogs?: boolean,
        bootLte?: number,
        bootGte?: number,
        bootUte?: boolean,
        fwd?: boolean,
        rwd?: boolean,
        awd?: boolean,
        manual?: boolean,
        automatic?: boolean,
        comfort?: boolean,
        overallStyle?: boolean,
        min5YearsWarranty?: boolean,
        practicalityCabin?: boolean,
        premiumCabin?: boolean,
        foldingBackSeats?: boolean,
        highTechInfoSystem?: boolean,
        adultSafe?: boolean,
        childrenSafe?: boolean,
        otherRoadUsersSafe?: boolean,
        assistanceSystem?: boolean,
        sportFeel?: boolean,
        handlingDynamics?: boolean,
        raceTrack?: boolean,
        kmRangeGte?: number,
        kmRangeLte?: number,
        fuelEconomyGte?: number,
        fuelEconomyLte?: number,
        powerGte?: number,
        accelerationLte?: number,
        engineGte?: number,
        page?: number,
        pageSize?: number,
    }): CancelablePromise<PaginatedResponseSchema_CarOut_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/cars',
            query: {
                'anna_for_women': annaForWomen,
                'young_driver': youngDriver,
                'driver_23_45': driver2345,
                'middle_aged_driver': middleAgedDriver,
                'older_driver': olderDriver,
                'short_distance': shortDistance,
                'long_distance': longDistance,
                'mixed_distance': mixedDistance,
                'perfect_city_car': perfectCityCar,
                'price_au__gte': priceAuGte,
                'price_au__lte': priceAuLte,
                'price_nz__gte': priceNzGte,
                'price_nz__lte': priceNzLte,
                'brands_id__in': brandsIdIn,
                'bodies_id__in': bodiesIdIn,
                'compact': compact,
                'medium': medium,
                'large': large,
                'petrol': petrol,
                'diesel': diesel,
                'phev': phev,
                'mhev': mhev,
                'electric': electric,
                'two_doors': twoDoors,
                'four_doors': fourDoors,
                'seats': seats,
                'flexible': flexible,
                'elderly_front_seat': elderlyFrontSeat,
                'children': children,
                'regularly_plus_one_adult': regularlyPlusOneAdult,
                'three_adults_back_seat': threeAdultsBackSeat,
                'elderly_back_seat': elderlyBackSeat,
                'dogs': dogs,
                'boot__lte': bootLte,
                'boot__gte': bootGte,
                'boot__ute': bootUte,
                'fwd': fwd,
                'rwd': rwd,
                'awd': awd,
                'manual': manual,
                'automatic': automatic,
                'comfort': comfort,
                'overall_style': overallStyle,
                'min_5_years_warranty': min5YearsWarranty,
                'practicality_cabin': practicalityCabin,
                'premium_cabin': premiumCabin,
                'folding_back_seats': foldingBackSeats,
                'high_tech_info_system': highTechInfoSystem,
                'adult_safe': adultSafe,
                'children_safe': childrenSafe,
                'other_road_users_safe': otherRoadUsersSafe,
                'assistance_system': assistanceSystem,
                'sport_feel': sportFeel,
                'handling_dynamics': handlingDynamics,
                'race_track': raceTrack,
                'km_range__gte': kmRangeGte,
                'km_range__lte': kmRangeLte,
                'fuel_economy__gte': fuelEconomyGte,
                'fuel_economy__lte': fuelEconomyLte,
                'power__gte': powerGte,
                'acceleration__lte': accelerationLte,
                'engine__gte': engineGte,
                'page': page,
                'page_size': pageSize,
            },
        });
    }

    /**
     * Get Brands
     * @returns CarBrandOut OK
     * @throws ApiError
     */
    public static getBrands(): CancelablePromise<Array<CarBrandOut>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/brands',
        });
    }

    /**
     * Get Bodies
     * @returns CarBodyOut OK
     * @throws ApiError
     */
    public static getBodies(): CancelablePromise<Array<CarBodyOut>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/bodies',
        });
    }

    /**
     * Get Budget
     * @returns BudgetOut OK
     * @throws ApiError
     */
    public static getBudget(): CancelablePromise<BudgetOut> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/budget',
        });
    }

}

import Vuex from 'vuex'

const store = new Vuex.Store({
    state: {
        tmp_models_list: [],
        base_media_url: '',
        page_number_models: 1,
        question_3: 0,
        question_10: 0,
        question_11: 0,
        question_12: 0,
        question_13: 0,
        query: {
            //question 1
            car_for_woman: false,
            car_for_man: false,
            //question 2
            young_driver: false,
            driver_23_45: false,
            middle_aged_driver: false,
            older_driver: false,
            //question 3
            short_distance: false,
            long_distance: false,
            mixed_distance: false,
            //question 4
            budget: 0,
            //question 5
            brands_list: [],
            //question 6
            bodies_list: [],
            //question 7
            compact: false,
            medium: false,
            large: false,
            //question 8
            fuel_type_list: [],
            //question 9
            solo_drive: false,
            big_family: false,
            occasionally_plus_one_adult: false,
            regularly_plus_one_adult: false,
            children: false,
            elderly_front_seat: false,
            elderly_back_seat: false,
            dogs: false,
            flexible: false,
            //question 10
            doors_2: false,
            doors_4: false,
            doors_unsure: false,
            doors_dosnt_matter: false,
            //question 13
            transmission_automatic: false,
            transmission_manual: false,
            transmission_dosnt_matter: false,
            //question 14
            engine_up_to_1: false,
            engine_1_2: false,
            engine_2_3: false,
            engine_bigger_then_3: false,
            engine_unsure: false,
            //question 15
            safety_adult:false,
            safety_child:false,
            safety_road_user:false,
            safety_systems:false,
            warranty_over_5_years:false,
            electric_range:false,
            goof_fuel_efficiency:false,
            very_goof_fuel_efficiency:false,
            comfort:false,
            practicality:false,
            cabin:false,
            style:false,
            info_system:false,
            sport_feel:false,
            handling:false,
            race_track:false,
            power_over_300:false,
            power_over_200:false,
            acceleration_under_5:false,
            acceleration_under_8:false,
            tall_driver:false,
            first_time_driver:false,
            folding_rear_seats:false,
        }
    },
})



export default store;
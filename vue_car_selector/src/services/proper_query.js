import store from "@/store";

let query_params = new URLSearchParams();
const DEFAULT_VALUE = '0'
const DEFAULT_VALUE_2 = '0'
function proper_query() {
    let query = store.state.query;
    query_params = new URLSearchParams();
    for (const [key, value] of Object.entries(query)) {
        if (value) {
            if (doors(key) || boot_size(key) || drive_type(key) || transmission_type(key) || engine_size(key)) {
                continue
            } else if (key === 'bodies_list') {
                value.forEach(item => {
                    query_params.append('bodies', item);
                })
            } else if (key === 'brands_list') {
                value.forEach(item => {
                    query_params.append('brands', item);
                })
            } else if (key === 'fuel_type_list') {
                value.forEach(item => {
                    query_params.append('fuel_type', item);
                })
            } else if (key === 'safety_adult') {
                query_params.append('safety_adult', DEFAULT_VALUE);
            } else if (key === 'safety_child') {
                query_params.append('safety_child', DEFAULT_VALUE);
            } else if (key === 'safety_road_user') {
                query_params.append('safety_road_user', DEFAULT_VALUE);
            } else if (key === 'safety_systems') {
                query_params.append('safety_systems', DEFAULT_VALUE);
            } else if (key === 'warranty_over_5_years') {
                query_params.append('warranty_years', '5');
            }  else if (key === 'goof_fuel_efficiency') {
                query_params.append('fuel_combined', '10');
            } else if (key === 'very_goof_fuel_efficiency') {
                query_params.append('fuel_combined', '7');
            } else if (key === 'comfort') {
                query_params.append('comfort', DEFAULT_VALUE_2);
            } else if (key === 'practicality') {
                query_params.append('practicality', DEFAULT_VALUE_2);
            } else if (key === 'cabin') {
                query_params.append('cabin', DEFAULT_VALUE_2);
            } else if (key === 'style') {
                query_params.append('style', DEFAULT_VALUE_2);
            } else if (key === 'info_system') {
                query_params.append('info_system', DEFAULT_VALUE_2);
            } else if (key === 'sport_feel') {
                query_params.append('sport_feel', DEFAULT_VALUE_2);
            } else if (key === 'handling') {
                query_params.append('handling', DEFAULT_VALUE_2);
            } else if (key === 'race_track') {
                query_params.append('race_track', DEFAULT_VALUE_2);
            } else if (key === 'power_over_300') {
                query_params.append('power_hp', '300');
            } else if (key === 'power_over_200') {
                query_params.append('power_hp', '200');
            } else if (key === 'acceleration_under_5') {
                query_params.append('acceleration', '5');
            } else if (key === 'acceleration_under_8') {
                query_params.append('acceleration', '8');
            } else {
                query_params.append(key, value.toString());
            }
        }
    }

    return query_params
}


function boot_size(name) {
    switch (name) {
        case 'boot_large':
            query_params.append('max_boot_space_min', '500')
            return true
        case 'boot_medium':
            query_params.append('max_boot_space_min', '300')
            query_params.append('max_boot_space_max', '500')
            return true
        case 'boot_small':
            query_params.append('max_boot_space_min', '200')
            query_params.append('max_boot_space_max', '300')
            return true
        case 'boot_x_small':
            query_params.append('max_boot_space_max', '200')
            return true
    }
    return false
}


function doors(name) {
    switch (name) {
        case 'doors_2':
            query_params.append('doors', '4')
            return true
        case 'doors_4':
            query_params.append('doors', '4')
            return true
        case 'doors_unsure':
            if (query_params.solo_drive || query_params.occasionally_plus_one_adult || query_params.elderly_front_seat) {
                query_params.append('doors', '2')
                return true
            } else {
                query_params.append('doors', '4')
                return true
            }
    }
    return false
}

function drive_type(name) {
    switch (name) {
        case 'drive_front':
            query_params.append('drive', 'front')
            return true
        case 'drive_rear':
            query_params.append('drive', 'rear')
            return true
        case 'drive_all_wheel':
            query_params.append('drive', 'all wheel')
            return true
    }
    return false
}

function transmission_type(name) {
    switch (name) {
        case 'transmission_automatic':
            query_params.append('transmission', 'manual')
            return true
        case 'transmission_manual':
            query_params.append('transmission', 'manual')
            return true
    }
    return false
}

function engine_size(name) {
    switch (name) {
        case 'engine_up_to_1':
            query_params.append('engine_size_max', '1000')
            return true
        case 'engine_1_2':
            query_params.append('engine_size_min', '1000')
            query_params.append('engine_size_max', '2000')
            return true
        case 'engine_2_3':
            query_params.append('engine_size_min', '2000')
            query_params.append('engine_size_max', '3000')
            return true
        case 'engine_bigger_then_3':
            query_params.append('engine_size_min', '3000')
            return true
    }
    return false
}


export default proper_query;
import os
import re
import traceback

import pandas as pd

from apps.cars.models import CarBrand, CarModel, Car, RaceTrackScale, FuelType, DriveType, \
    CarBody
from apps.importer.models import UploadDataInfo
from config.celery import app


@app.task
def add_cars_data_to_database(file_path, remove_file: bool = True):
    try:
        df = pd.read_excel(file_path, sheet_name=0)
        clear_df = df.dropna(subset=['ID', ]).fillna(0)
        add_brands_with_models(clear_df)
        add_cars_to_database(clear_df)
        if remove_file and os.path.isfile(file_path):
            os.remove(file_path)
        set_info_object(lenght=1, current=0, message=f'Done', status=UploadDataInfo.Status.FINISH)
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        set_info_object(lenght=1, current=0, message=traceback.format_exc(), status=UploadDataInfo.Status.ERROR)


def add_cars_to_database(clear_data):
    length = len(clear_data)
    for index, row in clear_data.iterrows():
        car_id = convert_value_to_int(row['ID'])
        if not car_id:
            return

        car, created = Car.objects.get_or_create(pk=car_id)
        try:
            car.name = row['NAMING']

            action_name = 'Adding' if created else 'Updating'
            set_info_object(lenght=length, current=(index + 1), message=f"{action_name} car ({car.name})...",
                            status=UploadDataInfo.Status.PROCESSING)

            car.model = get_car_model(row['MODEL'], row['MAKE'])
            car.body = get_car_body(row['BODY'])
            car.hot_hatch = convert_value_to_bool(row['SPORTSCAR      HOT HATCH (H)'])
            car.transmission = str(row['TRANSMISSION']).strip()
            car.drive = get_drivel_type(row['DRIVE'])
            car.engine_location = str(row['ENGINE LOCATION']).strip()
            car.engine_configuration = str(row['ENGINE CONFIGURATION']).strip()
            car.fuel_type = get_fuel_type(row['FUEL TYPE'])
            car.badge = str(row['BADGE']).strip()

            car.doors = convert_value_to_int(row['DOORS'])
            car.seats = convert_value_to_int(row['SEATS'])
            car.gears = convert_value_to_int(row['GEARS'])

            car.engine_size = convert_value_to_int(row['ENGINE SIZE'])
            car.cylinders = convert_value_to_int(row['CYLINDERS'])
            car.power_kw = convert_value_to_int(row['POWERkW'])
            car.power_hp = convert_value_to_int(row['POWERHP *1.341'])
            car.power_rpm = str(row['POWER (rpm)']).strip()
            car.torque_nm = convert_value_to_int(row['TORQUE Nm'])
            car.torque_rpm = str(row['TORQUE RPM']).strip()
            car.acceleration = convert_value_to_float(row['ACCELERATION 0-100 SEC'])
            car.top_speed = convert_value_to_int(row['TOP SPEED KM/H)'])
            car.fuel_capacity = convert_value_to_int(row['FUEL CAPACITY L'])
            car.fuel_combined = convert_value_to_float(row['FUEL COMBINED L/KM'])
            car.fuel_urban = convert_value_to_float(row['FUEL CITY       L/KM'])
            car.fuel_average_distance = convert_value_to_int(row['FUEL AVERAGE DISTANCE (KM)'])
            car.charging_time = convert_value_to_float(row['CHARGING TIME 0-100% 7.4 KW/in hours'])
            car.electric_range = convert_value_to_float(row['ELECTRIC RANGE KM'])
            car.fast_charging_time = convert_value_to_float(row['FASTCHARGE TIME 10-80%/in minutes'])
            car.fast_charging_max_kw = convert_value_to_float(row['FASTCHARGE POWER      MAX KW'])
            car.max_fuel_distance = convert_value_to_int(row['MAX FUEL DISTANCE KM'])
            car.min_fuel_distance = convert_value_to_int(row['MIN FUEL DISTANCE KM'])
            car.length = convert_value_to_int(row['LENGTH (MM)'])
            car.width = convert_value_to_int(row['WIDTH (MM)'])
            car.height = convert_value_to_int(row['HEIGHT (MM)'])
            car.wheelbase = convert_value_to_int(row['WHEELBASE (MM)'])
            car.tare_mass = convert_value_to_int(row['TARE MASS KG'])
            car.ground_clearance = convert_value_to_int(row['GROUND CLEARANCE (MM)'])
            car.min_boot_space = convert_value_to_int(row['MIN BOOT SPACE (L) '])
            car.max_boot_space = convert_value_to_int(row['MAX BOOT SPACE (L)'])
            car.foldable_seats = convert_value_to_bool(row['FOLDABLE SEATS'])

            car.ancap = convert_value_to_int(row['ANCAP “0”  to brak oceny '])

            warranty_years_au = convert_value_to_int(str(row['WARRANTY (YEARS)']).strip()[0])
            warranty_years_nz = convert_value_to_int(str(row['WARRANTY (YEARS)']).strip()[-2]) if len(
                str(row['WARRANTY (YEARS)']).strip()) > 1 else None

            car.warranty_years_au = warranty_years_au
            car.warranty_years_nz = warranty_years_nz
            car.warranty_distance = str(row['WARRANTY (KM)']).strip()

            price_au = re.sub("[^0-9]", "", str(row['AU PRICE']).strip())
            price_nz = re.sub("[^0-9]", "", str(row['NZ PRICE']).strip())
            car.price_au = int(price_au) if bool(row['AU']) and price_au else None
            car.price_nz = int(price_nz) if bool(row['NZ']) and price_nz else None

            car.error = False
            car.save()
        except Exception as e:
            tb = traceback.format_exc()
            print(tb)
            print(car.id)
            car.error = True
            car.save()


def get_car_body(value):
    str_value = str(value).strip()
    if str_value == 'TBC' or str_value == 'N/A':
        return None
    str_value = str_value.replace('/', ' / ')
    body, _ = CarBody.objects.get_or_create(name=str_value)
    return body


def get_drivel_type(value):
    str_value = str(value).strip()
    if str_value == 'All Wheel Drive':
        return DriveType.AWD
    elif str_value == 'Front Wheel Drive':
        return DriveType.FWD
    elif str_value == 'Rear Wheel Drive':
        return DriveType.RWD
    return None


def get_fuel_type(value):
    str_value = str(value).strip()
    if str_value == 'Petrol':
        return FuelType.PETROL
    elif str_value == 'Diesel':
        return FuelType.DIESEL
    elif str_value == 'Electric':
        return FuelType.ELECTRIC
    elif '(HEV)' in str_value:
        return FuelType.HEV
    elif '(PHEV)' in str_value:
        return FuelType.PHEV

    elif '(MHEV) Mild Hybrid Petrol' in str_value:
        return FuelType.MHEV_PETROL
    elif '(MHEV) Mild Hybrid Diesel' in str_value:
        return FuelType.MHEV_DIESEL
    return None


def convert_value_to_int(value):
    str_value = str(value).upper().strip()
    if str_value == 'TBC' or str_value == 'N/A':
        return None

    int_value = int(float(str_value))
    if int_value == 0:
        return None
    return int_value


def convert_value_to_bool(value):
    str_value = str(value).upper().strip()
    if str_value == 'TBC' or str_value == 'N/A':
        return None
    if str_value == '1':
        return True

    if str_value == '0':
        return False

    return bool(str_value)


def convert_value_to_float(value):
    str_value = str(value).upper().strip()
    if str_value == 'TBC' or str_value == 'N/A':
        return None

    float_value = float(str_value.replace('L/100KM', ''))
    if float_value == 0:
        return None

    return float_value


def get_car_model(model, brand):
    brand = get_car_brand(brand)
    model_name = str(model).strip()
    return CarModel.objects.get(brand=brand, name=model_name)


def get_car_brand(brand):
    brand_name = str(brand).strip()
    return CarBrand.objects.get(name=brand_name)


def add_brands_with_models(clear_data):
    length = len(clear_data)
    for index, row in enumerate(zip(clear_data['MAKE'], clear_data['MODEL'])):
        brand_name = str(row[0]).strip()
        model_name = str(row[1]).strip()
        brand, _ = CarBrand.objects.get_or_create(name=brand_name)
        CarModel.objects.get_or_create(brand=brand, name=model_name)
        set_info_object(lenght=length, current=(index + 1), message=f"Adding models ({brand_name} {model_name})...",
                        status=UploadDataInfo.Status.PROCESSING)


@app.task
def add_cars_parameters_data_to_database(file_path, remove_file: bool = True):
    try:
        df = pd.read_excel(file_path, sheet_name=2)

        clear_df = df.dropna(subset=['ID', ]).fillna(0)
        correct = add_parameters_to_database(clear_df)
        if not correct:
            set_info_object(lenght=1, current=0, message=f'Error: Invalid data in file',
                            status=UploadDataInfo.Status.FINISH)

        if remove_file and os.path.isfile(file_path):
            os.remove(file_path)

        if correct:
            set_info_object(lenght=1, current=0, message=f'Done', status=UploadDataInfo.Status.FINISH)
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        set_info_object(lenght=1, current=0, message=f'Error: {e}', status=UploadDataInfo.Status.ERROR)


def add_parameters_to_database(clear_data):
    """
    Columns:
                                  'ID',                        'NAMING',
                         'ANNA’S CARS',              'ANNA’S FOR WOMEN',
                               '16-23',                              60,
                    'PERFECT CITY CAR',                       'COMPACT',
                              'MEDIUM',                         'LARGE',
       'BIG FAMILY (MORE THAN 2 KIDS)',        '1 & 2 ADULTS BACK SEAT',
                  '3 ADULTS BACK SEAT',                      'CHILDREN',
                  'ELDERLY FRONT SEAT',             'ELDERLY BACK SEAT',
                                'DOGS',                      'FLEXIBLE',
                             'COMFORT',                  'PRACTICALITY',
                               'CABIN',                         'STYLE',
                         'INFO SYSTEM',                   'SPORTY FEEL',
                            'HANDLING',             'RACE TRACK -/+/++',
                      'LIGHT OFF ROAD',            'HEAVY     OFF ROAD',
                         'TALL DRIVER',             'FIRST TIME DRIVER',
                        'SAFETY ADULT',                  'SAFETY CHILD',
        'SAFETY PEDESTRIAN PROTECTION',                'SAFETY SYSTEMS'
    """
    length = len(clear_data)
    for index, row in clear_data.iterrows():
        car_id = row['ID']
        try:
            try:
                car = Car.objects.get(pk=car_id)
            except Car.DoesNotExist:
                continue

            set_info_object(lenght=length, current=(index + 1), message=f"Adding car parameters ({car.name})...",
                            status=UploadDataInfo.Status.PROCESSING)

            car.anna_cars = bool(row['ANNA’S CARS'])
            car.anna_for_women = bool(row['ANNA’S FOR WOMEN'])
            car.young_driver = bool(row['16-23'])
            car.older_driver = bool(row[60])
            car.perfect_city_car = bool(row['PERFECT CITY CAR'])
            car.compact = bool(row['COMPACT'])
            car.medium = bool(row['MEDIUM'])
            car.large = bool(row['LARGE'])
            car.big_family = bool(row['BIG FAMILY (MORE THAN 2 KIDS)'])
            car.regularly_plus_one_adult = bool(row['1 & 2 ADULTS BACK SEAT'])
            car.three_adults_back_seat = bool(row['3 ADULTS BACK SEAT'])
            car.children = bool(row['CHILDREN'])
            car.elderly_front_seat = bool(row['ELDERLY FRONT SEAT'])
            car.elderly_back_seat = bool(row['ELDERLY BACK SEAT'])
            car.dogs = bool(row['DOGS'])
            car.flexible = bool(row['FLEXIBLE'])
            car.comfort = convert_value_to_int(row['COMFORT'])
            car.practicality = convert_value_to_int(row['PRACTICALITY'])
            car.cabin = convert_value_to_int(row['CABIN'])
            car.style = convert_value_to_int(row['STYLE'])
            car.info_system = convert_value_to_int(row['INFO SYSTEM'])
            car.sport_feel = convert_value_to_int(row['SPORTY FEEL'])
            car.handling = convert_value_to_int(row['HANDLING'])
            car.race_track = get_race_track_scale(row['RACE TRACK -/+/++'])
            car.light_off_road = bool(row['LIGHT OFF ROAD'])
            car.heavy_off_road = bool(row['HEAVY     OFF ROAD'])
            car.tall_driver = bool(row['TALL DRIVER'])
            car.first_time_drive = bool(row['FIRST TIME DRIVER'])
            car.safety_adult = convert_value_to_int(row['SAFETY ADULT'])
            car.safety_child = convert_value_to_int(row['SAFETY CHILD'])
            car.safety_road_user = convert_value_to_int(row['SAFETY PEDESTRIAN PROTECTION'])
            car.safety_systems = convert_value_to_int(row['SAFETY SYSTEMS'])
            car.save()
        except Exception:
            tb = traceback.format_exc()
            print(tb)
            print(car_id)
            return False
    return True


def get_race_track_scale(race_tack_scale: str):
    if race_tack_scale == '-':
        return RaceTrackScale.NO

    elif race_tack_scale == '+':
        return RaceTrackScale.MEDIUM

    elif race_tack_scale == '++':
        return RaceTrackScale.YES

    else:
        return None


def set_info_object(lenght=0, current=0, message='', status: UploadDataInfo.Status = 1):
    info_obj, _ = UploadDataInfo.objects.get_or_create(pk=1)
    info_obj.all_items = lenght
    info_obj.current_item = current
    info_obj.message = message
    info_obj.status = status
    info_obj.save()

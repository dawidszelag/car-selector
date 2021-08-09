import os
import re
import traceback
import pandas as pd
from django.apps import apps
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from CarSelector.celery import app
from core.models import Car, CarModel, Market, CarOnTheMarket, UploadDataInfo, CarBrand, CarBody


@app.task
def add_cars_data_to_database(file_path):
    try:
        df = pd.read_excel(file_path, sheet_name='Database')
        clear_df = df.dropna(subset=['ID', ]).fillna(0)
        add_brands_with_models(clear_df)
        add_cars_to_database(clear_df)
        if os.path.isfile(file_path):
            os.remove(file_path)
        set_info_object(lenght=1, current=0, message=f'Done', status=1)
    except Exception as e:
        set_info_object(lenght=1, current=0, message=traceback.format_exc(), status=1)


def add_cars_to_database(clear_data):
    lenght = len(clear_data)
    au_market, _ = Market.objects.get_or_create(name='AU', currency='AUD')
    nz_market, _ = Market.objects.get_or_create(name='NZ', currency='NZD')
    for index, row in clear_data.iterrows():
        car, created = Car.objects.get_or_create(pk=int(row['ID']))
        try:
            car.name = row['NAMING'].split(' ', 1)[1] if row['NAMING'].split(' ')[0].isdigit() else row['NAMING']

            action_name = 'Adding' if created else 'Updating'
            set_info_object(lenght=lenght, current=(index + 1), message=f"{action_name} car ({car.name})...",
                            status=2)

            car.model = get_car_model(row['MODEL'], row['MAKE'])
            car.body = str(row['BODY']).strip()
            car.transmission = str(row['TRANSMISSION']).strip()
            car.drive = str(row['DRIVE']).strip()
            car.engine_location = str(row['ENGINE LOCATION']).strip()
            car.engine_configuration = str(row['ENGINE CONFIGURATION']).strip()
            car.fuel_type = str(row['FUEL TYPE']).strip()
            car.badge = str(row['BADGE']).strip()
            car.doors = int(float(str(row['DOORS'])))
            car.seats = int(float(str(row['SEATS'])))
            car.gears = int(float(str(row['GEARS'])))
            car.engine_size = int(float(row['ENGINE SIZE']))
            car.cylinders = int(float(row['CYLINDERS']))
            car.power_kw = str(row['POWER kW']).strip()
            car.power_hp = str(row['POWER HP *1.341']).strip()
            car.power_rpm = str(row['POWER (rpm)']).strip()
            car.torque_nm = str(row['TORQUE Nm']).strip()
            car.torque_rpm = str(row['TORQUE RPM']).strip()
            car.acceleration = str(row['ACCELERATION 0-100 SEC']).strip()
            car.top_speed = str(row['TOP SPEED KM/H']).strip()
            car.fuel_capacity = str(row['FUEL CAPACITY L']).strip()
            car.fuel_combined = str(row['FUEL COMBINED L/KM']).strip()
            car.fuel_urban = str(row['FUEL CITY L/KM']).strip()
            car.fuel_average_distance = str(row['FUEL AVERAGE DISTANCE (KM)']).strip()
            car.max_fuel_distance = str(row['MAX FUEL DISTANCE KM']).strip()
            car.min_fuel_distance = str(row['MIN FUEL DISTANCE KM']).strip()
            car.length = str(row['LENGTH (MM)']).strip()
            car.width = str(row['WIDTH (MM)']).strip()
            car.height = str(row['HEIGHT (MM)']).strip()
            car.wheelbase = str(row['WHEELBASE (MM)']).strip()
            car.tare_mass = str(row['TARE MASS KG']).strip()
            car.ground_clearance = str(row['GROUND CLEARANCE (MM)']).strip()
            car.min_boot_space = str(row['MIN BOOT SPACE (L) ']).strip()
            car.max_boot_space = str(row['MAX BOOT SPACE (L)']).strip()
            car.foldable_seats = bool(int(float(row['FOLDABLE SEATS'])))
            car.ancap = str(row['ANCAP']).strip()
            car.warranty_years = str(row['WARRANTY (YEARS)']).strip()
            car.warranty_distance = str(row['WARRANTY (KM)']).strip()

            try:
                price = re.sub("[^0-9]", "", str(row['AU PRICE']))
                print(f'{index} {price}')
                tmp_market, _ = CarOnTheMarket.objects.get_or_create(market=au_market, car=car)
                tmp_market.price = int(float(price)) if price != '' else 0
                tmp_market.save()
            except Exception as e:
                print(e)

            try:
                price = re.sub("[^0-9]", "", row['NZ PRICE'].strip())
                tmp_market, _ = CarOnTheMarket.objects.get_or_create(market=nz_market, car=car)
                tmp_market.price = int(float(price)) if price != '' else 0
                tmp_market.save()
            except:
                pass

            car.error = False
            car.save()
        except Exception as e:
            print(e)
            car.error = True
            car.save()


def get_car_model(model, brand):
    brand = get_car_brand(brand)
    model_name = str(model).strip()
    return CarModel.objects.get(brand=brand, name=model_name)


def get_car_brand(brand):
    brand_name = str(brand).strip()
    return CarBrand.objects.get(name=brand_name)


def add_brands_with_models(clear_data):
    lenght = len(clear_data)
    for index, row in enumerate(zip(clear_data['MAKE'], clear_data['MODEL'])):
        brand_name = str(row[0]).strip()
        model_name = str(row[1]).strip()
        brand, _ = CarBrand.objects.get_or_create(name=brand_name)
        CarModel.objects.get_or_create(brand=brand, name=model_name)
        set_info_object(lenght=lenght, current=(index + 1), message=f"Adding models ({brand_name} {model_name})...",
                        status=2)


@app.task
def add_cars_parameters_data_to_database(file_path):
    try:
        df = pd.read_excel(file_path, sheet_name='Database - Table 1')

        clear_df = df.dropna(subset=['ID', ]).fillna(0)
        correct = add_parameters_to_database(clear_df)
        if not correct:
            set_info_object(lenght=1, current=0, message=f'Error: Invalid data in file', status=1)

        if os.path.isfile(file_path):
            os.remove(file_path)

        if correct:
            set_info_object(lenght=1, current=0, message=f'Done', status=1)
    except Exception as e:
        set_info_object(lenght=1, current=0, message=f'Error: {e}', status=1)


def add_parameters_to_database(clear_data):
    lenght = len(clear_data)

    for index, row in clear_data.iterrows():
        try:

            if index > 100:
                break
            car = Car.objects.get(pk=int(row['ID']))
            set_info_object(lenght=lenght, current=(index + 1), message=f"Adding car parameters ({car.name})...",
                            status=2)

            car.anna_cars = row['ANNA’S CARS']
            car.anna_for_women = row['ANNA’S FOR WOMEN']
            car.anna_for_teens = row['ANNA’S FOR TEENS']
            car.young_driver = row['16-23']
            car.older_driver = row['60+']
            car.perfect_city_car = row['PERFECT CITY CAR']
            car.compact = row['COMPACT']
            car.medium = row['MEDIUM']
            car.large = row['LARGE']
            car.big_family = row['BIG FAMILY']
            car.regularly_plus_one_adult = row['REGULARLY 1+ ADULT']
            car.three_adults_back_seat = row['3 ADULTS BACK SEAT (comfortably long periods)']
            car.children = row['CHILDREN']
            car.elderly_front_seat = row['ELDERLY FRONT SEAT']
            car.elderly_back_seat = row['ELDERLY BACK SEAT']
            car.dogs = row['DOGS']
            car.flexible = row['FLEXIBLE']
            car.comfort = row['COMFORT']
            car.practicality = row['PRACTICALITY']
            car.style = row['STYLE']
            car.info_system = row['INFO SYSTEM']
            car.sport_feel = row['SPORTY FEEL']
            car.handling = row['HANDLING']
            car.race_track = row['RACE TRACK']
            car.light_off_road = row['LIGHT OFF ROAD']
            car.extreme_off_road = row['EXTREME OFF ROAD']
            car.tall_driver = row['TALL DRIVER']
            car.first_time_drive = row['FIRST TIME DRIVER']
            car.safety_adult = row['SAFETY ADULT']
            car.safety_child = row['SAFETY CHILD']
            car.safety_road_user = row['SAFETY PEDESTRIAN PROTECTION']
            car.safety_systems = row['SAFETY SYSTEMS']
            car.uber_recommendation = row['UBER RECOMMENDATION']
            car.save()
        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            return False
    return True


def set_info_object(lenght=0, current=0, message='', status=1):
    info_obj, _ = UploadDataInfo.objects.get_or_create(pk=1)
    info_obj.all_items = lenght
    info_obj.current_item = current
    info_obj.message = message
    info_obj.status = status
    info_obj.save()

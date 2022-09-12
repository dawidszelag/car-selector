import os
from pathlib import PosixPath

import pytest

from apps.cars.models import Car
from apps.importer.tasks import add_cars_parameters_data_to_database, add_cars_data_to_database


@pytest.fixture()
def cars_file_path():
    return PosixPath(os.path.dirname(os.path.abspath(__file__))) / 'files/DATABASE AU.xls'


@pytest.fixture()
def parameters_file_path():
    return PosixPath(os.path.dirname(os.path.abspath(__file__))) / 'files/RATINGS AU.xls'


def create_cars(number: int) -> list[Car]:
    cars = []
    for i in range(number):
        cars.append(Car(pk=i + 1))

    return Car.objects.bulk_create(cars)


@pytest.mark.django_db
def test_import_car_parameters(parameters_file_path):
    cars = create_cars(2000)

    add_cars_parameters_data_to_database(parameters_file_path, remove_file=False)

    first_car = cars[0]
    first_car.refresh_from_db()

    assert first_car.anna_cars
    assert not first_car.anna_for_women
    assert first_car.sport_feel == 7
    assert first_car.race_track == 2


@pytest.mark.django_db
def test_import_car(cars_file_path):
    add_cars_data_to_database(cars_file_path, remove_file=False)

    car = Car.objects.get(id=1)

    assert car.name == 'Abarth 595'
    assert car.model.name == '595'
    assert car.model.brand.name == 'Abarth'
    assert car.price_au is None
    assert car.price_nz == 34490
    assert car.body == 'Hatchback'

    car_2 = Car.objects.get(id=7)

    assert car_2.name == 'Alfa Romeo Giulia Quadrifoglio'
    assert car_2.model.name == 'Giulia'
    assert car_2.model.brand.name == 'Alfa Romeo'
    assert car_2.price_au == 148000
    assert car_2.price_nz == 139990
    assert car_2.body == 'Sedan'
    assert car_2.warranty_years_au == 3

    car_3 = Car.objects.get(id=27)

    assert car_3.warranty_years_au == 3
    assert car_3.warranty_years_nz == 5


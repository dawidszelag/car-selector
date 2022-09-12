from typing import List

from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ninja_extra import http_get, api_controller
from ninja import Query
from apps.cars.services.cars_services import CarOut, CarsService, CarsFilters, CarBrandOut, CarBodyOut, BudgetOut, \
    CarDetailsOut


@api_controller('/', tags=['Cars'])
class CarsApiController:

    def __init__(self):
        self.car_service = CarsService()

    @http_get('cars/{car_id}', response=CarDetailsOut, operation_id='get_car_details')
    def get_car_details(self, car_id: int):
        return self.car_service.get_car_details(car_id=car_id)

    @http_get('cars', response=PaginatedResponseSchema[CarOut], operation_id='get_cars')
    @paginate(PageNumberPaginationExtra, page_size=10)
    def get_cars(self, filters: CarsFilters = Query(...)):
        return self.car_service.get_cars(filters)

    @http_get('brands', response=List[CarBrandOut], operation_id='get_brands')
    def get_brands(self):
        return self.car_service.get_brands()

    @http_get('bodies', response=List[CarBodyOut], operation_id='get_bodies')
    def get_bodies(self):
        return self.car_service.get_bodies()

    @http_get('budget', response=BudgetOut, operation_id='get_budget')
    def get_budget(self):
        return self.car_service.get_budget()

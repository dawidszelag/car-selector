import os
from typing import List

from ninja import Schema, Field
from django.db.models import Max, F, Avg, Q, OuterRef, Subquery, FloatField
from ninja import ModelSchema
from pydantic.main import BaseModel

from apps.cars.models import Car, CarBrand, CarBody, FuelType, DriveType, RaceTrackScale, CarImage, CarModel


class CarsFilters(Schema):
    """"""
    anna_for_women: bool = None

    young_driver: bool = None
    driver_23_45: bool = None
    middle_aged_driver: bool = None
    older_driver: bool = None

    short_distance: bool = None
    long_distance: bool = None
    mixed_distance: bool = None
    perfect_city_car: bool = None

    price_au__gte: int = None
    price_au__lte: int = None
    price_nz__gte: int = None
    price_nz__lte: int = None

    brands_id__in: List[int] = None
    bodies_id__in: List[int] = None

    compact: bool = None
    medium: bool = None
    large: bool = None

    petrol: bool = None
    diesel: bool = None
    hev: bool = None
    phev: bool = None
    mhev_petrol: bool = None
    mhev_diesel: bool = None
    electric: bool = None

    two_doors: bool = None
    four_doors: bool = None

    seats: int = None

    flexible: bool = None
    elderly_front_seat: bool = None
    children: bool = None
    regularly_plus_one_adult: bool = None
    three_adults_back_seat: bool = None
    elderly_back_seat: bool = None
    dogs: bool = None

    boot__lte: int = None
    boot__gte: int = None
    boot__ute: bool = None

    fwd: bool = None
    rwd: bool = None
    awd: bool = None

    manual: bool = None
    automatic: bool = None

    comfort: bool = None
    overall_style: bool = None
    min_5_years_warranty: bool = None
    highest_safety_ratings: bool = None
    low_fuel_economy: bool = None

    practicality_cabin: bool = None
    premium_cabin: bool = None
    folding_back_seats: bool = None
    high_tech_info_system: bool = None
    adult_safe: bool = None
    children_safe: bool = None
    other_road_users_safe: bool = None
    assistance_system: bool = None
    sport_feel: bool = None
    handling_dynamics: bool = None
    race_track: bool = None
    race_track_plus: bool = None
    rapid_charging: bool = None
    light_off_road: bool = None
    heavy_off_road: bool = None
    tall_driver: bool = None
    first_time_drive: bool = None

    km_range__gte: int = None
    km_range__lte: int = None
    fuel_economy__gte: int = None
    fuel_economy__lte: int = None
    power__gte: int = None
    acceleration__lte: int = None
    engine__gte: float = None


class CarBrandOut(Schema):
    id: int
    name: str
    thumbnail: str = None


class CarBodyOut(Schema):
    id: int
    name: str
    thumbnail: str = None


class BudgetOut(Schema):
    min: int
    max: int


class BrandDetailsOut(ModelSchema):
    class Config:
        model = CarBrand
        model_fields = "__all__"


class ModelDetailsOut(ModelSchema):
    brand: BrandDetailsOut

    class Config:
        model = CarModel
        model_fields = "__all__"


class CarBodyModelOut(ModelSchema):
    class Config:
        model = CarBody
        model_fields = "__all__"


class CarImageOut(ModelSchema):
    class Config:
        model = CarImage
        model_fields = "__all__"


class CarListImageOut(ModelSchema):
    class Config:
        model = CarImage
        model_fields = ['image']


class CarsStats(BaseModel):
    max_fuel_range: float = None
    max_fuel_efficiency: float = None
    max_hybrid_range: float = None
    max_hybrid_charging_time: float = None
    max_electric_charging_time: float = None
    max_electric_fast_charging_time: float = None


class CarDetailsOut(ModelSchema):
    stats: CarsStats = None
    body: CarBodyModelOut
    model: ModelDetailsOut
    images: List[CarImageOut] = []

    class Config:
        objects = Car.objects
        model = Car
        model_fields = "__all__"


class CarOut(ModelSchema):
    thumbnail: str = None

    class Config:
        model = Car
        model_fields = ['id', 'name']


class CarsService:
    BASE_URL = os.environ.get("BACKEND_URL")

    @staticmethod
    def get_car_details(car_id: int) -> CarDetailsOut:
        car = Car.objects.get(id=car_id)
        car = CarDetailsOut.from_orm(car)
        car_stats = Car.objects.aggregate(
            max_fuel_range=Max('max_fuel_distance'),
            max_fuel_efficiency=Max('fuel_combined'),
            max_hybrid_range=Max('electric_range',
                                 filter=Q(fuel_type=FuelType.PHEV)),
            max_hybrid_charging_time=Max('charging_time',
                                         filter=Q(fuel_type=FuelType.PHEV)),
            max_electric_charging_time=Max('charging_time'),
            max_electric_fast_charging_time=Max('fast_charging_time'),
        )
        car.stats = car_stats
        return car

    @staticmethod
    def get_cars(filters: CarsFilters) -> List[CarOut]:
        """"""
        _filter = Q()
        _filter &= get_question_1_filter(filters)
        _filter &= get_question_2_filter(filters)
        _filter &= get_question_3_filter(filters)
        _filter &= get_question_4_filter(filters)
        _filter &= get_question_5_filter(filters)
        _filter &= get_question_6_filter(filters)
        _filter &= get_question_7_filter(filters)
        _filter &= get_question_8_filter(filters)
        _filter &= get_question_9_filter(filters)
        _filter &= get_question_10_filter(filters)
        _filter &= get_question_11_filter(filters)
        _filter &= get_question_12_filter(filters)
        _filter &= get_question_13_filter(filters)
        _filter &= get_question_14_filter(filters)
        _filter &= get_question_15_filter(filters)
        _filter &= get_question_15_2_filter(filters)

        images = CarImage.objects.filter(car_id=OuterRef("id"))
        return Car.objects.annotate(
            thumbnail=Subquery(images.values('image')[:1]),
            avr_safe_rating=Avg(
                F('safety_adult') + F('safety_child') + F('safety_road_user') + F('safety_systems'),
                output_field=FloatField()
            ) / 4
        ).filter(_filter).order_by('markets__price', '-avr_safe_rating', '-warranty_years_au', '-warranty_years_nz',
                                   'fuel_combined', '-comfort', '-practicality', '-min_boot_space', '-style',
                                   '-electric_range', '-fast_charging_time', )

    def get_brands(self) -> List[CarBrandOut]:
        return [CarBrandOut(id=brand.id,
                            name=brand.name,
                            thumbnail=self.BASE_URL + brand.image.url if brand.image else None)
                for brand in CarBrand.objects.all()]

    def get_bodies(self) -> List[CarBodyOut]:
        return [CarBodyOut(id=body.id,
                           name=body.name,
                           thumbnail=self.BASE_URL + body.image.url if body.image else None)
                for body in CarBody.objects.all()]

    @staticmethod
    def get_budget() -> BudgetOut:
        prices = Car.objects.aggregate(Max('price_au'),
                                       Max('price_nz'))

        if not prices:
            return BudgetOut(min=0, max=0)

        min_budget = 0
        max_budget = prices['price_au__max'] if prices['price_au__max'] and prices['price_au__max'] > prices[
            'price_nz__max'] else prices['price_nz__max']
        return BudgetOut(min=min_budget, max=max_budget)


def get_question_1_filter(filters: CarsFilters):
    question = Q()
    if filters.anna_for_women:
        question |= Q(anna_for_women=filters.anna_for_women)

    return question


def get_question_2_filter(filters: CarsFilters):
    question = Q()
    if filters.young_driver:
        question |= Q(young_driver=filters.young_driver)

    # if filters.driver_23_45:
    #     question |= Q(driver_23_45=filters.driver_23_45)
    #
    # if filters.middle_aged_driver:
    #     question |= Q(middle_aged_driver=filters.middle_aged_driver)

    if filters.older_driver:
        question |= Q(older_driver=filters.older_driver)

    return question


def get_question_3_filter(filters: CarsFilters):
    question = Q()
    if filters.short_distance:
        question |= ~Q(fuel_type=FuelType.DIESEL)

    if filters.long_distance:
        question |= ~Q(fuel_type=FuelType.ELECTRIC)

    if filters.perfect_city_car:
        question |= Q(perfect_city_car=filters.perfect_city_car)

    return question


def get_question_4_filter(filters: CarsFilters):
    if filters.price_au__gte is None \
            and filters.price_nz__gte is None \
            and filters.price_au__lte is None \
            and filters.price_nz__lte is None:
        return Q()

    question = Q(price_au__isnull=False) | Q(price_nz__isnull=False)
    if filters.price_au__gte is not None and filters.price_nz__gte is not None:
        question &= Q(Q(price_au__gte=filters.price_au__gte) | Q(price_nz__gte=filters.price_nz__gte))

    if filters.price_au__lte is not None and filters.price_nz__lte is not None:
        question &= Q(Q(price_au__lte=filters.price_au__lte) | Q(price_nz__lte=filters.price_nz__lte))

    return question


def get_question_5_filter(filters: CarsFilters):
    question = Q()
    if filters.brands_id__in:
        question = Q(model__brand__id__in=filters.brands_id__in)
    return question


def get_question_6_filter(filters: CarsFilters):
    question = Q()
    if filters.bodies_id__in:
        question = Q(body_id__in=filters.bodies_id__in)
    return question


def get_question_7_filter(filters: CarsFilters):
    question = Q()
    if filters.compact:
        question |= Q(compact=filters.compact)

    if filters.medium:
        question |= Q(medium=filters.medium)

    if filters.large:
        question |= Q(medium=filters.large)
    return question


def get_question_8_filter(filters: CarsFilters):
    question = Q()
    if filters.petrol:
        question |= Q(fuel_type=FuelType.PETROL)

    if filters.diesel:
        question |= Q(fuel_type=FuelType.DIESEL)

    if filters.electric:
        question |= Q(fuel_type=FuelType.ELECTRIC)

    if filters.hev:
        question |= Q(fuel_type=FuelType.HEV)

    if filters.phev:
        question |= Q(fuel_type=FuelType.PHEV)

    if filters.mhev_petrol:
        question |= Q(fuel_type=FuelType.MHEV_PETROL)

    if filters.mhev_diesel:
        question |= Q(fuel_type=FuelType.MHEV_DIESEL)

    return question


def get_question_9_filter(filters: CarsFilters):
    question = Q()
    if filters.two_doors:
        question |= Q(doors=2) | Q(doors=3)

    if filters.four_doors:
        question |= Q(doors=4) | Q(doors=5)

    return question


def get_question_10_filter(filters: CarsFilters):
    question = Q()
    if filters.seats:
        question = Q(seats__gte=filters.seats)

    return question


def get_question_11_filter(filters: CarsFilters):
    question = Q()
    if filters.flexible:
        question &= Q(flexible=filters.flexible)

    if filters.elderly_front_seat:
        question &= Q(elderly_front_seat=filters.elderly_front_seat)

    # question group
    if filters.children or filters.regularly_plus_one_adult or filters.three_adults_back_seat or filters.elderly_back_seat:
        sub_question = Q()
        if filters.children:
            sub_question |= Q(children=filters.children)

        if filters.regularly_plus_one_adult:
            sub_question |= Q(regularly_plus_one_adult=filters.regularly_plus_one_adult)

        if filters.three_adults_back_seat:
            sub_question |= Q(three_adults_back_seat=filters.three_adults_back_seat)

        if filters.elderly_back_seat:
            sub_question |= Q(elderly_back_seat=filters.elderly_back_seat)

        question &= sub_question

    if filters.dogs:
        question &= Q(dogs=filters.dogs)

    return question


def get_question_12_filter(filters: CarsFilters):
    question = Q()
    if filters.boot__lte:
        question &= Q(max_boot_space__lte=filters.boot__lte)

    if filters.boot__gte:
        question &= Q(min_boot_space__gte=filters.boot__gte)

    if filters.boot__ute:
        question &= Q(body__name__icontains='ute')

    return question


def get_question_13_filter(filters: CarsFilters):
    question = Q()
    if filters.fwd:
        question &= Q(drive=DriveType.FWD)

    if filters.rwd:
        question &= Q(drive=DriveType.RWD)

    if filters.awd:
        question &= Q(drive=DriveType.AWD)

    return question


def get_question_14_filter(filters: CarsFilters):
    question = Q()
    if filters.manual:
        question &= Q(transmission__icontains='manual')

    if filters.automatic:
        question &= Q(transmission__icontains='automa')

    return question


def get_question_15_filter(filters: CarsFilters):
    question = Q()
    DEFAULT_RATING = 5

    if filters.comfort:
        question &= Q(comfort__gte=DEFAULT_RATING)

    if filters.overall_style:
        question &= Q(style__gte=DEFAULT_RATING)

    if filters.min_5_years_warranty:
        question &= Q(warranty_years_au__gte=5)

    if filters.highest_safety_ratings:
        question &= Q(avr_safe_rating__gte=80)

    if filters.low_fuel_economy:
        question &= Q(fuel_combined__lte=8)

    if filters.premium_cabin:
        question &= Q(cabin__gte=5)

    if filters.folding_back_seats:
        question &= Q(foldable_seats=filters.folding_back_seats)

    if filters.high_tech_info_system:
        question &= Q(info_system__gte=DEFAULT_RATING)

    if filters.adult_safe:
        question &= Q(safety_adult__gte=80)

    if filters.children_safe:
        question &= Q(safety_child__gte=80)

    if filters.other_road_users_safe:
        question &= Q(safety_road_user__gte=80)

    if filters.assistance_system:
        question &= Q(safety_systems__gte=80)

    if filters.sport_feel:
        question &= Q(sport_feel__gte=5)

    if filters.handling_dynamics:
        question &= Q(handling__gte=5)

    if filters.race_track:
        question &= Q(Q(race_track=RaceTrackScale.YES) | Q(race_track=RaceTrackScale.MEDIUM))

    if filters.race_track_plus:
        question &= Q(race_track=RaceTrackScale.YES)

    if filters.rapid_charging:
        question &= Q(fast_charging_max_kw__gte=200)

    if filters.light_off_road:
        question &= Q(light_off_road=filters.light_off_road)

    if filters.heavy_off_road:
        question &= Q(heavy_off_road=filters.heavy_off_road)

    if filters.tall_driver:
        question &= Q(tall_driver=filters.tall_driver)

    if filters.first_time_drive:
        question &= Q(first_time_drive=filters.first_time_drive)

    return question


def get_question_15_2_filter(filters: CarsFilters):
    question = Q()

    if filters.km_range__gte:
        question &= Q(
            Q(fuel_average_distance__gte=filters.km_range__gte) | Q(electric_range__gte=filters.km_range__gte))

    if filters.km_range__lte:
        question &= Q(
            Q(fuel_average_distance__lte=filters.km_range__lte) | Q(electric_range__lte=filters.km_range__lte))

    if filters.fuel_economy__gte:
        question &= Q(fuel_combined__gte=filters.fuel_economy__gte)

    if filters.fuel_economy__lte:
        question &= Q(fuel_combined__lte=filters.fuel_economy__lte)

    if filters.power__gte:
        question &= Q(power_kw__gte=filters.power__gte)

    if filters.acceleration__lte:
        question &= Q(acceleration__lte=filters.acceleration__lte)

    if filters.engine__gte:
        question &= Q(engine_size__gte=filters.engine__gte * 1000)

    return question

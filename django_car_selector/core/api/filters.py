from django.db.models import Q
from django_filters import rest_framework as filters

from core.models import Car, CarBrand, CarOnTheMarket, CarBody

try:
    BRANDS = [(brand.pk, brand.name) for brand in CarBrand.objects.all()]
    BODIES = [(body.pk, body.name) for body in CarBody.objects.all()]
except:
    BRANDS = []
    BODIES = []

FUEL_TYPES = [(fuel_type['fuel_type'], fuel_type['fuel_type']) for fuel_type in
              Car.objects.order_by('fuel_type').values('fuel_type').distinct()]


class CarFilter(filters.FilterSet):
    brands = filters.MultipleChoiceFilter(
        method='filter_brand',
        choices=BRANDS,
    )
    bodies = filters.MultipleChoiceFilter(
        method='filter_body',
        choices=BODIES,
    )
    fuel_type = filters.MultipleChoiceFilter(
        method='filter_fuel_type',
        choices=FUEL_TYPES,
    )
    budget = filters.NumberFilter(method='filter_budget', )
    max_boot_space = filters.NumberFilter(lookup_expr='gte')
    drive = filters.CharFilter(lookup_expr='icontains')
    transmission = filters.CharFilter(lookup_expr='icontains')
    engine_size = filters.RangeFilter(lookup_expr='range')

    # question 15
    safety_adult = filters.NumberFilter(lookup_expr='gte')
    safety_child = filters.NumberFilter(lookup_expr='gte')
    safety_road_user = filters.NumberFilter(lookup_expr='gte')
    safety_systems = filters.NumberFilter(lookup_expr='gte')
    warranty_years = filters.NumberFilter(lookup_expr='gte')
    electric_range = filters.NumberFilter(lookup_expr='gte')
    fuel_combined = filters.NumberFilter(lookup_expr='lte')
    comfort = filters.NumberFilter(lookup_expr='gte')
    practicality = filters.NumberFilter(lookup_expr='gte')
    cabin = filters.NumberFilter(lookup_expr='gte')
    style = filters.NumberFilter(lookup_expr='gte')
    info_system = filters.NumberFilter(lookup_expr='gte')
    sport_feel = filters.NumberFilter(lookup_expr='gte')
    handling = filters.NumberFilter(lookup_expr='gte')
    race_track = filters.NumberFilter(lookup_expr='gte')
    power_hp = filters.NumberFilter(lookup_expr='gte')
    acceleration = filters.NumberFilter(lookup_expr='lte')

    def filter_budget(self, queryset, name, value):
        filter_b = Q()
        filter_b |= Q(markets__price__lte=int(value))
        filter_b &= Q(markets__market__name='AU')
        print(filter_b)
        return queryset.filter(
            filter_b
        )

    def filter_brand(self, queryset, name, value):
        filter_b = Q()
        for item in value:
            filter_b |= Q(model__brand=item)
        return queryset.filter(
            filter_b
        )

    def filter_body(self, queryset, name, value):
        filter_b = Q()
        for item in value:
            car_body = CarBody.objects.get(pk=item)
            filter_b |= Q(body__icontains=car_body.name)
        return queryset.filter(
            filter_b
        )

    def filter_fuel_type(self, queryset, name, value):
        filter_b = Q()
        for item in value:
            filter_b |= Q(fuel_type__icontains=item)
        return queryset.filter(
            filter_b
        )

    class Meta:
        fields = (
            'model',
            # question 1
            'car_for_woman',
            'car_for_man',
            # question 2
            'young_driver',
            'driver_23_45',
            'middle_aged_driver',
            'older_driver',
            # question 3
            'short_distance',
            'long_distance',
            'mixed_distance',
            # question 4
            'budget',
            # question 5
            'brands',
            # question 6
            'bodies',
            # question 7
            'compact',
            'medium',
            'large',
            # question 8
            'fuel_type',
            # question 9
            'solo_drive',
            'big_family',
            'occasionally_plus_one_adult',
            'regularly_plus_one_adult',
            'children',
            'elderly_front_seat',
            'elderly_back_seat',
            'dogs',
            'flexible',
            # question 10
            'doors',
            # question 11
            'max_boot_space',
            # question 12
            'drive',
            # question 13
            'transmission',
            # question 14
            'engine_size',
            # question 15
            'safety_adult',
            'safety_child',
            'safety_road_user',
            'safety_systems',
            'warranty_years',
            'electric_range',
            'fuel_combined',
            'comfort',
            'practicality',
            'cabin',
            'style',
            'info_system',
            'sport_feel',
            'handling',
            'race_track',
            'power_hp',
            'acceleration',
            'light_off_road',
            'extreme_off_road',
            'tall_driver',
            'first_time_drive',
            'foldable_seats',

        )
        model = Car

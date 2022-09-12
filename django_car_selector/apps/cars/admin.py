from django.contrib import admin

from apps.cars.models import CarOnTheMarket, CarImage, CarModel, CarBody, CarBrand, Car


def set_unready(queryset):
    for car in queryset:
        car.ready = False
        car.save()


set_unready.short_description = 'Set as "Not ready"'


def set_ready(queryset):
    for car in queryset:
        car.ready = True
        car.save()


set_ready.short_description = 'Set as "Ready"'


class CarGallery(admin.StackedInline):
    model = CarImage
    extra = 1
    verbose_name = 'Image'
    verbose_name_plural = 'Gallery'
    list_display = ('thumbnail',)
    readonly_fields = ('thumbnail',)


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'ready', 'error']
    search_fields = ('name',)
    actions = [set_unready, set_ready]
    list_filter = ('error', 'ready')
    inlines = (CarGallery,)
    list_per_page = 100

    fieldsets = [
        ('Properties',
         {'fields': [('compact', 'medium', 'large'), ('car_for_woman', 'car_for_man', 'young_driver', 'driver_23_45',
                                                      'middle_aged_driver', 'older_driver'),
                     ('short_distance', 'long_distance', 'mixed_distance'),
                     ('solo_drive', 'big_family', 'regularly_plus_one_adult', 'three_adults_back_seat', 'children',
                      'elderly_front_seat', 'elderly_back_seat',
                      'dogs', 'flexible'), ('safety_adult', 'safety_child', 'safety_road_user', 'safety_systems'),
                     'comfort',
                     'practicality', 'cabin', 'style', 'info_system', 'sport_feel', 'handling', 'race_track',
                     'light_off_road', 'heavy_off_road', 'all_drive', 'first_time_drive', 'tall_driver', 'anna_cars',
                     'anna_for_women', 'perfect_city_car']}),
        ('Metadata',
         {'fields': ['ready', 'error']}),
        ('Car info',
         {'fields': ['model', 'name', 'badge', 'body', 'doors', 'seats', 'transmission', 'gears',
                     'drive', ]}),
        ('Engine',
         {'fields': ['engine_location', 'engine_size', 'engine_configuration', 'cylinders', 'power_kw', 'power_hp',
                     'power_rpm', 'torque_rpm', 'acceleration', 'top_speed',
                     'fuel_type', 'fuel_capacity', 'fuel_combined', 'fuel_urban', 'fuel_average_distance',
                     'max_fuel_distance', 'min_fuel_distance', 'electric_range']}),
        ('Other',
         {'fields': [('length', 'width', 'height'), 'wheelbase', 'tare_mass', 'ground_clearance',
                     'min_boot_space', 'max_boot_space', 'foldable_seats',
                     'ancap', ('warranty_years_au', 'warranty_years_nz'), 'warranty_distance', 'battery_warranty_years',
                     'battery_warranty_distance']}),

    ]


class CarModelAdmin(admin.ModelAdmin):
    actions = [set_unready, set_ready]
    search_fields = ('name', 'brand__name')
    list_display = ['get_full_name']

    def get_full_name(self, obj):
        return obj


class CarBodyAdmin(admin.ModelAdmin):
    actions = [set_unready, set_ready]
    search_fields = ('name',)
    list_display = ['get_full_name']

    def get_full_name(self, obj):
        return obj


class CarBrandAdmin(admin.ModelAdmin):
    actions = [set_unready, set_ready]
    search_fields = ('name',)
    list_display = ['get_full_name']

    def get_full_name(self, obj):
        return obj


admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarBody, CarBodyAdmin)
admin.site.register(CarBrand, CarBrandAdmin)

admin.site.site_header = 'Auto selector'
admin.site.site_title = 'Auto selector'

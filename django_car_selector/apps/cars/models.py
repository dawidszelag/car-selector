from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html


class RaceTrackScale(models.IntegerChoices):
    NO = 1, 'No'
    MEDIUM = 2, 'Medium'
    YES = 3, 'Well'


class FuelType(models.IntegerChoices):
    PETROL = 1, 'Petrol'
    DIESEL = 2, 'Diesel'
    ELECTRIC = 3, 'Electric'
    HEV = 4, 'Hybrid petrol'
    PHEV = 5, 'Plug in Hybrid Petrol'
    MHEV_PETROL = 6, 'Mild Hybrid Petrol'
    MHEV_DIESEL = 7, 'Mild Hybrid Diesel'


class DriveType(models.IntegerChoices):
    AWD = 1, 'All Wheel Drive'
    FWD = 2, 'Front Wheel Drive'
    RWD = 3, 'Rear Wheel Drive'


class Feedback(models.Model):
    result = models.BooleanField(default=None)
    date = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    """
    Car model contains information about car
    """
    id = models.CharField(max_length=20, primary_key=True)

    # # Car base information
    model = models.ForeignKey("CarModel", related_name='car', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)
    badge = models.CharField(max_length=300, blank=True, null=True)
    body = models.ForeignKey('CarBody', on_delete=models.SET_NULL, blank=True, null=True)
    hot_hatch = models.BooleanField(default=None, null=True)
    doors = models.PositiveSmallIntegerField(null=True)
    seats = models.PositiveSmallIntegerField(null=True)
    transmission = models.CharField(max_length=300, blank=True, null=True)
    gears = models.PositiveIntegerField(null=True)
    drive = models.PositiveIntegerField(choices=DriveType.choices, blank=True, null=True)
    engine_location = models.CharField(max_length=300, blank=True, null=True)
    engine_size = models.PositiveSmallIntegerField(null=True)
    engine_configuration = models.CharField(max_length=300, blank=True, null=True)
    cylinders = models.PositiveSmallIntegerField(null=True)
    power_kw = models.PositiveIntegerField(verbose_name="Power (kW)", null=True)
    power_hp = models.PositiveIntegerField(verbose_name="Power (HP)", null=True, blank=True)
    power_rpm = models.CharField(max_length=100, verbose_name="Power (rpm)", null=True, blank=True)
    torque_nm = models.PositiveIntegerField(verbose_name="Power (Nm)", null=True, blank=True)
    torque_rpm = models.CharField(max_length=100, verbose_name="torque (rpm)", null=True, blank=True)
    acceleration = models.FloatField(verbose_name="Acceleration 0-100", null=True, blank=True)
    top_speed = models.PositiveSmallIntegerField(verbose_name="Top speed (KM/H)", null=True, blank=True)
    fuel_type = models.PositiveSmallIntegerField(choices=FuelType.choices, blank=True, null=True)
    fuel_capacity = models.PositiveIntegerField(verbose_name="Fuel capacity L", null=True, blank=True)
    fuel_combined = models.FloatField(verbose_name="Fuel combined (L/KM)", null=True, blank=True)
    fuel_urban = models.FloatField(verbose_name="Fuel urban (L/KM)", null=True, blank=True)
    fuel_average_distance = models.PositiveIntegerField(verbose_name="Fuel average distance (KM)", null=True,
                                                        blank=True)
    electric_range = models.PositiveIntegerField(verbose_name="Electric range (KM)", default=None, null=True,
                                                 blank=True)
    charging_time = models.FloatField(verbose_name="Charging time 0-100% 7.4 KW", null=True, blank=True)
    fast_charging_time = models.FloatField(verbose_name="Fastcharge time 10%-80%", null=True, blank=True)
    fast_charging_max_kw = models.FloatField(verbose_name="Fastcharge power max KW", null=True, blank=True)
    max_fuel_distance = models.PositiveIntegerField(verbose_name="Max fuel distance (KM)", null=True, blank=True)
    min_fuel_distance = models.PositiveIntegerField(verbose_name="Min fuel distance (KM)", null=True, blank=True)
    length = models.PositiveIntegerField(verbose_name="Length (MM)", null=True)
    width = models.PositiveIntegerField(verbose_name="Width (MM)", null=True)
    height = models.PositiveIntegerField(verbose_name="Height (MM)", null=True)
    wheelbase = models.PositiveIntegerField(verbose_name="Wheelbase (MM)", null=True)
    tare_mass = models.PositiveIntegerField(verbose_name="Tare mass (KG)", null=True)
    ground_clearance = models.PositiveIntegerField(verbose_name="Ground clearance (MM)", null=True)
    min_boot_space = models.PositiveIntegerField(verbose_name="Min boot space (L)", null=True, blank=True)
    max_boot_space = models.PositiveIntegerField(verbose_name="Max boot space (L)", null=True, blank=True)
    foldable_seats = models.BooleanField(default=None, null=True)
    ancap = models.PositiveIntegerField(null=True, verbose_name="ANCAP", blank=True)
    warranty_years_au = models.PositiveIntegerField(verbose_name="Warranty AU (Years)", null=True, blank=True)
    warranty_years_nz = models.PositiveIntegerField(verbose_name="Warranty NZ (Years)", null=True, blank=True)
    warranty_distance = models.CharField(max_length=100, verbose_name="Warranty AU (KM)", null=True, blank=True)
    battery_warranty_years = models.CharField(max_length=100, verbose_name="Battery warranty (Years)", null=True,
                                              blank=True)
    battery_warranty_distance = models.CharField(max_length=100, verbose_name="Battery warranty (KM)", null=True,
                                                 blank=True)

    # #  Properties
    compact = models.BooleanField(default=False)
    medium = models.BooleanField(default=False)
    large = models.BooleanField(default=False)

    # # Age group of the driver(s)
    young_driver = models.BooleanField(verbose_name="Young drivers (16-23)", default=False)
    driver_23_45 = models.BooleanField(verbose_name="Drivers (23-45)", default=False)
    middle_aged_driver = models.BooleanField(verbose_name="Middle aged drivers (45-60)", default=False)
    older_driver = models.BooleanField(verbose_name="Older drivers (60+)", default=False)

    # # Where will you drive?
    short_distance = models.BooleanField(verbose_name="Mainly local distance", default=False)
    long_distance = models.BooleanField(verbose_name="Long distance", default=False)
    mixed_distance = models.BooleanField(verbose_name="Mixed distance", default=False)
    perfect_city_car = models.BooleanField(verbose_name="Perfect city car", default=False)

    # # Who will be your passenger
    solo_drive = models.BooleanField(verbose_name="Solo drive", default=False)
    big_family = models.BooleanField(default=False)
    occasionally_plus_one_adult = models.BooleanField(verbose_name="Occasionally 1+ adult", default=False)
    regularly_plus_one_adult = models.BooleanField(verbose_name="Regularly 1+ adult", default=False)
    three_adults_back_seat = models.BooleanField(verbose_name="3 Adults back seat", default=False)

    children = models.BooleanField(default=False)
    elderly_front_seat = models.BooleanField(default=False)
    elderly_back_seat = models.BooleanField(default=False)
    dogs = models.BooleanField(default=False)
    flexible = models.BooleanField(default=False)

    safety_adult = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                                    help_text="percentage value (0-100)", blank=True, null=True)
    safety_child = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                                    help_text="percentage value (0-100)", blank=True, null=True)
    safety_road_user = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                                        help_text="percentage value (0-100)", blank=True, null=True)
    safety_systems = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                                      help_text="percentage value (0-100)", blank=True, null=True)
    comfort = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                               help_text="range (1-10)", blank=True, null=True)
    practicality = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                                    help_text="range (1-10)", blank=True, null=True)
    cabin = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                             help_text="range (1-10)", blank=True, null=True)
    style = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                             help_text="range (1-10)", blank=True, null=True)
    info_system = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                                   help_text="range (1-10)", blank=True, null=True)
    sport_feel = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                                  help_text="range (1-10)", blank=True, null=True)
    handling = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                                help_text="range (1-10)", blank=True, null=True)
    race_track = models.PositiveSmallIntegerField(choices=RaceTrackScale.choices, blank=True, null=True)

    light_off_road = models.BooleanField(default=False)
    heavy_off_road = models.BooleanField(default=False)
    all_drive = models.BooleanField(default=False)
    first_time_drive = models.BooleanField(default=False)
    tall_driver = models.BooleanField(verbose_name="Tall driver(s) - over 1.9 m", default=False)

    anna_cars = models.BooleanField(verbose_name="Anna's cars", default=False)
    anna_for_women = models.BooleanField(verbose_name="Anna's for women", default=False)

    # Pricing
    price_au = models.PositiveIntegerField(null=True, blank=True, verbose_name="Price AU")
    price_nz = models.PositiveIntegerField(null=True, blank=True, verbose_name="Price NZ")

    # metadata
    ready = models.BooleanField(default=False, help_text="Ready to publish?")
    error = models.BooleanField(default=False, help_text="Data contains an error")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


def get_next_order_value():
    try:
        car_body = CarBody.objects.all().order_by('-order').first()
        return car_body.order + 1
    except:
        return 1


class CarBody(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="body_images", blank=True)
    order = models.PositiveSmallIntegerField(default=get_next_order_value)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Car bodies'
        ordering = ('order', 'name',)


class CarBrand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="brand_images", null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="markets")
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="model_images", null=True)

    def __str__(self):
        return f'{self.brand} - {self.name}'

    class Meta:
        ordering = ('brand__name',)


class Market(models.Model):
    name = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'currency',)


class CarOnTheMarket(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="markets")
    market = models.ForeignKey(Market, related_name="cars", on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f"{self.car} ({self.market})"

    class Meta:
        unique_together = ('car', 'market',)


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car_images")

    class Meta:
        ordering = ["image",]

    def thumbnail(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" height="55px" /></a>')
        else:
            return '(None)'

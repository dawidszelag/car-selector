from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F
from django.utils.html import format_html


class Car(models.Model):
    """Car model contains information about car"""

    # # Car base information
    model = models.ForeignKey("CarModel", related_name='car', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)
    badge = models.CharField(max_length=300, blank=True, null=True)
    body = models.CharField(max_length=300, blank=True, null=True)
    doors = models.PositiveSmallIntegerField(null=True)
    seats = models.PositiveSmallIntegerField(null=True)
    transmission = models.CharField(max_length=300, blank=True, null=True)
    gears = models.PositiveIntegerField(null=True)
    drive = models.CharField(max_length=300, blank=True, null=True)
    engine_location = models.CharField(max_length=300, blank=True, null=True)
    engine_size = models.PositiveSmallIntegerField(null=True)
    engine_configuration = models.CharField(max_length=300, blank=True, null=True)
    cylinders = models.PositiveSmallIntegerField(null=True)
    power_kw = models.CharField(max_length=100, verbose_name="Power (kW)", null=True)
    power_hp = models.CharField(max_length=100, verbose_name="Power (HP)", null=True)
    power_rpm = models.CharField(max_length=100, verbose_name="Power (rpm)", null=True)
    torque_nm = models.CharField(max_length=100, verbose_name="Power (Nm)", null=True)
    torque_rpm = models.CharField(max_length=100, verbose_name="torque (rpm)", null=True)
    acceleration = models.CharField(max_length=100, verbose_name="Acceleration 0-100", null=True)
    top_speed = models.CharField(max_length=100, verbose_name="Top speed (KM/H)", null=True)
    fuel_type = models.CharField(max_length=300, blank=True, null=True)
    fuel_capacity = models.CharField(max_length=100, null=True)
    fuel_combined = models.CharField(max_length=100, verbose_name="Fuel combined (L/KM)", null=True)
    fuel_urban = models.CharField(max_length=100, verbose_name="Fuel urban (L/KM)", null=True)
    fuel_average_distance = models.CharField(max_length=100, verbose_name="Fuel average distance (KM)", null=True)
    electric_range = models.CharField(max_length=100, verbose_name="Electric range (KM)", default=0, null=True)
    max_fuel_distance = models.CharField(max_length=100, verbose_name="Max fuel distance (KM)", null=True)
    min_fuel_distance = models.CharField(max_length=100, verbose_name="Min fuel distance (KM)", null=True)
    length = models.CharField(max_length=100, verbose_name="Length (MM)", null=True)
    width = models.CharField(max_length=100, verbose_name="Width (MM)", null=True)
    height = models.CharField(max_length=100, verbose_name="Height (MM)", null=True)
    wheelbase = models.CharField(max_length=100, verbose_name="Wheelbase (MM)", null=True)
    tare_mass = models.CharField(max_length=100, verbose_name="Tare mass (KG)", null=True)
    ground_clearance = models.CharField(max_length=100, verbose_name="Ground clearance (MM)", null=True)
    min_boot_space = models.CharField(max_length=100, verbose_name="Min boot space (L)", null=True)
    max_boot_space = models.CharField(max_length=100, verbose_name="Max boot space (L)", null=True)
    foldable_seats = models.BooleanField(default=False)
    ancap = models.CharField(max_length=10, verbose_name="ANCAP")
    warranty_years = models.CharField(max_length=100, verbose_name="Warranty (Years)", null=True)
    warranty_distance = models.CharField(max_length=100, verbose_name="Warranty (KM)")
    battery_warranty_years = models.CharField(max_length=100, verbose_name="Battery warranty (Years)", null=True)
    battery_warranty_distance = models.CharField(max_length=100, verbose_name="Battery warranty (KM)", null=True)

    # #  Properties
    compact = models.BooleanField(default=False)
    medium = models.BooleanField(default=False)
    large = models.BooleanField(default=False)
    # # Gender(s) of the driver(s)
    car_for_woman = models.BooleanField(default=False)
    car_for_man = models.BooleanField(default=False)

    # # Age group of the driver(s)
    young_driver = models.BooleanField(verbose_name="Young drivers (16-23)", default=False)
    driver_23_45 = models.BooleanField(verbose_name="Drivers (23-45)", default=False)
    middle_aged_driver = models.BooleanField(verbose_name="Middle aged drivers (45-60)", default=False)
    older_driver = models.BooleanField(verbose_name="Older drivers (60+)", default=False)

    # # Where will you drive?
    short_distance = models.BooleanField(verbose_name="Mainly local distance", default=False)
    long_distance = models.BooleanField(verbose_name="Long distance", default=False)
    mixed_distance = models.BooleanField(verbose_name="Mixed distance", default=False)

    # # Who will be your passenger
    solo_drive = models.BooleanField(verbose_name="Solo drive", default=False)
    big_family = models.BooleanField(default=False)
    occasionally_plus_one_adult = models.BooleanField(verbose_name="Occasionally 1+ adult", default=False)
    regularly_plus_one_adult = models.BooleanField(verbose_name="Regularly 1+ adult", default=False)
    three_adults_back_seat = models.BooleanField(verbose_name="3 Adults back seat",
                                                 default=False)
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
    race_track = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                                  help_text="range (1-10)", blank=True, null=True)

    light_off_road = models.BooleanField(default=False)
    extreme_off_road = models.BooleanField(default=False)
    all_drive = models.BooleanField(default=False)
    first_time_drive = models.BooleanField(default=False)
    tall_driver = models.BooleanField(verbose_name="Tall driver(s) - over 1.9 m", default=False)

    uber_recommendation = models.BooleanField(default=False)
    anna_cars = models.BooleanField(verbose_name="Anna's cars", default=False)
    anna_for_women = models.BooleanField(verbose_name="Anna's for women", default=False)
    anna_for_teens = models.BooleanField(verbose_name="Anna's teens", default=False)
    perfect_city_car = models.BooleanField(verbose_name="Perfect city car", default=False)
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
    image = models.ImageField(upload_to="body_images")
    order = models.PositiveSmallIntegerField(default=get_next_order_value)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Car bodies'
        ordering = ('-name',)


class CarBrand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="brand_images", null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="markets")
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="model_images")

    def __str__(self):
        return f'{self.brand} - {self.name}'

    class Meta:
        ordering = ('-name',)


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

    def thumbnail(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" height="55px" /></a>')
        else:
            return '(None)'


class UploadDataInfo(models.Model):
    all_items = models.PositiveSmallIntegerField(default=0)
    current_item = models.PositiveSmallIntegerField(default=0)
    message = models.CharField(max_length=300)
    # 1 - finish. 2 - working, 3 - error
    status = models.PositiveSmallIntegerField(default=1)

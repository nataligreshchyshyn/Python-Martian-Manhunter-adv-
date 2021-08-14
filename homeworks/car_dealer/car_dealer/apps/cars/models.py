from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class Car(models.Model):
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    car_model = models.ForeignKey(
        'cars.CarModel',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    slug = models.SlugField(max_length=75)

    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True
    )
    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    engine_type = models.CharField(max_length=15)

    CLASS_A_plus = "A+"
    CLASS_A = "A"
    CLASS_B = "B"
    CLASS_C = "C"
    CLASS_D = "D"
    CLASS_E = "E"
    CLASS_F = "F"
    CLASS_G = "G"

    POLLUTANT_CHOICES = (
        (CLASS_A_plus, "class A+"),
        (CLASS_A, "class A"),
        (CLASS_B, "class B"),
        (CLASS_C, "class C"),
        (CLASS_D, "class D"),
        (CLASS_E, "class E"),
        (CLASS_F, "class F"),
        (CLASS_G, "class G"),
    )
    pollutant_class = models.CharField(
        max_length=10,
        choices=POLLUTANT_CHOICES,
        default=CLASS_G,
        blank=True
    )
    price = models.PositiveIntegerField()

    doors = models.PositiveIntegerField()
    capacity = models.IntegerField()
    gear_case = models.CharField(max_length=25)
    number = models.CharField(max_length=15, null=True)
    sitting_place = models.PositiveIntegerField()
    first_registration_date = models.DateTimeField()
    engine_power = models.IntegerField()
    category = models.ManyToManyField(
        'cars.Property',
        blank=True,
    )
    fuel_type = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    class Meta:
        app_label = 'cars'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.slug


class FuelType(models.Model):
    PETROL = 'Petrol'
    DIESEL = 'Diesel'
    LPG = 'Gas'
    BIOFUEL = 'Biofuel'
    HYBRID = 'Hybrid'
    ELECTRIC = 'Electric'

    FUEL_TYPE_CHOICES = (
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (BIOFUEL, 'Biofuel'),
        (LPG, 'Liquified Petroleum Gas'),
        (HYBRID, 'Plug-in Hybrid Electric Vehicle'),
        (ELECTRIC, 'Battery Electric Vehicle'),
    )

    fuel_type = models.CharField(
        max_length=50,
        choices=FUEL_TYPE_CHOICES,
        default=PETROL,
        blank=True,
    )

    class Meta:
        app_label = 'cars'
        verbose_name = 'Fuel type'
        verbose_name_plural = 'Fuel types'

    def __str__(self):
        return self.fuel_type


class Color(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        app_label = 'cars'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        app_label = 'cars'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=25, unique=True)
    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
        related_name='models',
    )

    class Meta:
        app_label = 'cars'
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name


class Picture(models.Model):
    url = models.ImageField(
        upload_to='pictures',
        blank=True,
    )
    position = models.CharField(max_length=15)
    metadata = models.JSONField(encoder=DjangoJSONEncoder)
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
        related_name='pictures',
    )

    class Meta:
        app_label = 'cars'
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class Property(models.Model):
    CAT_M_LIGHT = 'Category M light-duty'
    CAT_M_HEAVY = 'Category M heavy-duty'
    CAT_N = 'Category N'
    CAT_L = 'Category L'
    CAT_T = 'Category T'

    CATEGORY_CHOICES = (
        (CAT_M_LIGHT, 'Passenger cars and vans'),
        (CAT_M_HEAVY, 'Trucks, buses, and coaches'),
        (CAT_N, 'Vehicles carrying goods'),
        (CAT_L, '2- and 3-wheel vehicles and quadricycles'),
        (CAT_T, 'Agricultural and forestry tractors and their trailers')
    )

    category = models.CharField(
        max_length=250,
        choices=CATEGORY_CHOICES,
        default=CAT_M_LIGHT,
        blank=True
    )
    name = models.CharField(max_length=25)

    class Meta:
        app_label = 'cars'
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name

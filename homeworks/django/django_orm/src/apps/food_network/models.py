from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

USER_MODEL = get_user_model()


class Country(models.Model):
    iso_code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=75)
    capital = models.CharField(max_length=75, null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'Country - {self.name}'


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(
        'food_network.Country',
        to_field='iso_code',
        on_delete=models.CASCADE,
        related_name='cities',
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name} city'


class Restaurant(models.Model):
    name = models.CharField(max_length=75)
    location = models.ForeignKey(
        'food_network.City',
        on_delete=models.CASCADE,
        related_name='restaurants',
    )
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='restaurants',
    )
    phone = models.PositiveIntegerField(null=True, editable=True)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return f'{self.name} the restaurant'


class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    position = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    home_place = models.ForeignKey(
        'food_network.City',
        on_delete=models.CASCADE,
        related_name='citizens',
    )
    work_place = models.ForeignKey(
        'food_network.Restaurant',
        on_delete=models.CASCADE,
        related_name='workers',
    )

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return f'{self.position} - {self.first_name} {self.second_name}'


class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = ArrayField(
        models.CharField(max_length=25, blank=True),
    )
    description = models.TextField()
    price = models.PositiveIntegerField(editable=True)
    category = models.ManyToManyField(
        'food_network.Menu',
        related_name='dishes',
    )
    place = models.ManyToManyField(
        'food_network.Restaurant',
        related_name='dishes',
    )

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return f'{self.name}'


class Menu(models.Model):
    SUMMER = 'summer'
    AUTUMN = 'autumn'
    WINTER = 'winter'
    SPRING = 'spring'
    ALL_YEAR = 'year'
    SEASON_DISHES_CHOICES = [
        (SUMMER, 'Summer menu'),
        (AUTUMN, 'Autumn menu'),
        (WINTER, 'Winter menu'),
        (SPRING, 'Spring menu'),
        (ALL_YEAR, 'Regular menu'),
    ]

    season = models.CharField(
        max_length=15,
        choices=SEASON_DISHES_CHOICES,
        default=ALL_YEAR,
        blank=True
    )

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return f'{self.season}'

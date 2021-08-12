from django.db import models
from django.contrib.auth.models import User


class Dealer(User):

    title = models.CharField(max_length=255)
    city = models.ForeignKey(
        'car_showroom.City',
        on_delete=models.CASCADE,
        related_name='dealers'
    )

    class Meta:
        app_label = 'car_showroom'
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} from {self.city}, {self.city.country}'


class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.ForeignKey(
        'car_showroom.Country',
        on_delete=models.CASCADE,
        related_name='cities',
        null=True,
    )

    class Meta:
        app_label = 'car_showroom'
        verbose_name = 'City'
        verbose_name_plural = 'Cites'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=75)
    code = models.PositiveIntegerField()

    class Meta:
        app_label = 'car_showroom'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
        related_name='dealers'
    )
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='dealers',
    )

    class Meta:
        app_label = 'dealers'
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'

    def __str__(self):
        return f'{self.user} from {self.city}, {self.city.country}'


class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        related_name='cities',
        null=True,
    )

    class Meta:
        app_label = 'dealers'
        verbose_name = 'City'
        verbose_name_plural = 'Cites'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=75)
    code = models.PositiveIntegerField()

    class Meta:
        app_label = 'dealers'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


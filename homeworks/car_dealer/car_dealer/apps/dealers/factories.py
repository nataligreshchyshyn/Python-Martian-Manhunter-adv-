import factory
from .models import Dealer, City, Country


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = 'USA'
    code = 1


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = 'Detroit'
    country = factory.SubFactory(CountryFactory)


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dealer

    title = 'manager'
    city = factory.SubFactory(CityFactory)



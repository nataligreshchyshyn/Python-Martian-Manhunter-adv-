import factory

from car_dealer.car_showroom.factories import CarFactory
from car_dealer.car_showroom.models import Order


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    car = factory.SubFactory(CarFactory)
    status = 'waiting'
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda a: f'{a.first_name}.{a.last_name}@example.com'.lower())
    phone = '9700345897'
    message = 'This is an example of client message'

from datetime import datetime
import factory

from dealers.factories import DealerFactory
from .models import Car, Color, Brand, CarModel, Property


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color

    name = 'yellow'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = 'ford'


class CarModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarModel

    name = 'mustang'
    brand = factory.SubFactory(BrandFactory)


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    category = 'Category M light-duty'
    name = 'coupe'


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    color = factory.SubFactory(ColorFactory)
    car_model = factory.SubFactory(CarModelFactory)
    slug = 'ford_mustang'
    status = 'pending'
    dealer = factory.SubFactory(DealerFactory)
    engine_type = 'V8'
    pollutant_class = 'B'
    price = 80000
    fuel_type = 'Petrol'
    doors = 4
    capacity = 237
    gear_case = '6 Speed Automatic'
    sitting_place = 4
    first_registration_date = factory.LazyFunction(datetime.now)
    engine_power = 395

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for category in extracted:
                self.categories.add(category)

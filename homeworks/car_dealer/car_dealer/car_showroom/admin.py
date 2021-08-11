from django.contrib import admin
from car_showroom.models import Dealer, City, Country, Car, Color, Brand, CarModel, Picture, Property, Order, \
    NewsLetter


class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city')
    search_fields = ('title', )


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'color', 'engine_type', 'fuel_type', 'gear_case', 'price', 'status', )
    search_fields = ('car_model', 'category', 'status')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'car', 'status')
    search_fields = ('first_name', 'last_name', 'car', 'status')


admin.site.register(Dealer, DealerAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Car, CarAdmin)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Picture)
admin.site.register(Property)
admin.site.register(Order, OrderAdmin)
admin.site.register(NewsLetter)

from django.contrib import admin
from .models import Car, Color, Brand, CarModel, Picture, Property


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'color', 'engine_type', 'fuel_type', 'gear_case', 'price', 'status', )
    search_fields = ('car_model', 'category', 'status')


admin.site.register(Car, CarAdmin)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Picture)
admin.site.register(Property)

from django.contrib import admin

from apps.food_network.models import Country, City, Restaurant, Worker, Dish, Menu


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Restaurant)
admin.site.register(Worker)
admin.site.register(Dish)
admin.site.register(Menu)

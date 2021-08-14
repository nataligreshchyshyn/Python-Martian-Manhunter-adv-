from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'car', 'status')
    search_fields = ('first_name', 'last_name', 'car', 'status')


admin.site.register(Order, OrderAdmin)

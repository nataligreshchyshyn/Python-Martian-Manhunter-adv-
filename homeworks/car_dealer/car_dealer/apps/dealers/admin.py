from django.contrib import admin
from .models import Dealer, City, Country


class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city')
    search_fields = ('title', )


admin.site.register(Dealer, DealerAdmin)
admin.site.register(City)
admin.site.register(Country)

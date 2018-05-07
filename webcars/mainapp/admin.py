from django.contrib import admin
from mainapp.models import Car, CarMake

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'make', 'car_model', 'year', 'price')


admin.site.register(Car, CarAdmin)
admin.site.register(CarMake)
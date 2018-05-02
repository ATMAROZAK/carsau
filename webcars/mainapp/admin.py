from django.contrib import admin
from mainapp.models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'brand', 'car_model', 'year', 'price')


admin.site.register(Car, CarAdmin)
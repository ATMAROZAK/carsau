from mainapp.models import Car
import django_filters


class CarFilter(django_filters.FilterSet):
    make = django_filters.CharFilter(lookup_expr='icontains')
    car_model = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Car
        fields = ['make', 'car_model', 'year', 'price']


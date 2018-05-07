from mainapp.models import Car, CarMake
import django_filters
from mainapp.forms import CarSearchForm

class CarFilter(django_filters.FilterSet):
    #make = django_filters.CharFilter(lookup_expr='icontains', label="Make")
    make = django_filters.ModelChoiceFilter(queryset=CarMake.objects.all())
    car_model = django_filters.CharFilter(lookup_expr='icontains', label="Model")

    class Meta:
        model = Car
        form = CarSearchForm
        fields = ['make', 'car_model', 'year', 'price']

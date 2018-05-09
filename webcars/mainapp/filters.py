from mainapp.models import Car, CarMake, CarModel
import django_filters
#from mainapp.forms import CarSearchForm

class CarFilter(django_filters.FilterSet):
    #make = django_filters.CharFilter(lookup_expr='icontains', label="Make")
    #car_model = django_filters.CharFilter(lookup_expr='icontains', label="Model")
    make = django_filters.ModelChoiceFilter(queryset=CarMake.objects.all(), lookup_expr='icontains')
    car_model = django_filters.ModelChoiceFilter(queryset=CarModel.objects.all(), lookup_expr='icontains')

    #car_model = django_filters.ChoiceFilter(lookup_expr='icontains')

    class Meta:
        model = Car
       # form = CarSearchForm
        fields = ['make', 'car_model', 'year', 'price']

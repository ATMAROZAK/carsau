from django.shortcuts import render, HttpResponse
import random
from mainapp.models import Car, CarModel, CarMake
from django.contrib.auth.models import User
from mainapp.filters import CarFilter
from django.db.models import Q
from mainapp.forms import SimpleCarSearchForm, AdvancedCarSearch

# Create your views here.

def random_cars(request):
    brand = ['toyota', 'mazda', 'opel', 'audi', 'lexus', 'peugeot', 'bmw', 'citroen', 'volvo', 'suzuki', 'jeep',
             'cadillac', 'ford', 'fiat', 'dodge', 'mazda', 'mercedes-benz', 'nissan']

    car_model = ['model1', 'model2', 'model3', 'model4','model5', 'model6', 'model7', 'model8', 'model9', 'model10']

    body_type = ['']

    #owner = ['xu1la', 'Vadim']

    car_instances = []
    for x in range(1000):
        car_instances.append(Car(owner=User.objects.get(first_name="Vadim"),
                                    brand=random.choice(brand),
                                    car_model=random.choice(car_model),
                                    year=random.choice(range(1980, 2018)),
                                    price=random.choice(range(5000, 100000))))
    Car.objects.bulk_create(car_instances)

    return HttpResponse("<h1>COMPLETE</h1>")


def car_search(request):
    car_list = Car.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    return render(request, 'cars/index.html', {'filter' : car_filter})


def load_car_models(request):
    make = request.GET.get('make')
    print(make)
    if make is '':
        models = CarModel.objects.none()
    else:
        models = CarModel.objects.filter(make__make=make).order_by('car_model')
    return render(request, 'cars/model_dropdown_list_option.html', {'models': models})


def search(request):
    q_objects = Q()

    make = request.GET.get('make')
    if make:
        q_objects &= Q(make__icontains=make)

    car_model = request.GET.get('car_model')
    if car_model:
        q_objects &= Q(car_model__icontains=car_model)

    year = request.GET.get('year')
    if year:
        q_objects &= Q(year=int(year))

    price = request.GET.get('price')
    if price:
        q_objects &= Q(price=int(price))

    color = request.GET.get('color')
    if color:
        q_objects &= Q(color__icontains=color)

    queryset = Car.objects.filter(q_objects)
    form = AdvancedCarSearch(make=make, car_model=car_model, color=color)

    return render(request, 'search/carsearch.html', {'form': form,
                                                     'cars' : queryset})


def index(request):
    form = SimpleCarSearchForm()
    return render(request, 'cars/index.html', {'form': form})
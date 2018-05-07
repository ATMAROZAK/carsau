from django.shortcuts import render, HttpResponse
import random
from mainapp.models import Car
from django.contrib.auth.models import User
from mainapp.filters import CarFilter


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
from registration.forms import RegistrationFormUniqueEmail
from django import forms
from django.db.models import Max, Min
from django_filters import filterset
from mainapp.models import CarMake, CarModel, Car



class MyRegForm(RegistrationFormUniqueEmail):
    username = forms.CharField(max_length=254, required=False, widget=forms.HiddenInput())
    first_name = forms.CharField(max_length=20, required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        self.cleaned_data['username'] = email
        return email

    def save(self, commit=True):
        user = super(MyRegForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()

        return user
"""
class CarSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        FILTER_CHOICES = (
            ('Honda', 'Honda'),
            ('VAZ', 'VAZ'),
            ('assigned', 'Assigned'),
            ('reopened', 'Reopened'),
            ('closed', 'Closed'),
            ('', 'Any'),
        )
        super().__init__(*args, **kwargs)
        self.fields['make'].choices = FILTER_CHOICES"""

class SimpleCarSearchForm(forms.Form):

    YEAR_CHOICE = ([('', '--------')])
    YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(1980, 2019))))
    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), to_field_name="make")
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.none(), to_field_name="car_model")
    min_year = forms.ChoiceField(choices=YEAR_CHOICE)
    min_price = forms.IntegerField()
    max_price = forms.IntegerField()

class AdvancedCarSearch(forms.Form):
    YEAR_CHOICE = ([('', '--------')])
    YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(1980, 2019))))

    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), to_field_name="make")
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.none(), to_field_name="car_model")

    min_year = forms.ChoiceField(choices=YEAR_CHOICE)
    max_year = forms.ChoiceField(choices=YEAR_CHOICE)

    min_price = forms.IntegerField()
    max_price = forms.IntegerField()
    color = forms.CharField()

    def __init__(self, *args, **kwargs):
        YEAR_CHOICE = ([('', '--------')])


        """make = None
        if 'make' in kwargs:
            make = kwargs.pop('make')
            if make:
                car_start_year = Car.objects.filter(make__iexact=make).aggregate(Min('year'))['year__min']
                YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(car_start_year, 2019))))
        else:
            YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(1980, 2019))))

        car_model = None
        if 'car_model' in kwargs:
            car_model = kwargs.pop('car_model')
            if car_model:
                car_start_year = Car.objects.filter(car_model__iexact=car_model).aggregate(Min('year'))['year__min']
                YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(car_start_year, 2019))))"""

        make = None
        car_model = None
        if 'make' in kwargs and 'car_model' in kwargs: # Если в запросе есть make и car_model
            car_model = kwargs.pop('car_model')
            make = kwargs.pop('make')
            if car_model and make: #Если make и car_model содержат инфу то берем год по модели
                car_start_year = Car.objects.filter(car_model__iexact=car_model).aggregate(Min('year'))['year__min']
                YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(car_start_year, 2019))))
            elif not make and car_model: # Если нет марки но есть модель машины то год по модели
                car_start_year = Car.objects.filter(car_model__iexact=car_model).aggregate(Min('year'))['year__min']
                YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(car_start_year, 2019))))
            elif not car_model and make: #Если нет модели но есть марка то год по марке
                car_start_year = Car.objects.filter(make__iexact=make).aggregate(Min('year'))['year__min']
                YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(car_start_year, 2019))))
            else:
                YEAR_CHOICE.extend(((str(x), x) for x in reversed(range(1980, 2019))))

        color = None
        if 'color' in kwargs:
            color = kwargs.pop('color')

        min_year = None
        if 'min_year' in kwargs:
            min_year = kwargs.pop('min_year')

        max_year = None
        if 'max_year' in kwargs:
            max_year = kwargs.pop('max_year')

        min_price = None
        if 'min_price' in kwargs:
            min_price = kwargs.pop('min_price')

        max_price = None
        if 'max_price' in kwargs:
            max_price = kwargs.pop('max_price')

        super(AdvancedCarSearch, self).__init__(*args, **kwargs)

        if make:
            self.fields['make'].initial = CarMake.objects.get(make=make)
            self.fields['car_model'].queryset = CarModel.objects.filter(make__make=make)

        if car_model:
            self.fields['car_model'].initial = CarModel.objects.get(car_model=car_model)

        if min_year:
            self.fields['min_year'].initial = min_year

        if max_year:
            self.fields['max_year'].initial = max_year

        self.fields['min_year'].choices = YEAR_CHOICE
        self.fields['max_year'].choices = YEAR_CHOICE

        if min_price:
            self.fields['min_price'].initial = min_price

        if max_price:
            self.fields['max_price'].initial = max_price

        if color:
            self.fields['color'].initial = color

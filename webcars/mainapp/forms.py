from registration.forms import RegistrationFormUniqueEmail
from django import forms

from django_filters import filterset
from mainapp.models import CarMake, CarModel



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

    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), to_field_name="make")
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.none(), to_field_name="car_model")
    price = forms.IntegerField()
    year = forms.IntegerField()


class AdvancedCarSearch(forms.Form):
    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), to_field_name="make")
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.none(), to_field_name="car_model")
    price = forms.IntegerField()
    year = forms.IntegerField()
    color = forms.CharField()
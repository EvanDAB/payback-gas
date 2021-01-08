from django import forms
from .models import *
from django.forms import ModelForm

# Create your forms here.
# class SimpleCalculatorForm(forms.Form):
#     mpgForm=forms.IntegerField(label='Miles Per Gallon')
#     gaspriceForm=forms.IntegerField(label='Gas Price')
#     distanceForm=forms.IntegerField(label='Distance')


class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

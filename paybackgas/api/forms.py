from django import forms
from .models import *
from django.forms import ModelForm
from api.models import SimpleCalculatorModel, MPGCalculatorModel, DistanceCalculatorModel

class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

class MPGCalculatorForm(ModelForm):
    class Meta:
        model=MPGCalculatorModel 
        fields="__all__"

class DistanceCalculatorForm(ModelForm):
    class Meta:
        model=DistanceCalculatorModel 
        fields="__all__"
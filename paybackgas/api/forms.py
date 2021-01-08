from django import forms
from .models import *
from django.forms import ModelForm

# Create your forms here.
class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

class MPGCalculatorForm(ModelForm):
    class Meta:
        model=MPGCalculatorModel
        fields="__all__"
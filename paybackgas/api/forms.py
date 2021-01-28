from django import forms
from .models import *
from django.forms import ModelForm, modelformset_factory
from api.models import SimpleCalculatorModel, MPGCalculatorModel, DistanceCalculatorModel

class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

class MPGCalculatorForm(ModelForm):
    class Meta:
        model=MPGCalculatorModel 
        fields="__all__"

DistanceCalculatorFormset = modelformset_factory(
    DistanceCalculatorModel, 
    fields=('destination', ),
    extra=1,
    widgets={'destination': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Destination Here'
        })
    }
)
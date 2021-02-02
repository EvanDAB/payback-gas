from django import forms
from .models import *
from django.forms import ModelForm, modelformset_factory
from api.models import SimpleCalculatorModel, MPGCalculatorModel, DistanceCalculatorModel

class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"
        widgets={
            'mpg': forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Enter MPG'
            }),
            'distance': forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Enter Total Trip (mi)'
            }),
            'gas_price': forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Enter Gas Price'
            })
        }

class MPGCalculatorForm(ModelForm):
    class Meta:
        model=MPGCalculatorModel 
        fields="__all__"
        widgets={
            'year': forms.Select(attrs={
                'class': 'col-8 custom-select'
            })
        }

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
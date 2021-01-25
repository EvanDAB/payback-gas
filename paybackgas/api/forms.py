from django import forms
from .models import *
from django.forms import ModelForm, modelformset_factory

# , inlineformset_factory
from api.models import SimpleCalculatorModel, MPGCalculatorModel, DistanceCalculatorModel, DistanceCalculatorModelDestinations

class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

class MPGCalculatorForm(ModelForm):
    class Meta:
        model=MPGCalculatorModel 
        fields="__all__"

# class DistanceCalculatorForm(forms.Form):
#     destination = forms.CharField(
#         label="Destination",
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Here'
#         })
#     )

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
# class DistanceCalculatorForm(ModelForm):
#     class Meta:
#        model=DistanceCalculatorModel 
#        fields="__all__"
    
#     def __init__(self, user, *args, **kwargs):
#         super(DistanceCalculatorForm, self).__init__(*args, *kwargs)
#         self.fields['destiation'] = forms.CharField(max_length=250)
# class DestinationsForm(forms.Form):
#     pass

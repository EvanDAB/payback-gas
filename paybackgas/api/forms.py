from django import forms
from .models import *
from django.forms import ModelForm
# formset_factory, inlineformset_factory
from api.models import SimpleCalculatorModel, MPGCalculatorModel, DistanceCalculatorModel, DistanceCalculatorModelDestinations

class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

class MPGCalculatorForm(ModelForm):
    class Meta:
        model=MPGCalculatorModel 
        fields="__all__"

class DistanceCalculatorForm(ModelForm):
#    class Meta:
#     model=DistanceCalculatorModel 
#     fields="__all__"
    destination_0 = forms.CharField(required=True)
    def save(self):
        DistanceCalculatorModel = self.instance
        dist_fk.destination_set_all().delete()
        for i in range(1):
            destination = self.cleaned_data['destination_{}'.format(i)]


# DistanceCalculatorFormSet = inlineformset_factory( 
#     model=DistanceCalculatorModel, 
#     form=DistanceCalculatorForm, 
#     fields='destination', extra=1, can_delete=True
#     )
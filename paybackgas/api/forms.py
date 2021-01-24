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
    destination_1 = forms.CharField(required=True)
    destination_2 = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        interests = ProfileInterest.objects.filter(
            profile=self.instance
        )
        for i in range(len(interests) + 1):
            field_name = 'interest_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = interests[i].interest
            except IndexError:
                self.initial[field_name] = “”
        # create an extra blank field
        field_name = 'interest_%s' % (i + 1,)
        self.fields[field_name] = forms.CharField(required=False)

    def clean(self):
        interests = set()
        i = 0
        field_name = 'interest_%s' % (i,)
        while self.cleaned_data.get(field_name):
           interest = self.cleaned_data[field_name]
           if interest in interests:
               self.add_error(field_name, 'Duplicate')
           else:
               interests.add(interest)
           i += 1
           field_name = 'interest_%s' % (i,)
       self.cleaned_data[“interests”] = interests
    def save(self):
        DistanceCalculatorModel = self.instance
        dist_fk.destination_set_all().delete()
        for i in range(3):
            destination = self.cleaned_data['destination_{}'.format(i)]
            DistanceCalculatorModelDestinations.objects.create(
                dist_fk=dist_fk, destination=destination
            )

# DistanceCalculatorFormSet = inlineformset_factory( 
#     model=DistanceCalculatorModel, 
#     form=DistanceCalculatorForm, 
#     fields='destination', extra=1, can_delete=True
#     )
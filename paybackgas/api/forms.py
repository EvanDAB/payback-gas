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
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['year'].queryset = Year.objects.none()

class AdvMPGCalculatorForm(ModelForm):
    class Meta:
        model = AdvMPGCalculatorModel
        fields = {'vehicle_id', 'year', 'make', 'model', 'model_options'}

        def __init__(self, *args, **kwargs):
            super().__inti__(*args, **kwargs)
            self.fields['model_options'].queryset = CarModelOptions.objects.none()

            if 'year' in self.data:
                try:
                    year = int(self.data.get('year'))
                    self.fields['model_options'].queryset = CarModelOptions.objects.filter(year=year).order_by('name')
                except (ValueError, TypeError):
                    pass #invalid input form the client: ignore and fallback to empty CIty queryset
            elif self.instance.pk:
                self.fields['model_options'].queryset = self.instance.year.branc_set.order_by('name')
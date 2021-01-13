from django import forms
from .models import *
from django.forms import ModelForm
from api.models import MPGCalculatorModel

# print(Year.objects)
# print('----YEAR OBJECTS ----')
# print(Year.CAR_YEARS)
# print('----YEAR CAR YEARS----')
# print(Year.CAR_YEARS[0])
# print('----YEAR CAR YEARS [AT INDEX]----')
#find a good alternative to objects.none() or objects.all()

# print(Year.CAR_YEARS.objects)
# Create your forms here.
class SimpleCalculatorForm(ModelForm):
    class Meta:
        model=SimpleCalculatorModel
        fields="__all__"

class MPGCalculatorForm(ModelForm):
    class Meta:
        # model=Year #here it displays the years from 1984 - current year
        # fields="__all__"
        model=MPGCalculatorModel # it shows both make and year select but doesn't populate them
        fields="__all__"

# class AdvMpgCalcForm(forms.ModelForm):
#     class Meta:
#         model = AdvMpgCalcModel
#         fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['make'].queryset = Make.objects.none() #takes field of make, #queryset shows dropdown (displays none at first)

    #     if 'year' in self.data:
    #         try:
    #             year_id = int(self.data.get('year'))
    #             self.fields['make'].queryset = Make.objects.filter(year_id=year_id)
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty make queryset
    #     elif self.instance.pk:
    #         self.fields['make'].queryset = self.instance.year.make_set
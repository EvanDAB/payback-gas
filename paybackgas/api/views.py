import requests
from urllib.parse import urlencode
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .forms import SimpleCalculatorForm, MPGCalculatorForm, DistanceCalculatorForm
# DistanceCalculatorFormSet
from .models import DistanceCalculatorModel
from decimal import Decimal
#the following were added to see if we could add additional forms on the distance page
# from django.forms import formset_factory, inlineformset_factory
# from django.db import transaction
# from django.urls import reverse_lazy

# Create your views here.
def main(request):
    if request.method == 'GET':
        form = SimpleCalculatorForm(request.GET)
        if form.is_valid():
            mpg = form.cleaned_data['mpg']
            gas_price = form.cleaned_data['gas_price']
            distance = form.cleaned_data['distance']
            total = distance / mpg * gas_price
            pretty_total = "{:.2f}".format(total)
            print('The trip costed ', pretty_total)
            return render(request, 'api/result.html', {'total' : pretty_total})
        
    return render(request, 'api/home.html', {'form' : form})


def mpgCalc(request):
    if request.method=='GET':
        form =  MPGCalculatorForm(request.GET)
        return render(request, 'api/mpg/mpg.html', {'form' : form })

def distanceCalc(request):
    form = DistanceCalculatorForm
    # items_formset = inlineformset_factory(Parent, Item, form=ItemForm, extra=1)
    # item_forms = items_formset() 
    # model = DistanceCalculatorModel
    # template_name = 'distance/distance.html'
    # form_class = DistanceCalculatorForm
    # success_url = None
   
    # def get_context_data(self, **kwargs):
    #     data = super(distanceCalc. self).get_context_data(**kwargs)
    #     if self.request.POST:
    #        data['destination'] = DistanceCalculatorFormSet(self.request.POST)
    #     else:
    #         data['destination'] = DistanceCalculatorFormSet()
    #     return data
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     destinations = context['destination']
    #     with transacton.atomic():
    #         self.object = form.save()
    #         if destinations.is_valid():
    #             destinations - self.object
    #             destinations.save()
    #     return super(DistanceCalculatorModel, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('disance:distance')
            
    return render(request, 'api/distance/distance.html', {'form': form })
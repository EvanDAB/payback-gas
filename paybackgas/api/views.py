import requests
from urllib.parse import urlencode
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .forms import SimpleCalculatorForm, MPGCalculatorForm, DistanceCalculatorForm
from decimal import Decimal


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
   
        
    return render(request, 'api/distance/distance.html', {'form': form })
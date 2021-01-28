import requests
from urllib.parse import urlencode
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, redirect
from django.views.generic import TemplateView
from .forms import SimpleCalculatorForm, MPGCalculatorForm,  DistanceCalculatorFormset
from .models import DistanceCalculatorModel
from decimal import Decimal
from .google_scrape import determine_distance as google_scrape
from django.urls import reverse_lazy


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


def mpg_calculator(request):
    if request.method=='GET':
        form =  MPGCalculatorForm(request.GET)
        return render(request, 'api/mpg/mpg.html', {'form' : form })

def distance_calculator(request):
    template_name='api/distance/distance.html'
    heading_message='Model Formset Demo'

    if request.method == 'GET':
        formset = DistanceCalculatorFormset(queryset=DistanceCalculatorModel.objects.none())
        # print(formset)
    elif request.method == 'POST':
        formset = DistanceCalculatorFormset(request.POST)
        print('formset: ', formset)
        if formset.is_valid():
            for form in formset:
                print('form: ', form)
                if form.cleaned_data.get('destination'):
                    # form.save()
                    print('CD: ', form.cleaned_data.get('destination'))
                    # return render(request, 'api/distance/distance-result.html')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message
    }) 

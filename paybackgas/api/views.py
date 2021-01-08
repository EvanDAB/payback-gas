from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import SimpleCalculatorForm
from decimal import Decimal 
# Create your views here.
def main(request):
    if request.method == 'GET':
        form = SimpleCalculatorForm(request.GET)
        if form.is_valid():
            mpg = form.cleaned_data['mpg']
            gasprice = form.cleaned_data['gasprice']
            distance = form.cleaned_data['distance']
            total = distance / mpg * gasprice
            prettytotal = "{:.2f}".format(total)
            print('The trip costed ', prettytotal)
            return render(request, 'api/result.html', {'total' : prettytotal})
        
    return render(request, 'api/home.html', {'form' : form})
    # return HttpResponse('MAIN')

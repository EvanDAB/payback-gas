from django.db import models
import datetime
import requests
import bs4
import urllib3
from bs4 import BeautifulSoup
# Create your models here.

now = datetime.datetime.now()
current_year = now.year
car_years = []
car_years_range = current_year - 1984
for i in range(car_years_range+1):
    car_years.append((str(i) , str(1984+i)))

class MPGCalculatorModel(models.Model):
    # class YearChoices(models.IntegerChoices):
    #     car_years
    
    # year = models.IntegerField(choices=YearChoices.choices)
    CAR_YEARS = car_years
    year = models.PositiveSmallIntegerField(default=('0','1984'), choices=CAR_YEARS)
    # make = models.CharField(max_length=40, choices=None)
    

    def __str__(self):
        return self.year

#Simple Calcualor Model 
class SimpleCalculatorModel(models.Model):
    mpg=models.DecimalField(max_digits=4, decimal_places=2, null=False)
    gas_price=models.DecimalField(max_digits=4, decimal_places=3, null=False)
    distance=models.DecimalField(max_digits=7, decimal_places=2, null=False)
# class Make(models.Model):
#     year = models.ForeignKey(Year, on_delete=models.CASCADE)
#     make = models.CharField(max_length=40)

#     def __str__(self):
#         return self.make

# class CarModel(models.Model):
#     year = models.ForeignKey(CarYear, on_delete=models.CASCADE)
#     make = models.ForeignKey(CarMake, on_delete=models.SET_NULL, blank=True, null=True)
#     model = models.CharField(max_length=100)

#     def __str__(self):
#         return self.make

# class CarModelOptions(models.Model):
#     year = models.ForeignKey(CarYear, on_delete=models.CASCADE)
#     make = models.ForeignKey(CarMake, on_delete=models.SET_NULL, blank=True, null=True)
#     model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, blank=True, null=True)
#     model_options = models.CharField(max_length=100)

#     def __str__(self):
#         return self.model_options

# # Returns vehilce ID
# class MPGCalculatorModel(models.Model):
#     name = models.CharField(max_length=124)
#     year = models.ForeignKey(Year, on_delete=models.CASCADE)
#     make = models.ForeignKey(Make, on_delete=models.SET_NULL, blank=True, null=True)
# #     model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, blank=True, null=True)
# #     model_options = models.ForeignKey(CarModelOptions, on_delete=models.SET_NULL, blank=True, null=True)
# #     vehicle_id = models.IntegerField()

#     def __str__(self):
#         return self.name




from django.db import models
import datetime
import requests
import bs4
import urllib3
from bs4 import BeautifulSoup
# Create your models here.

#Simple Calcualor Model 
class SimpleCalculatorModel(models.Model):
    mpg=models.DecimalField(max_digits=4, decimal_places=2, null=False)
    gasprice=models.DecimalField(max_digits=4, decimal_places=3, null=False)
    distance=models.DecimalField(max_digits=7, decimal_places=2, null=False)

#Adv. MPG Calculator
# class CarYear(models.Model):
#     year = models.IntegerField()
#     def __str__(self):
#         return self.year

# class CarMake(models.Model):
#     year = models.ForeignKey(CarYear, on_delete=models.CASCADE)
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
#     modelOptions = models.CharField(max_length=100)
    
class MPGCalculatorModel(models.Model):
    now = datetime.datetime.now()
    global currentyear
    currentyear = now.year
    global caryears
    caryears = []
    caryearsrange = currentyear - 1984
    for i in range(caryearsrange+1):
        caryears.append((i, 1984+i))

    class CarYear(models.IntegerChoices):
        caryears
    year = models.IntegerField(choices=caryears)

from django.db import models
import datetime
import requests
# import bs4
# import urllib3
# from bs4 import BeautifulSoup
# Create your models here.

now = datetime.datetime.now()
current_year = now.year
car_years = []
car_years_range = current_year - 1984
for i in range(car_years_range+1):
    car_years.append((str(i) , str(1984+i)))

class MPGCalculatorModel(models.Model):
    CAR_YEARS = car_years
    year = models.PositiveSmallIntegerField(default=('0','1984'), choices=CAR_YEARS)

    def __str__(self):
        return self.year

class DistanceCalculatorModel(models.Model):
    destination = models.CharField(max_length=100)
    # end_destination = models.CharField(max_length=100)
    # # api_key AIzaSyCNyQlXhkdhJQ4iczZl79qrzPf8EJXhzL8
    # def __str__(self):
    #     return self.id
class DistanceCalculatorModelDestinations(models.Model):
    dist_fk = models.ForeignKey(DistanceCalculatorModel)
    
#Simple Calcualor Model 
class SimpleCalculatorModel(models.Model):
    mpg=models.DecimalField(max_digits=4, decimal_places=2, null=False)
    gas_price=models.DecimalField(max_digits=4, decimal_places=3, null=False)
    distance=models.DecimalField(max_digits=7, decimal_places=2, null=False)
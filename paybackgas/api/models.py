from django.db import models
import datetime

# Create your models here.
class SimpleCalculatorModel(models.Model):
    mpg=models.DecimalField(max_digits=4, decimal_places=2, null=False)
    gasprice=models.DecimalField(max_digits=4, decimal_places=3, null=False)
    distance=models.DecimalField(max_digits=7, decimal_places=2, null=False)

class MPGCalculatorModel(models.Model):
    now = datetime.datetime.now()
    currentyear = now.year
    global caryears
    caryears = []
    caryearsrange = currentyear - 1984
    for i in range(caryearsrange+1):
        caryears.append((i, 1984+i))
    print(caryears)

    # class YearChoices(models.IntegerChoices):
    #     year = models.IntegerField(choices=caryears)

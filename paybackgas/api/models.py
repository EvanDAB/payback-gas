from django.db import models


# Create your models here.
class SimpleCalculatorModel(models.Model):
    mpg=models.DecimalField(max_digits=4, decimal_places=2, null=False)
    gasprice=models.DecimalField(max_digits=4, decimal_places=3, null=False)
    distance=models.DecimalField(max_digits=7, decimal_places=2, null=False)

# class MPGCalculator(models.Model):
#     currentyear = date.year()
#     print(currentyear)
#     # def setChoiceValues(iterator, value):
#     #     return (iterator, value)
#     # class Year(models.IntegerChoices):

#     # year=models.Integer
from django.contrib import admin
from .models import CarYear, CarMake, CarModel, CarModelOptions

# Register your models here.
admin.site.register(CarYear)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(CarModelOptions)
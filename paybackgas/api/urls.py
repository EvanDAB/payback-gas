from django.urls import path
from .views import main, mpgCalc

urlpatterns = [
    path('', main),
    path('mpg/', mpgCalc)
]
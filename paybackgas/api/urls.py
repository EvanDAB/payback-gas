from django.urls import path
from .views import main, mpgCalc, distanceCalc
# from . import views

urlpatterns = [
    path('', main),
    path('mpg/', mpgCalc),
    path('distance/', distanceCalc)

]
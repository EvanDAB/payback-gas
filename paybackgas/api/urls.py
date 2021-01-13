from django.urls import path
from .views import main, mpgCalc
from . import views

urlpatterns = [
    path('', main),
    path('mpg/', mpgCalc)
    # path('ajax/load-makes', views.load_makes, name='ajax_load_makes')
    # path('advMPG/', views.CarYearListView.as_view(), name='car_year')
]
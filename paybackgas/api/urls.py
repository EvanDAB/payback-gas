from django.urls import path
from .views import main, mpg_calculator, distance_calculator, google_scrape
# from . import views

urlpatterns = [
    path('', main),
    path('mpg/', mpg_calculator),
    path('distance/', distance_calculator),
    path('distance/google_scrape/', google_scrape)

]
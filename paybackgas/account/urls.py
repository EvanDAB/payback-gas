from django.urls import path
from . import views

urlpatterns = [
    #postviews
    path('login/', views.user_login,name='login')
]
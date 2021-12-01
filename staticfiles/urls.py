from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 
from .views import *

urlpatterns = [
    #Leave as empty string for base url
    path('', views.load, name="the_load"),
    path('load/', views.load, name="load"),
    path('home/', views.home, name="home"),
    path('data/', views.data, name="data"),
    path('data/eda', views.eda, name="eda"),
    path('data/regression', views.regression, name="regression"),
    path('index/', views.index, name="index"),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_home, name='index_home'),
    path('calculate_total', views.calculate_total, name='calculate_total'),


]

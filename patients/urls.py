from django.urls import path
from .views import get_patients, get_insurances, get_records

urlpatterns = [
  path('get_patients/', get_patients),
  path('get_insurances/', get_insurances),
  path('get_records/', get_records)
]
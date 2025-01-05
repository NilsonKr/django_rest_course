from django.urls import path
from .views import patients_view, patient_pk_view,get_insurances, get_records

urlpatterns = [
  path('', patients_view),
  path('<pk>/', patient_pk_view),
  path('get_insurances/', get_insurances),
  path('get_records/', get_records)
]
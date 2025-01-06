from django.urls import path
from .views import PatientsView, PatientDetailView

urlpatterns = [
  path('', PatientsView.as_view()),
  path('<pk>/', PatientDetailView.as_view()),
  # path('get_insurances/', get_insurances),
  # path('get_records/', get_records)
]
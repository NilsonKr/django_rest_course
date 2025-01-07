from rest_framework.response import Response
from rest_framework import status


from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

# Create your views here.

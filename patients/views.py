from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

# Create your views here.


@api_view(['GET'])
def get_patients(request):
  patients = Patient.objects.all()
  serializer = PatientSerializer(patients, many=True)

  return Response(serializer.data)


@api_view(['GET'])
def get_insurances(request):
  insurances = Insurance.objects.all()
  serializer = InsuranceSerializer(insurances, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_records(request):
  insurances = MedicalRecord.objects.all()
  serializer = MedicalRecordSerializer(insurances, many=True)
  return Response(serializer.data)
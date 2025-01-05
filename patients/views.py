from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

# Create your views here.

@api_view(['GET', 'POST'])
def patients_view(request):
  if request.method == 'GET':
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)
    
  if request.method == 'POST': 
    serializer = PatientSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data ,status=status.HTTP_201_CREATED)
  
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def patient_pk_view(request, pk):

  try: 
    patient = Patient.objects.get(id=pk)
  except Patient.DoesNotExist:
    return Response({'detail': 'Patient does not exitsts'}, status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = PatientSerializer(patient)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if request.method == 'PUT':
    serializer = PatientSerializer(patient, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  if request.method == 'PATCH':
    serializer = PatientSerializer(patient, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  if request.method == 'DELETE':
    serializer = PatientSerializer(patient)
    patient.delete()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


      



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
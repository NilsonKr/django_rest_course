from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

# Create your views here.

class PatientsViewSet(ModelViewSet):
  serializer_class = PatientSerializer
  queryset = Patient.objects.all()
  
  
  def destroy(self, request, pk):
    instance = self.get_object()
    serializer = self.serializer_class(instance)
    self.perform_destroy(instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

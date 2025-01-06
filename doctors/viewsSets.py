from rest_framework.viewsets import ModelViewSet
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorsViewSet(ModelViewSet):
  serializer_class = DoctorSerializer
  queryset = Doctor.objects.all()
from rest_framework import serializers
from .models import Doctor, DoctorAvailability, Department

class DoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
  class Meta:
    model = DoctorAvailability
    fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = '__all__'
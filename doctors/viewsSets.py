from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorsViewSet(ModelViewSet):
  serializer_class = DoctorSerializer
  queryset = Doctor.objects.all()

  @action(methods=['POST'], detail=True, url_path='send-inform-email')
  def send_inform_email(self, request, pk):
    instance = self.get_object()
    return Response({ 'detail': f'Informe del Doctor {instance.first_name} {instance.last_name} has sido enviado al email {request.data["email"]}'})
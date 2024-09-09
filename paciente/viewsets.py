from rest_framework import viewsets
from paciente.models import Paciente
from paciente.serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
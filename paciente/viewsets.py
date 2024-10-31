from rest_framework import viewsets
from paciente.models import Paciente, Consulta
from paciente.serializers import PacienteSerializer, ConsultaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
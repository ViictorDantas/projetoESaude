from rest_framework import viewsets
from paciente.models import Paciente , Prontuario
from paciente.serializers import PacienteSerializer, ProntuarioSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    
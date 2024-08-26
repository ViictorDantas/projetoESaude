from rest_framework import serializers
from paciente.models import Paciente , Prontuario

class ProntuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prontuario
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    
    prontuarios = ProntuarioSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'
        
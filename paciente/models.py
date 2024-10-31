from django.db import models
from usuario.models import Usuario

'''

CRIAR API
passo 1 Criar Models
passo 2 Criar o Serializers
passo 3 Criar viewsets
passo 4 criar routers
passo 5 incluir a rota na ulrs.py do setup
passo 6 colocar o admin

'''

class Paciente(Usuario):

    plano_saude = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = [
            'first_name' 
        ]

    def __str__(self):
        return f'Paciente: {self.first_name} {self.last_name}'

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="consultas_medico")
    data_horario = models.DateTimeField()
    motivo = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['data_horario']

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico} em {self.data_horario}"





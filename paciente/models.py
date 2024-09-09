from django.db import models
from usuario.models import Usuario

class Paciente(Usuario):
    # Aqui você pode adicionar campos específicos de Paciente
    plano_saude = models.CharField(max_length=100, blank=True, null=True)  # Plano de saúde do paciente
    numero_cartao_sus = models.CharField(max_length=15, blank=True, null=True)  # Número do cartão SUS
    alergias = models.TextField(blank=True, null=True) 
    historico_medico = models.TextField(blank=True, null=True) 

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = [
            'first_name' 
        ]

    def __str__(self):
        return f'Paciente: {self.first_name} {self.last_name}'

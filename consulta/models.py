from django.db import models

'''

CRIAR API
passo 1 Criar Models
passo 2 Criar o Serializers
passo 3 Criar viewsets
passo 4 criar routers
passo 5 incluir a rota na ulrs.py do setup
passo 6 colocar o admin

'''

class Consulta(models.Model):
    
    paciente = models.CharField(null=True, blank=True, max_length=255)
    data_consulta = models.DateTimeField(null=True, blank=True)
    medico = models.CharField(max_length=255)
    laudo_final = models.CharField(max_length=255)
    prescricoes = models.TextField()
    exames_solicitados = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.medico
    
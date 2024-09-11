from django.db import models


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    numero_residencia = models.CharField(max_length=10) 
    cep = models.CharField(max_length=8)  # formato xxxxxxxx (sem hífen)
    

    def __str__(self):
        return f'{self.rua}, {self.bairro} - {self.cep}'
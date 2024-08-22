from django.contrib import admin
from consulta.models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data_consulta', 'medico')

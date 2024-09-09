from django.contrib import admin
from consulta.models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data_consulta', 'medico', 'laudo_final', 'prescricoes', 'exames_solicitados')

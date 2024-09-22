from rest_framework import routers
from paciente.viewsets import PacienteViewSet

paciente_router = routers.DefaultRouter()
paciente_router.register('paciente', PacienteViewSet)

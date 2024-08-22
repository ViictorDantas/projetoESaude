from rest_framework import routers
from consulta.viewsets import ConsultaViewSet


consulta_router = routers.DefaultRouter()
consulta_router.register('consulta', ConsultaViewSet)
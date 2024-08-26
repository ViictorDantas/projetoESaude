from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from consulta.router import consulta_router
from paciente.router import paciente_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(consulta_router.urls)),
    path('api/v1/', include(paciente_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

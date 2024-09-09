from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario.router import usuario_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include(usuario_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

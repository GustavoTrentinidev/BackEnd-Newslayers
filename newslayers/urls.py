from django.contrib import admin
from django.urls import path, include

from core.views import UsuarioViewSet, TopicoViewSet, CurtidaViewSet, NoticiaViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'topicos', TopicoViewSet)
router.register(r'curtidas', CurtidaViewSet)
router.register(r'noticias', NoticiaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]

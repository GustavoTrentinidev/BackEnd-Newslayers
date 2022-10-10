from django.contrib import admin
from django.urls import path, include

from core.views import UsuarioViewSet, TopicoViewSet, NoticiaViewSet, ComentarioViewSet, CurtidaViewSet, MIDIAUSERViewSet

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'topicos', TopicoViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'curtidas', CurtidaViewSet)
router.register(r'midias-usuarios', MIDIAUSERViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

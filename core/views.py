from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Topico, Curtida
from core.serializers import UsuarioSerializer, TopicoSerializer, CurtidaSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TopicoViewSet(ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

class CurtidaViewSet(ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer
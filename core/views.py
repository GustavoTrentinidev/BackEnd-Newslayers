from core.models.Midia import Midia
from core.models.Midia_user import Midia_user
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Topico, Noticia, Comentario, Curtida, Midia
from core.serializers import UsuarioSerializer, TopicoSerializer, NoticiaSerializer, CriarNoticiaSerializer, ComentarSerializer,UsuarioPostSerializer, CurtirSerilializer, MIDIAUSERPOSTSerializer
from rest_framework.permissions import AllowAny


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes_by_action = {'create': [AllowAny]}
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return UsuarioSerializer
        return UsuarioPostSerializer

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
    

class TopicoViewSet(ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

class NoticiaViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = Noticia.objects.all()
        idtopico = self.request.query_params.get('idtopico') 
        #Para filtrar pelo id é necessário utilizar um url como: http://127.0.0.1:8000/noticias/?idtopico=3
        if idtopico is not None:
            queryset = queryset.filter(topico_idtopico=idtopico)
        return queryset 

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return NoticiaSerializer
        return CriarNoticiaSerializer

class ComentarioViewSet(ModelViewSet):
    serializer_class = ComentarSerializer
    def get_queryset(self):
        queryset = Comentario.objects.all()
        idnoticia = self.request.query_params.get('idnoticia')
        if idnoticia is not None:
            queryset = queryset.filter(noticia_idnoticia=idnoticia)
        return queryset

class CurtidaViewSet(ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtirSerilializer
    def get_queryset(self):
        queryset = Curtida.objects.all()
        idnoticia = self.request.query_params.get('idnoticia')
        if idnoticia is not None:
            queryset = queryset.filter(idnoticia=idnoticia)
        return queryset

class MIDIAUSERViewSet(ModelViewSet):
    queryset = Midia_user.objects.all()
    serializer_class = MIDIAUSERPOSTSerializer

class UsuarioLogado(ModelViewSet):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Usuario.objects.filter(id=user.id)
        return queryset
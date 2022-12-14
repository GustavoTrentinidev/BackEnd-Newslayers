from django.http import HttpResponse
from core.models.Midia import Midia
from core.models.Midia_user import Midia_user
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Topico, Noticia, Comentario, Curtida, Midia
from core.serializers import UsuarioSerializer, TopicoSerializer, NoticiaSerializer, CriarNoticiaSerializer, ComentarSerializer,UsuarioPostSerializer, CurtirSerilializer, MIDIAUSERPOSTSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action


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
    
    @action(detail=True, methods=['get'])
    def seguir(self, request, pk):
        # ​http://localhost:8000/usuarios/17/seguir/ -> segue o usuário 17
        seguidor = Usuario.objects.get(id=request.user.id)
        seguido = Usuario.objects.get(id=pk)
        if not Usuario.objects.get(id=pk).seguidores.contains(seguidor):
            Usuario.objects.get(id=pk).seguidores.add(seguidor)
            return HttpResponse(content=f'{seguidor.username} começou a seguir {seguido.username}')
        else:
            Usuario.objects.get(id=pk).seguidores.remove(seguidor)
            return HttpResponse(content=f'{seguidor.username} deixou de seguir {seguido.username}')
        
class TopicoViewSet(ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

from core.paginations import NoticiasPagination

class NoticiaViewSet(ModelViewSet):
    pagination_class = NoticiasPagination
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

class TodasNoticiasView(ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

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
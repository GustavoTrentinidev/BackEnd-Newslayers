from tkinter import FLAT
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, HiddenField, CurrentUserDefault
from core.models import Usuario, Topico, Curtida, Midia_user, Noticia, Midia, Comentario
from django.contrib.auth.models import Group
from drf_extra_fields.fields import Base64ImageField


class CurtirSerilializer(ModelSerializer):
    iduser = CharField(default=CurrentUserDefault()) 
    class Meta:
        model = Curtida
        fields = ('id','iduser','idnoticia')

class CurtidaNoticiaSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = ("iduser",)

class CurtidaUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = ("idnoticia",)

class MidiaUserSerializer(ModelSerializer):
    class Meta:
        model = Midia_user
        fields = ("id","midiabannerpath", "midiaprofilepath")

class MidiaNoticiaSerializer(ModelSerializer):
    midiapath = Base64ImageField()
    class Meta: 
        model = Midia
        fields = ("midiapath",)

class UsuarioNoticiasSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)
    class Meta:
        model = Noticia
        fields = ("id","midia","noticiatitulo","texto","noticiadatacadastro")

class UsuarioPostSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("username", "password", "email",)

    email = CharField(max_length=120, required=True)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        instance.groups.add(Group.objects.get(name="leitor"))
        return instance

class UsuarioSerializer(ModelSerializer):
    midia = MidiaUserSerializer()
    curtidas = CurtidaUsuarioSerializer(many=True)
    noticias = UsuarioNoticiasSerializer(many=True)
    class Meta: 
        model = Usuario
        fields = "__all__"

    seguidores = SerializerMethodField()
    def get_seguidores(self,instance):
        nomes_seguidores = []
        qtd_curtidas_seguidor = []
        seguidores = instance.seguidores.get_queryset()
        noticias_usuario = Noticia.objects.filter(user_iduser=instance.id)
        for seguidor in seguidores:
            if noticias_usuario:
                for noticia in noticias_usuario:
                    for curtida in Curtida.objects.filter(idnoticia=noticia.id).values_list('iduser',flat=True):
                        if curtida == seguidor.id:
                            qtd_curtidas_seguidor.append(seguidor.id)
                            
            if Midia_user.objects.filter(user_iduser=seguidor.id):
                midiabannerpath = Midia_user.objects.values_list('midiabannerpath', flat=True).get(user_iduser=seguidor.id)
                midiabannerpath = "https://newslayersimages.s3.amazonaws.com/"+ midiabannerpath
                midiaprofilepath = Midia_user.objects.values_list('midiaprofilepath', flat=True).get(user_iduser=seguidor.id)
                midiaprofilepath = "https://newslayersimages.s3.amazonaws.com/"+ midiaprofilepath
                midia = {"midiabannerpath": midiabannerpath,"midiaprofilepath": midiaprofilepath}
            else:
                midia = {}
            likes = len(qtd_curtidas_seguidor)
            nomes_seguidores.append({"id": seguidor.id, "username": seguidor.username, "midia":midia, "curtidas": likes})
        return nomes_seguidores
    
    seguindo = SerializerMethodField()
    def get_seguindo(self,instance):
        nomes_seguidos = []
        seguindo = instance.seguindo.get_queryset()
        for seguidos in seguindo:
            if Midia_user.objects.filter(user_iduser=seguidos.id):
                midiabannerpath = Midia_user.objects.values_list('midiabannerpath', flat=True).get(user_iduser=seguidos.id)
                midiabannerpath = "https://newslayersimages.s3.amazonaws.com/"+ midiabannerpath
                midiaprofilepath = Midia_user.objects.values_list('midiaprofilepath', flat=True).get(user_iduser=seguidos.id)
                midiaprofilepath = "https://newslayersimages.s3.amazonaws.com/"+ midiaprofilepath
                midia = {"midiabannerpath": midiabannerpath,"midiaprofilepath": midiaprofilepath}
            else:
                midia = {}
            nomes_seguidos.append({"id":seguidos.id ,"username": seguidos.username, "midia":midia})
        return nomes_seguidos

    # def create(self, validated_data):
    #     fotos = validated_data.pop("midia")
    #     usuario  = Usuario.objects.create(**validated_data)
    #     Midia_user.objects.create(**fotos, user_iduser=usuario)
    #     return usuario

class TopicoSerializer(ModelSerializer):
    class Meta:
        model = Topico
        fields = "__all__"

class UsuarioNaNoticia(ModelSerializer):
    midia = MidiaUserSerializer()
    class Meta:
        model = Usuario
        fields = ("username", "id" , "midia")

class ComentarioNoticiaSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("id","datacomentario","textocomentario", "user_iduser")

class NoticiaSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)
    user_iduser = UsuarioNaNoticia()
    topico_idtopico = TopicoSerializer()
    comentarios = ComentarioNoticiaSerializer(many=True)
    curtidas = CurtidaNoticiaSerializer(many=True)
    class Meta:
        model = Noticia
        fields = "__all__"
    
class CriarNoticiaSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)
    user_iduser = HiddenField(default=CurrentUserDefault()) 
    class Meta:
        model = Noticia
        fields = (
            "id",
            "user_iduser",
            "topico_idtopico",
            "midia",
            "noticiatitulo",
            "texto"
        )
    def create(self, validated_data):
        fotos = validated_data.pop("midia")
        noticia = Noticia.objects.create(**validated_data)
        for foto in fotos:
            Midia.objects.create(**foto, noticia_idnoticia=noticia)
        return noticia
    
class MIDIAUSERPOSTSerializer(ModelSerializer):
    midiabannerpath=Base64ImageField()
    midiaprofilepath=Base64ImageField()
    class Meta:
        model = Midia_user
        fields = "__all__"

class ComentarSerializer(ModelSerializer):
    user_iduser = UsuarioNaNoticia(default=CurrentUserDefault()) 
    class Meta:
        model = Comentario
        fields = "__all__"
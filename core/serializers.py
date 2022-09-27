from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Usuario, Topico, Curtida


class UsuarioSerializer(ModelSerializer):
    class Meta: 
        model = Usuario
        fields = "__all__"

    seguidores = SerializerMethodField()
    def get_seguidores(self,instance):
        nomes_seguidores = []
        seguidores = instance.seguidores.get_queryset()
        for seguidor in seguidores:
            nomes_seguidores.append({"id": seguidor.id, "username": seguidor.username})
        return nomes_seguidores
    
    seguindo = SerializerMethodField()
    def get_seguindo(self,instance):
        nomes_seguidos = []
        seguindo = instance.seguindo.get_queryset()
        for seguidos in seguindo:
            nomes_seguidos.append({"id":seguidos.id ,"username": seguidos.username})
        return nomes_seguidos

    midia = SerializerMethodField()
    def get_midia(self, instance):
        banner_e_profile = []
        midia = instance.midia.get_queryset()
        for img in midia:
            banner_e_profile.append({"midiabannerpath": img.midiabannerpath, "midiaprofilepath": img.midiaprofilepath})
        return banner_e_profile

class TopicoSerializer(ModelSerializer):
    class Meta:
        model = Topico
        fields = "__all__"

class CurtidaSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = "__all__"
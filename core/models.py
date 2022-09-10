from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    seguidores = models.ManyToManyField('self', symmetrical=False, related_name='seguindo')

# class Seguir(models.Model):
#     def __str__(self):
#         return (self.usuarioSeguidor.nome + ' seguindo ' + self.usuarioSeguido.nome)
#     usuarioSeguido = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='seguindo')
#     usuarioSeguidor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='seguidores')
#     class Meta:
#         verbose_name_plural = "Seguir"

class Topico(models.Model):
    def __str__(self):
        return self.nometopico
    nometopico = models.CharField(max_length=45)

class Noticia(models.Model):
    def __str__(self):
        return self.noticiatitulo
    noticiatitulo = models.CharField(max_length=180)
    texto = models.CharField(max_length=7000)
    noticiadatacadastro = models.DateField(default=datetime.now)
    user_iduser = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    topico_idtopico = models.ForeignKey(Topico, on_delete=models.PROTECT)

class Comentario(models.Model):
    def __str__(self):
        return f'({self.noticia_idnoticia}) {self.user_iduser}: {self.textocomentario}'
    datacomentario = models.DateField(default=datetime.now)
    textocomentario = models.CharField(max_length=240)
    user_iduser = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    noticia_idnoticia = models.ForeignKey(Noticia, on_delete=models.PROTECT)

class Curtida(models.Model):
    def __str__(self):
        return f'{self.iduser} -> {self.idnoticia}'
    iduser = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    idnoticia = models.ForeignKey(Noticia, on_delete=models.PROTECT)

from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from .Topico import Topico


class Noticia(models.Model):
    def __str__(self):
        return self.noticiatitulo
    noticiatitulo = models.CharField(max_length=180)
    texto = models.CharField(max_length=7000)
    noticiadatacadastro = models.DateField(default=datetime.now)
    user_iduser = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="noticias")
    topico_idtopico = models.ForeignKey(Topico, on_delete=models.PROTECT, related_name="noticias")
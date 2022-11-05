from django.db import models
from .Noticia import Noticia
from django.contrib.auth import get_user_model


class Curtida(models.Model):
    def __str__(self):
        return f'{self.iduser} -> {self.idnoticia}'
    iduser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="curtidas")
    idnoticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="curtidas")
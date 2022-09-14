from django.db import models


class Topico(models.Model):
    def __str__(self):
        return self.nometopico
    nometopico = models.CharField(max_length=45)
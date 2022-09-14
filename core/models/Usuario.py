from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    seguidores = models.ManyToManyField('self', symmetrical=False, related_name='seguindo')
from django.db import models

class Usuario(models.Model):
    def __str__(self):
        return self.nome
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    senha = models.CharField(max_length=45)
    tipousuario = models.IntegerField(default=0)
    img = models.ImageField()
    banner = models.ImageField()

class Seguir(models.Model):
    def __str__(self):
        return (self.usuarioSeguidor.nome + ' seguindo ' + self.usuarioSeguido.nome)
    usuarioSeguido = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='seguindo')
    usuarioSeguidor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='seguidores')
    class Meta:
        verbose_name_plural = "Seguir"
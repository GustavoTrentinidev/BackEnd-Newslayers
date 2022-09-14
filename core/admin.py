from django.contrib import admin
from core.models import Usuario, Noticia, Topico, Curtida, Comentario, Midia_user, Midia

#admin.site.register(Usuario)
# admin.site.register(Noticia)
admin.site.register(Topico)
admin.site.register(Curtida)
admin.site.register(Comentario)

class MidiaUserInline(admin.TabularInline):
    model = Midia_user

@admin.register(Usuario)
class UsuarioComMidia(admin.ModelAdmin):
    inlines = (MidiaUserInline,)

class MidiaNoticiaInline(admin.TabularInline):
    model = Midia

@admin.register(Noticia)
class NoticiaComMidia(admin.ModelAdmin):
    inlines = (MidiaNoticiaInline,)
from django.contrib import admin
from core.models import Usuario, Noticia, Topico, Curtida, Comentario, Midia_user, Midia

#admin.site.register(Usuario)
# admin.site.register(Noticia)
admin.site.register(Topico)
admin.site.register(Curtida)
admin.site.register(Comentario)
admin.site.register(Midia_user)
admin.site.register(Usuario)

class MidiaNoticiaInline(admin.TabularInline):
    model = Midia

@admin.register(Noticia)
class NoticiaComMidia(admin.ModelAdmin):
    inlines = (MidiaNoticiaInline,)
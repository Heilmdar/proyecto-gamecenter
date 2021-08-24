from django.contrib import admin
from .models import Ventas
from .models import Nosotros
from .models import ComentarioContacto
#from .models import Desarrolladores
# Register your models here.
class administrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Ventas, administrarModelo)

class administrarNosotros(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Nosotros, administrarNosotros)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

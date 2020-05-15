from django.contrib import admin
from libros.models import Libro
from libros.models import Ejemplar
from libros.models import Autor
from libros.models import Usuario

# Register your models here.

admin.site.register(Libro,)
admin.site.register(Ejemplar,)
admin.site.register(Autor,)
admin.site.register(Usuario,)

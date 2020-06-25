from django.contrib import admin
from libros.models import Libro, Ejemplar, Autor ,Usuario

# Register your models here.


class LibroInLine(admin.TabularInline):
    model = Libro

class AutorDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']
    inlines = [ LibroInLine,]
    search_fields = ['Nombre',]
    

class LibroDisplay(admin.ModelAdmin):
    list_display = ['editorial', 'titulo']
    


class EjemplarDisplay(admin.ModelAdmin):
    filter_horizontal = ('cod_libro', )
    #si el jet esta funcionando, esto no funciona


class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información personal', {'fields':('cod_usr', 'nombre',)
        }),

        ('Contacto', {'fields':('telefono', 'direccion',)
        })
    )

    list_display = ['nombre', 'direccion']
    
    
admin.site.register(Libro, LibroDisplay)
admin.site.register(Ejemplar, EjemplarDisplay)
admin.site.register(Autor, AutorDisplay)
admin.site.register(Usuario, UsuarioAdmin)

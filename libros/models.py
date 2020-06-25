from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length = 35)
    codigo = models.AutoField(primary_key = True, default = None, unique = True)

    def __str__(self):
        return str(self.nombre)


class Libro(models.Model):
    titulo = models.CharField(max_length = 30)
    editorial = models.CharField(max_length = 30)
    paginas = models.IntegerField(null = True)
    codigo = models.AutoField(primary_key = True, unique = True)
    codigo_aut = models.ForeignKey(Autor, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)


class Ejemplar(models.Model):
    codigo = models.AutoField(primary_key = True, unique = True)
    localizacion = models.CharField(max_length = 30)
    cod_libro = models.ManyToManyField(Libro)
    #si el jet esta funcionando, esto no funciona
    

    def __str__(self):
        return str(self.cod_libro)



class Usuario(models.Model):
    codigo = models.AutoField(primary_key = True, unique = True)
    cod_usr = models.IntegerField(null = True)
    telefono = models.IntegerField(null = True)
    nombre = models.CharField(max_length = 35)
    direccion = models.CharField(max_length = 25)
    cod_ejem = models.ManyToManyField(Ejemplar)

    def __str__(self):
        return str(self.nombre)

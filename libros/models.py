from django.db import models

# Create your models here.

class Usuario(models.Model):
    codigo = models.AutoField(primary_key = True, unique = True)
    telefono = models.IntegerField(null = True)
    nombre = models.CharField(max_length = 35)
    direccion = models.CharField(max_length = 25)

    def __str__(self):
        return str(self.nombre +", "+self.direccion)


class Ejemplar(models.Model):
    codigo = models.AutoField(primary_key = True, unique = True)
    localizacion = models.CharField(max_length = 30)
    codigo_usr = models.ForeignKey(Usuario, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)





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
    codigo_eje = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    codigo_lbr = models.ForeignKey(Autor, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)

# Generated by Django 2.2 on 2020-06-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0014_usuario_cod_usr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='cod_libro',
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='cod_libro',
            field=models.ManyToManyField(to='libros.Libro'),
        ),
    ]
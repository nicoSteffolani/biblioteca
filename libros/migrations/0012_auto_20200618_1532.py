# Generated by Django 2.2 on 2020-06-18 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0011_auto_20200618_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='codigo_eje',
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='cod_libro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='libros.Libro'),
        ),
    ]

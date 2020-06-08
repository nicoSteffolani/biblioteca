# Generated by Django 2.2 on 2020-05-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_auto_20200515_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='codigo_lbr',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='libros.Libro'),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='codigo_usr',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='libros.Usuario'),
        ),
        migrations.AddField(
            model_name='libro',
            name='codigo_eje',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='libros.Ejemplar'),
        ),
    ]
# Generated by Django 2.2 on 2020-05-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_auto_20200515_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='codigo',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='codigo',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='libro',
            name='codigo',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='codigo',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
    ]

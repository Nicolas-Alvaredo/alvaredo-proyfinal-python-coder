# Generated by Django 5.1.1 on 2024-10-25 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_pelicula_descripcion_pelicula_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha_lanzamiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
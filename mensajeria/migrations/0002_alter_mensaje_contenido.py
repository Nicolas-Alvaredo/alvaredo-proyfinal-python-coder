# Generated by Django 5.1.1 on 2024-10-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='contenido',
            field=models.TextField(verbose_name='Escribe tu mensaje'),
        ),
    ]

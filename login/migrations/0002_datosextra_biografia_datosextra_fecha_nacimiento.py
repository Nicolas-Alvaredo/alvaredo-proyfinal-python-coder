# Generated by Django 5.1.1 on 2024-10-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datosextra',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocente', '0006_estudiante_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='listas',
            name='Nombre_lista',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.RemoveField(
            model_name='listas',
            name='Estudiante',
        ),
        migrations.AddField(
            model_name='listas',
            name='Estudiante',
            field=models.ManyToManyField(to='GestionDocente.estudiante'),
        ),
    ]

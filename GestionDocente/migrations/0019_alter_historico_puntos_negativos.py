# Generated by Django 4.1.4 on 2023-01-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocente', '0018_alter_historico_evidencias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='Puntos_negativos',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

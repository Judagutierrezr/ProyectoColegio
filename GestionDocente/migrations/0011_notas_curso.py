# Generated by Django 4.1.4 on 2023-01-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocente', '0010_alter_notas_español_1_alter_notas_español_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='Curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GestionDocente.curso'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-30 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_rename_fecha_creacion_contacto_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='created_at',
        ),
    ]

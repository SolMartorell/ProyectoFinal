# Generated by Django 4.0.6 on 2022-08-30 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_contacto_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='created_at',
        ),
    ]

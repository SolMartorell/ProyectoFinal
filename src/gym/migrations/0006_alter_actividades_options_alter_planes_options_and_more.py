# Generated by Django 4.0.6 on 2022-08-23 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_alter_planes_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividades',
            options={'verbose_name': 'Actividades', 'verbose_name_plural': 'Actividades'},
        ),
        migrations.AlterModelOptions(
            name='planes',
            options={'verbose_name': 'Planes', 'verbose_name_plural': 'Planes'},
        ),
        migrations.AlterModelOptions(
            name='socios',
            options={'verbose_name': 'Socios', 'verbose_name_plural': 'Socios'},
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_alter_actividades_options_alter_planes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socios',
            name='cuota_paga',
            field=models.BooleanField(blank=True),
        ),
    ]
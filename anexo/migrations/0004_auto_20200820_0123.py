# Generated by Django 3.0.5 on 2020-08-20 04:23

import anexo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo', '0003_auto_20200819_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='anexo',
            field=models.FileField(upload_to=anexo.models.caminho_anexo),
        ),
    ]
# Generated by Django 3.0.5 on 2020-09-17 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guarnicao', '0005_remove_guarnicao_finalizadopor'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarnicao',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Está ativo?'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-09-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guarnicao', '0008_auto_20200917_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guarnicao',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Está ativa?'),
        ),
    ]

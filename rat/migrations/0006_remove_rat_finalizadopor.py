# Generated by Django 3.0.5 on 2020-09-17 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat', '0005_rat_finalizadopor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rat',
            name='finalizadopor',
        ),
    ]
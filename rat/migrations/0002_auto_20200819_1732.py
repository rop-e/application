# Generated by Django 3.0.5 on 2020-08-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rat',
            name='infracao',
            field=models.BooleanField(help_text='Informe se houve infração', verbose_name='Houve infração?'),
        ),
    ]

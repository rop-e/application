# Generated by Django 3.0.5 on 2020-08-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opo', '0002_auto_20200821_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opo',
            name='datatermino',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de término'),
        ),
    ]

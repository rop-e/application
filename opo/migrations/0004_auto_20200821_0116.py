# Generated by Django 3.0.5 on 2020-08-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opo', '0003_auto_20200821_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oporelatorio',
            name='datafinalizacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de finalização'),
        ),
    ]

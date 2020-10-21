# Generated by Django 3.0.5 on 2020-09-15 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policial', '0001_initial'),
        ('guarnicao', '0002_auto_20200813_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarnicao',
            name='finalizadopor',
            field=models.ForeignKey(blank=True, help_text='Finalizado por', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finalizadopor', to='policial.Policial'),
        ),
    ]

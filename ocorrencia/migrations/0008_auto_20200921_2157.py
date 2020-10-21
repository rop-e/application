# Generated by Django 3.0.5 on 2020-09-22 00:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0007_observacaoocorrencia_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacaoocorrencia',
            name='dataatualizacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de atualização'),
        ),
        migrations.AddField(
            model_name='observacaoocorrencia',
            name='datacriacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de criação'),
            preserve_default=False,
        ),
    ]

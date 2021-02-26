# Generated by Django 3.0.5 on 2020-09-17 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0003_remove_ocorrencia_finalizadopor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='vinculo',
            field=models.ForeignKey(blank=True, help_text='Informe a ocorrência', null=True, on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.Ocorrencia', verbose_name='É vinculo de ocorrência?'),
        ),
    ]
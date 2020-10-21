# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anexo', '0001_initial'),
        ('rat', '0001_initial'),
        ('ocorrencia', '0001_initial'),
        ('policial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexo',
            name='ocorrencia',
            field=models.ForeignKey(blank=True, help_text='Informe a ocorrência', null=True, on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.Ocorrencia', verbose_name='Ocorrência'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='policial',
            field=models.ForeignKey(help_text='Informe o policial', on_delete=django.db.models.deletion.CASCADE, to='policial.Policial', verbose_name='Policial'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='rat',
            field=models.ForeignKey(blank=True, help_text='Informe o Registro de Acidente de Trânsito', null=True, on_delete=django.db.models.deletion.CASCADE, to='rat.RAT', verbose_name='Registro de Acidente de Trânsito'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='tipoanexo',
            field=models.ForeignKey(help_text='Informe o tipo de anexo', on_delete=django.db.models.deletion.CASCADE, to='anexo.TipoAnexo', verbose_name='Tipo de anexo'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('observacao', '0001_initial'),
        ('rat', '0001_initial'),
        ('ocorrencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedimento', models.CharField(help_text='Informe o procedimento utilizado na ocorrencia', max_length=50, verbose_name='Procedimento')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Procedimento',
                'verbose_name_plural': 'Procedimentos',
                'db_table': 'procedimento',
            },
        ),
        migrations.CreateModel(
            name='ProcedimentoOcorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('observacao', models.ForeignKey(help_text='Informe a observação', on_delete=django.db.models.deletion.CASCADE, to='observacao.Observacao', verbose_name='Observação')),
                ('ocorrencia', models.ForeignKey(blank=True, help_text='Informe a ocorrência', null=True, on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.Ocorrencia', verbose_name='Ocorrência')),
                ('procedimento', models.ForeignKey(help_text='Informe o procedimento', on_delete=django.db.models.deletion.CASCADE, to='procedimentoocorrencia.Procedimento', verbose_name='Procedimento')),
                ('rat', models.ForeignKey(blank=True, help_text='Informe o Registro de Acidente de Trânsito', null=True, on_delete=django.db.models.deletion.CASCADE, to='rat.RAT', verbose_name='Registro de Acidente de Trânsito')),
            ],
            options={
                'verbose_name': 'Procedimento da ocorrência',
                'verbose_name_plural': 'Procedimentos da ocorrência',
                'db_table': 'procedimentoocorrencia',
            },
        ),
    ]

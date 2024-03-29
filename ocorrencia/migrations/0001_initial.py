# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('observacao', '0001_initial'),
        ('endereco', '0001_initial'),
        ('guarnicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Informe o tipo penal', max_length=50, verbose_name='Tipo penal')),
            ],
            options={
                'verbose_name': 'Tipo de infração',
                'verbose_name_plural': 'Tipos de infração',
                'db_table': 'infracao',
            },
        ),
        migrations.CreateModel(
            name='TipoOcorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoocorrencia', models.CharField(help_text='Informe o tipo de ocorrência', max_length=50, verbose_name='Tipo de Ocorrência')),
            ],
            options={
                'verbose_name': 'Tipo de ocorrência',
                'verbose_name_plural': 'Tipos de ocorrência',
                'db_table': 'tipoocorrencia',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.IntegerField(blank=True, help_text='Informe a ocorrência', null=True, verbose_name='É vinculo de ocorrência?')),
                ('relatorio', models.TextField(blank=True, null=True, verbose_name='Relatório da ocorrência')),
                ('dataocorrencia', models.DateTimeField(verbose_name='Data da ocorrência')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('endereco', models.ForeignKey(help_text='Informe o endereço da ocorrência', on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco', verbose_name='Endereço da Ocorrência')),
                ('guarnicao', models.ForeignKey(help_text='Informe a Guarnição', on_delete=django.db.models.deletion.CASCADE, to='guarnicao.Guarnicao', verbose_name='Guarnição')),
                ('infracao', models.ForeignKey(help_text='Informe o tipo penal', null=True, on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.Infracao', verbose_name='Tipo Penal')),
                ('tipoocorrencia', models.ForeignKey(help_text='Informe o tipo de ocorrência', on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.TipoOcorrencia', verbose_name='Tipo de Ocorrência')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'verbose_name_plural': 'Ocorrências',
                'db_table': 'ocorrencia',
            },
        ),
        migrations.CreateModel(
            name='ObservacaoOcorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.ForeignKey(help_text='Informe a observação', on_delete=django.db.models.deletion.CASCADE, to='observacao.Observacao', verbose_name='Observação')),
                ('ocorrencia', models.ForeignKey(help_text='Informe a ocorrência', on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.Ocorrencia', verbose_name='Ocorrência')),
            ],
            options={
                'verbose_name': 'Observação da ocorrência',
                'verbose_name_plural': 'Observações da ocorrência',
                'db_table': 'observacaoocorrencia',
            },
        ),
        migrations.CreateModel(
            name='GuarnicaoApoio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guarnicao', models.ManyToManyField(help_text='Informe a guarnição de apoio', to='guarnicao.Guarnicao', verbose_name='Guarnição')),
                ('ocorrencia', models.ForeignKey(help_text='Informe a Ocorrência', on_delete=django.db.models.deletion.CASCADE, to='ocorrencia.Ocorrencia', verbose_name='Ocorrência')),
            ],
            options={
                'verbose_name': 'Guarnição de Apoio',
                'verbose_name_plural': 'Guarnições de Apoio',
                'db_table': 'guarnicaoapoio',
            },
        ),
    ]

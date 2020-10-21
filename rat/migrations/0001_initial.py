# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('observacao', '0001_initial'),
        ('localrecebedor', '0001_initial'),
        ('veiculo', '0001_initial'),
        ('envolvido', '0001_initial'),
        ('endereco', '0001_initial'),
        ('guarnicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CondicaoMeteorologica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicao', models.CharField(help_text='Informe a condição meteorológica', max_length=100, verbose_name='Condição Meteorológica')),
            ],
            options={
                'verbose_name': 'Condição meteorológica',
                'verbose_name_plural': 'Condições meteorológicas',
                'db_table': 'condicaometeorologica',
            },
        ),
        migrations.CreateModel(
            name='CondicaoSinalizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicao', models.CharField(help_text='Informe a condição da sinalização', max_length=100, verbose_name='Condição da sinalização')),
            ],
            options={
                'verbose_name': 'Condição da sinalização',
                'verbose_name_plural': 'Condições de sinalização',
                'db_table': 'condicaosinalizacao',
            },
        ),
        migrations.CreateModel(
            name='CondicaoVia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicao', models.CharField(help_text='Informe a condição da via', max_length=100, verbose_name='Condição da Via')),
            ],
            options={
                'verbose_name': 'Condição da via',
                'verbose_name_plural': 'Condições da via',
                'db_table': 'condicaovia',
            },
        ),
        migrations.CreateModel(
            name='Pavimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavimentacao', models.CharField(help_text='Informe o tipo da pavimentação', max_length=100, verbose_name='Informe o tipo da pavimentação')),
            ],
            options={
                'verbose_name': 'Pavimentação',
                'verbose_name_plural': 'Pavimentações',
                'db_table': 'pavimentacao',
            },
        ),
        migrations.CreateModel(
            name='RAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infracao', models.BooleanField(help_text='Informe se houve infração', verbose_name='Infração?')),
                ('relatorio', models.TextField(blank=True, null=True, verbose_name='Relatório da ocorrência')),
                ('dataocorrencia', models.DateTimeField(verbose_name='Data da ocorrência')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('condicaometeorologica', models.ForeignKey(help_text='Informe a condição meteorológica', on_delete=django.db.models.deletion.CASCADE, to='rat.CondicaoMeteorologica', verbose_name='Condição meteorológica')),
                ('condicaosinalizacao', models.ForeignKey(help_text='Informe a condição da sinalização', on_delete=django.db.models.deletion.CASCADE, to='rat.CondicaoSinalizacao', verbose_name='Condição da sinalização')),
                ('condicaovia', models.ForeignKey(help_text='Informe a condição da via', on_delete=django.db.models.deletion.CASCADE, to='rat.CondicaoVia', verbose_name='Condição da via')),
                ('endereco', models.ForeignKey(help_text='Informe o endereço', on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco', verbose_name='Endereço')),
                ('guarnicao', models.ForeignKey(help_text='Informe a guarnição', on_delete=django.db.models.deletion.CASCADE, to='guarnicao.Guarnicao', verbose_name='Guarnição')),
                ('pavimentacao', models.ForeignKey(help_text='Informe o tipo de pavimentação', on_delete=django.db.models.deletion.CASCADE, to='rat.Pavimentacao', verbose_name='Tipo de pavimentação')),
            ],
            options={
                'verbose_name': 'Registro de Acidente de Trânsito',
                'verbose_name_plural': 'Registros de Acidente de Trânsito',
                'db_table': 'rat',
            },
        ),
        migrations.CreateModel(
            name='TipoAcidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Informe o tipo de acidente', max_length=100, verbose_name='Tipo de Acidente')),
            ],
            options={
                'verbose_name': 'Tipo de acidente',
                'verbose_name_plural': 'Tipos de acidente',
                'db_table': 'tipoacidente',
            },
        ),
        migrations.CreateModel(
            name='TracadoVia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracado', models.CharField(help_text='Informe o traçado da via', max_length=100, verbose_name='Traçado da Via')),
            ],
            options={
                'verbose_name': 'Traçado de via',
                'verbose_name_plural': 'Traçados de via',
                'db_table': 'tracadovia',
            },
        ),
        migrations.CreateModel(
            name='RATVeiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('agenterecebedor', models.ForeignKey(blank=True, help_text='Selecione o local destinado', null=True, on_delete=django.db.models.deletion.CASCADE, to='localrecebedor.AgenteRecebedor', verbose_name='Agente recebedor')),
                ('localrecebedor', models.ForeignKey(blank=True, help_text='Selecione o local destinado', null=True, on_delete=django.db.models.deletion.CASCADE, to='localrecebedor.LocalRecebedor', verbose_name='Local destinado')),
                ('observacao', models.ForeignKey(blank=True, help_text='Informe a observação', null=True, on_delete=django.db.models.deletion.CASCADE, to='observacao.Observacao', verbose_name='Observação')),
                ('rat', models.ForeignKey(help_text='Informe o Registro de Acidente de Trânsito', on_delete=django.db.models.deletion.CASCADE, to='rat.RAT', verbose_name='Registro de Acidente de Trânsito')),
                ('veiculo', models.ForeignKey(help_text='Informe o veículo', on_delete=django.db.models.deletion.CASCADE, to='veiculo.Veiculo', verbose_name='Veículo')),
            ],
            options={
                'verbose_name': 'Veículo de RAT',
                'verbose_name_plural': 'Veículos de RAT',
                'db_table': 'ratveiculos',
            },
        ),
        migrations.CreateModel(
            name='RATVeiculoEnvolvidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('envolvido', models.ForeignKey(help_text='Informe o envolvido', on_delete=django.db.models.deletion.CASCADE, to='envolvido.Envolvido', verbose_name='Envolvido')),
                ('ratveiculos', models.ForeignKey(help_text='Informe o veículo', on_delete=django.db.models.deletion.CASCADE, to='veiculo.Veiculo', verbose_name='Veículo')),
            ],
            options={
                'verbose_name': 'Envolvido em veículo de RAT',
                'verbose_name_plural': 'Envolvidos em veículo de RAT',
                'db_table': 'ratveiculoenvolvidos',
            },
        ),
        migrations.CreateModel(
            name='RATObjetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(help_text='Informe uma descrição', verbose_name='Descrição')),
                ('quantidade', models.IntegerField(help_text='Informe a quantidade', verbose_name='Quantidade')),
                ('localconducao', models.CharField(help_text='Informe o local de condução', max_length=100, verbose_name='Local de condução')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('rat', models.ForeignKey(help_text='Informe o Registro de Acidente de Trânsito', on_delete=django.db.models.deletion.CASCADE, to='rat.RAT', verbose_name='Registro de Acidente de Trânsito')),
            ],
            options={
                'verbose_name': 'Objeto de RAT',
                'verbose_name_plural': 'Objetos de RAT',
                'db_table': 'ratobjetos',
            },
        ),
        migrations.AddField(
            model_name='rat',
            name='tipoacidente',
            field=models.ForeignKey(help_text='Informe o tipo de acidente', on_delete=django.db.models.deletion.CASCADE, to='rat.TipoAcidente', verbose_name='Tipo de acidente'),
        ),
        migrations.AddField(
            model_name='rat',
            name='tracadovia',
            field=models.ForeignKey(help_text='Informe o traçado da via', on_delete=django.db.models.deletion.CASCADE, to='rat.TracadoVia', verbose_name='Traçado da via'),
        ),
    ]

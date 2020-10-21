# Generated by Django 3.0.5 on 2020-09-17 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('observacao', '0001_initial'),
        ('guarnicao', '0010_remove_guarnicao_desbloqueadopor'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarnicao',
            name='observacao',
            field=models.ForeignKey(blank=True, help_text='Selecione a observação', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guarnicao_observacao', to='observacao.Observacao', verbose_name='Observação'),
        ),
    ]

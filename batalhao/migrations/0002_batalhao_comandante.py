# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('batalhao', '0001_initial'),
        ('policial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batalhao',
            name='comandante',
            field=models.ForeignKey(blank=True, help_text='Informe o comandante do BPM', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comandante_batalhao', to='policial.Policial', verbose_name='Comandante'),
        ),
    ]

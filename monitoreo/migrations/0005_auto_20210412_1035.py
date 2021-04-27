# Generated by Django 3.1.4 on 2021-04-12 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0004_auto_20210325_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuenteFinanciamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Fuente de Financiamiento',
                'verbose_name_plural': 'Fuentes de Financiamiento',
            },
        ),
        migrations.RemoveField(
            model_name='homologacionfondos',
            name='presupuesto',
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presupuesto', models.FloatField()),
                ('fuente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo.fuentefinanciamiento')),
                ('homologacion_fondos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo.homologacionfondos')),
            ],
            options={
                'verbose_name': 'Presupuesto',
                'verbose_name_plural': 'Presupuesto',
            },
        ),
    ]
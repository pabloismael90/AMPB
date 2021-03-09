# Generated by Django 3.1.4 on 2021-03-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20210304_0957'),
        ('monitoreo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilVocacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Perfil vocacional metodológico',
                'verbose_name_plural': 'Perfiles vocacionales metodológico',
            },
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('edad', models.IntegerField()),
                ('sexo', models.IntegerField(choices=[(1, 'Mujer'), (2, 'Hombre'), (3, 'Otros')])),
                ('procedencia', models.CharField(max_length=250, verbose_name='Lugar de procedencia')),
                ('reside', models.IntegerField(choices=[(1, 'Dentro'), (2, 'Fuera')], verbose_name='Reside dentro o fuera de la comunidad')),
                ('nivel_escolaridad', models.IntegerField(choices=[(1, 'Primaria incompleta'), (2, 'Primaria completa'), (3, 'Secundaria incompleta'), (4, 'Secundaria completa'), (5, 'Universidad incompleta'), (6, 'Universidad completa')], verbose_name='Nivel de escolaridad')),
                ('trabajo', models.IntegerField(choices=[(1, 'Medio tiempo'), (2, 'Tiempo completo'), (3, 'Por proyectos'), (4, 'No trabaja')])),
                ('fecha', models.DateField(verbose_name='Fecha en la que se incorporó a la Escuela')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo.cargo', verbose_name='Cargo en la organización')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.escuela', verbose_name='Organización a la que pertenece')),
                ('talleres', models.ManyToManyField(to='monitoreo.Talleres', verbose_name='Talleres de la Escuela en los que ha participado')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
            },
        ),
        migrations.CreateModel(
            name='Formadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('sexo', models.IntegerField(choices=[(1, 'Mujer'), (2, 'Hombre'), (3, 'Otros')])),
                ('nivel_escolaridad', models.IntegerField(choices=[(1, 'Primaria incompleta'), (2, 'Primaria completa'), (3, 'Secundaria incompleta'), (4, 'Secundaria completa'), (5, 'Universidad incompleta'), (6, 'Universidad completa')], verbose_name='Nivel académico')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.escuela', verbose_name='Organización forestal a la que pertenece')),
                ('perfil_vocacional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo.perfilvocacional', verbose_name='Perfil vocacional metodológico')),
            ],
            options={
                'verbose_name': 'Persona formadora de formadores',
                'verbose_name_plural': 'Personas formadoras de formadores',
            },
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_actualidad_biblioteca_evento_galeria_imagenes_liderazgo'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualidad',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=300),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.4 on 2021-03-23 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20210304_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprendimientos',
            name='escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.escuela', verbose_name='Núcleo'),
        ),
    ]

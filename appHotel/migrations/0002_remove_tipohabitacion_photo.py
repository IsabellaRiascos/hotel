# Generated by Django 2.1.3 on 2018-11-27 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appHotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipohabitacion',
            name='photo',
        ),
    ]
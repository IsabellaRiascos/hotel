# Generated by Django 2.1.3 on 2018-11-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHotel', '0002_remove_tipohabitacion_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipohabitacion',
            name='photo',
            field=models.ImageField(default=1, upload_to='media/photos/'),
            preserve_default=False,
        ),
    ]

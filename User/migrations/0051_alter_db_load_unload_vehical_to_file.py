# Generated by Django 4.0 on 2022-01-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0050_alter_db_load_unload_vehical_from_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='To_File',
            field=models.ImageField(upload_to='To_Company/'),
        ),
    ]

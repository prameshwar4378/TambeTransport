# Generated by Django 4.0 on 2022-01-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_db_load_unload_vehical_driver_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_load_unload_vehical',
            old_name='Driver_Name',
            new_name='first_name',
        ),
    ]

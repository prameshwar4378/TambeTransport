# Generated by Django 4.0 on 2022-01-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0051_alter_db_load_unload_vehical_to_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='From_File',
            field=models.ImageField(null=True, upload_to='From_Company/'),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='To_File',
            field=models.ImageField(null=True, upload_to='To_Company/'),
        ),
    ]
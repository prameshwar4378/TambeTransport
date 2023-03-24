# Generated by Django 4.0 on 2022-01-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_rename_status_delivered_db_load_unload_vehical_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='From_File',
            field=models.FileField(default=None, max_length=250, upload_to='From_Company/'),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=50),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='To_File',
            field=models.FileField(default=None, max_length=250, upload_to='To_Company/'),
        ),
    ]

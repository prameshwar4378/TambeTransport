# Generated by Django 4.0 on 2022-01-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_alter_db_load_unload_vehical_from_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='From_LR_No',
            field=models.IntegerField(),
        ),
    ]

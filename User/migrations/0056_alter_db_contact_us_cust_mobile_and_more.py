# Generated by Django 4.0 on 2022-02-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0055_db_load_unload_vehical_from_file2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_contact_us',
            name='cust_mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Auto_LR_No',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='From_LR_No',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='From_Mobile',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='To_Mobile',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0 on 2022-01-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0039_alter_db_load_unload_vehical_driver_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_load_unload_vehical',
            name='GST_Paid_Per',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='db_load_unload_vehical',
            name='GST_ToPay_Per',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]

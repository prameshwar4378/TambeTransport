# Generated by Django 4.0 on 2022-01-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_alter_db_load_unload_vehical_from_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='AOC_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Door_Delivery_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Freight_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GRAND_TOTAL_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GST_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Hamali_Charges_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Other_Charges_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='ST_Charges_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='SUB_TOTAL_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Value_Subcharge_ToPay',
            field=models.IntegerField(default='', null=True),
        ),
    ]

# Generated by Django 4.0 on 2022-01-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0022_alter_db_load_unload_vehical_from_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='AOC_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='AOC_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Actual_Weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Charged_Weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Delivery_At',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Door_Delivery_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Door_Delivery_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Freight_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Freight_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GRAND_TOTAL_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GRAND_TOTAL_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GST_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GST_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Hamali_Charges_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Hamali_Charges_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Item_Type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Other_Charges_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Other_Charges_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='ST_Charges_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='ST_Charges_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='SUB_TOTAL_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='SUB_TOTAL_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='To_Mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Value_Subcharge_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Value_Subcharge_ToPay',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

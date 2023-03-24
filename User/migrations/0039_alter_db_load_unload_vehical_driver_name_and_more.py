# Generated by Django 4.0 on 2022-01-22 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('User', '0038_alter_db_load_unload_vehical_driver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Driver_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Admin', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GRAND_TOTAL_Paid',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='GRAND_TOTAL_ToPay',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
    ]
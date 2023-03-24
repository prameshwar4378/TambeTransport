# Generated by Django 4.0 on 2022-01-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0052_alter_db_load_unload_vehical_from_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_contact_us',
            name='cust_message',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='db_contact_us',
            name='cust_mobile',
            field=models.IntegerField(max_length=999999999999),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='E_Way_Bill',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='To_File',
            field=models.ImageField(default='static/default.png', null=True, upload_to='To_company/'),
        ),
    ]

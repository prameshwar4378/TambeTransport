# Generated by Django 4.0 on 2022-01-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0041_alter_db_load_unload_vehical_gst_paid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='db_load_unload_vehical',
            name='Item_Type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
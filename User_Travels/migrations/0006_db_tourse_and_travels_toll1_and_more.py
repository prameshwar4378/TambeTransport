# Generated by Django 4.0 on 2022-02-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Travels', '0005_alter_db_tourse_and_travels_closing_km_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll1_photo',
            field=models.ImageField(blank=True, null=True, upload_to='toll1'),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll2_photo',
            field=models.ImageField(blank=True, null=True, upload_to='toll2'),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll3_photo',
            field=models.ImageField(blank=True, null=True, upload_to='toll3'),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll4_photo',
            field=models.ImageField(blank=True, null=True, upload_to='toll4'),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll5_photo',
            field=models.ImageField(blank=True, null=True, upload_to='toll5'),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_tourse_and_travels',
            name='toll6_photo',
            field=models.ImageField(blank=True, null=True, upload_to='toll6'),
        ),
        migrations.AlterField(
            model_name='db_tourse_and_travels',
            name='order_by',
            field=models.ImageField(blank=True, null=True, upload_to='order_by'),
        ),
    ]

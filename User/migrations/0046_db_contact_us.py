# Generated by Django 4.0 on 2022-01-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0045_delete_db_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_mobile', models.IntegerField()),
                ('cust_message', models.CharField(max_length=50)),
            ],
        ),
    ]
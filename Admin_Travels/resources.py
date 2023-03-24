
from dataclasses import fields
from lib2to3.pgen2.driver import Driver
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
from User_Travels.models import DB_Tourse_and_Travels


class DB_Tourse_Travels_Resource(resources.ModelResource):
    driver_name=fields.Field(
        column_name='driver_name',
        attribute='driver_name',
        widget=ForeignKeyWidget(User,'first_name'))

    class Meta:
        model = DB_Tourse_and_Travels
        
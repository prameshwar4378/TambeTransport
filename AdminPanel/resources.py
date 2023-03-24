
from dataclasses import fields
from lib2to3.pgen2.driver import Driver
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from AdminPanel.models import DB_Company_List
from User.models import DB_Load_Unload_Vehical
from django.contrib.auth.models import User


class DB_Load_Unload_Vehical_Resource(resources.ModelResource):
    From_company = fields.Field(
        column_name='From_company',
        attribute='From_company',
        widget=ForeignKeyWidget(DB_Company_List, 'Company_Name'))

    To_company = fields.Field(
        column_name='To_company',
        attribute='To_company',
        widget=ForeignKeyWidget(DB_Company_List, 'Company_Name'))

    Driver_Name=fields.Field(
        column_name='Driver_Name',
        attribute='Driver_Name',
        widget=ForeignKeyWidget(User,'first_name')
    )
    class Meta:
        model = DB_Load_Unload_Vehical
        


class User_Resource(resources.ModelResource):

    class Meta:
        model = User
        fields=['id','username','first_name','last_name','email','last_login','date_joined']
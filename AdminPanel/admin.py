from django.contrib import admin
from .models import DBUser,DB_Company_List
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.widgets import ForeignKeyWidget
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('emp_name','emp_id_no')
admin.site.register(DBUser,StudentAdmin)

# class CompanyListAdmin(admin.ModelAdmin):
#     list_display=('emp_name',)

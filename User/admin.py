from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import DB_Load_Unload_Vehical,DB_Contact_Us

# Register your models here.
class AdminDetails(admin.ModelAdmin):
    list_display=('Driver_Name','From_LR_No','Vehical_No')
admin.site.register(DB_Load_Unload_Vehical,AdminDetails)


class EnquiryAdmin(admin.ModelAdmin):
    list_display=('cust_name','cust_mobile','cust_message')
admin.site.register(DB_Contact_Us,EnquiryAdmin)

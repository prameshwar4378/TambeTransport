from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_home,name="travel_admin_home"),
    path('admin_travel_all_records',views.admin_travel_all_records,name="admin_travel_all_records"),
    path('print_travel_receipt/<int:id>',views.print_travel_receipt,name="print_travel_receipt"),  
    path('update_travel_record/<int:id>',views.update_travel_record,name="update_travel_record"),
    path('delete_travel_record/<int:id>',views.delete_travel_record,name="delete_travel_record"),
    path('travel_export_excel/',views.travel_export_excel, name="travel_export_excel"), 
]

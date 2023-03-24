"""TambeTransport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path("",views.AdminHome,name="adminhome"),
    path('export_data/',views.export_data, name="export_data"),
    path('export_users/',views.export_users, name="export_users"),
    # path("admin_login/",views.admin_login, name="admin_login"),
    path("admin_logout/",views.admin_logout, name="admin_logout"),
    path('manage_user/',views.Manageuser,name="manageuser"),
    path('manage_company/',views.Manage_Company,name="managecompany"),
    path('update_company/<int:id>/',views.Update_Company_Name_List,name="updatecompany"),
    path('delete_company/<int:id>/',views.Delete_Company_Name_List,name="deletecompany"),  
    path('admin_pending_records/',views.admin_pending_records,name="admin_pending_records"), 
    path('admin_vehical_records/',views.AdminVehicalRecords,name="admin_vehical_records"),
    path('delete_user/<int:id>/',views.delete_data, name='delete_data'),
    path('delete_vehical_record/<int:id>',views.delete_vehical_record,name="delete_vehical_record"),
    path('update_vehical_record/<int:id>',views.update_vehical_records,name="update_vehical_record"),
    path('<int:id>/',views.update_user_data, name='update_user_data'),
    path('gen_lr/<int:id>/',views.generate_lr,name='generate_lr'), 
    path('print_lr/<int:id>/',views.print_lr,name='print_lr'),   
    path('update_lr/<int:id>/',views.update_lr,name='update_lr'),   
    path('enquiry/',views.enquiry,name='enquiry'),   
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_home,name="travel_user_home"), 
    path('new_entry/',views.new_entry,name="travel_new_entry"), 
    path('pending_records/',views.pending_records,name="travel_pending_records"), 
    path('droped_records/',views.droped_records,name="droped_records"),  
    path('drop_cust/<int:id>',views.drop_cust,name="drop_cust"), 
    path('manage_diesel/<int:id>',views.manage_diesel,name="manage_diesel"), 

]

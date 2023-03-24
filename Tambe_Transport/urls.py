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
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from AdminPanel import views as AV
from User import views as UV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',AV.index, name='index'),
    path("Admin_Home/",include('AdminPanel.urls'),name="adminhome"),
    path('admin_login/',AV.admin_login,name='admin_login'),
    path('admin_choose_dashboard/',AV.admin_choose_dashboard,name='admin_choose_dashboard'),  
    path('admin_travels/',include('Admin_Travels.urls'),name="admin_travel"), 
    path('user_choose_dashboard/',UV.user_choose_dashboard,name='user_choose_dashboard'), 
    path('user_travels/',include('User_Travels.urls'),name="user_travel"),  
    path('user/',include('User.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

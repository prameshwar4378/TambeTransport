from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='user_home'),
    path("user_login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path('new_entry/',views.new_entry, name="new_entry"),
    path('pending_records/',views.pending_records, name="pending_records"),
    path('delivered_records/',views.delivered_records, name="delivered_records"),
    path('<int:id>/',views.deliver_form, name='deliver_form'),
    # path('gen_lr/<int:id>/',views.generate_lr,name='generate_lr'),
    path('contact_us/',views.contact_us,name='contact_us'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
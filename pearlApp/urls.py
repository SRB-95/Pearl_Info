from django.urls import path
from . import views
#Access user profile_pic from project instead of DB
from  django.conf import settings
from django.conf.urls.static import static

app_name = 'pearlApp'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('user_logout/', views.user_logout, name = 'user_logout'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('service/', views.service, name = 'service'),
    path('add_profile/', views.add_profile, name = 'add_profile'),   
    path('user_profile/', views.user_profile, name = 'user_profile'),   
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
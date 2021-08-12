from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path('', views.search , name='users-search'),
    path('login/', views.login , name='login'),
    path('profile/', views.profile, name='profile') ,
    path('logout/', views.login , name='logout'),
    path('help/', views.help , name='help'),
    path('register/', views.register, name='register'),
    path('login/', views.help , name='help')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
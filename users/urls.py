from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.search , name='users-search'),
    path('login/', views.login , name='login'),
    path('logout/', views.login , name='logout'),
    path('help/', views.help , name='help'),
    path('register/', views.register, name='register'),
    path('login/', views.help , name='help')
]
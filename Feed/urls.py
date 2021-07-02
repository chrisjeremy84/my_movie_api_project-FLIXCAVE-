from django.urls import path
from . import views

urlpatterns = [
    path('', views.Feed , name='blog-feed'),
    path('about/', views.About , name='about')
]
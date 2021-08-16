from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),


]
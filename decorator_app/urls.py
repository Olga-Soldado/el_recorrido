from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home),
    path('login',views.login),
    path('menu',views.main),
    path('register',views.register),
    path('logout',views.logout),
   
]
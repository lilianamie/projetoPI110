from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('administrador/', views.administrador, name='administrador'),
    path('usuario/', views.usuario, name='usuario'),
    #path('logout/', views.logout, name='logout'),
    path('login/',views.login, name='login'),
    path('admin/',admin.site.urls)
]
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('experiencias/', views.experiencias, name='experiencias'),
    path('cursos/', views.cursos, name='cursos'),
    path('sobre/', views.sobre, name='sobre'),
    path('logout/', views.logout, name='logout')
]
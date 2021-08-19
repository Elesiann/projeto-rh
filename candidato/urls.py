from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('experiencias/', views.experiencias, name='experiencias'),
    path('cursos/', views.cursos, name='cursos'),
    path('sobre/', views.sobre, name='sobre')
]
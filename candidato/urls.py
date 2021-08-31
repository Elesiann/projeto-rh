from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('experiencias/', views.experiencias, name='experiencias'),
    path('cursos/', views.cursos, name='cursos'),
    path('sobre/', views.sobre, name='sobre'),
    path('logout/', views.logout, name='logout'),
    path('botao_proximo/', views.botao_proximo, name='botao_proximo'),
    path('botao_finalizar/', views.botao_finalizar, name='botao_finalizar'),
    path('administrador/', views.administrador, name='administrador'),
]

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('login/', include('candidato.urls')),
    path('registro/', include('candidato.urls')),
    path('experiencias/', include('candidato.urls')),
    path('cursos/', include('candidato.urls')),
    path('sobre/', include('candidato.urls')),
    path('admin/', admin.site.urls),
]

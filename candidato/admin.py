from django.contrib import admin
from .models import Cursos, Experiencias, Registro, Sobre


admin.site.register(Registro) # Caso queira administrador adicionar pessoas ao admin
admin.site.register(Sobre)
admin.site.register(Experiencias)
admin.site.register(Cursos)

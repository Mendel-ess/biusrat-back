from django.contrib import admin
from .models import Usuarios, Alimentacion, Ejercicio, Entrenamiento, Comida, Programa, Sleep
# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Alimentacion)
admin.site.register(Ejercicio)
admin.site.register(Entrenamiento)
admin.site.register(Comida)
admin.site.register(Programa)
admin.site.register(Sleep)



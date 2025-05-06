from django.contrib import admin

# Register your models here.
from .models import Producto  # Asegúrate de que el modelo Estudiante esté importado

admin.site.register(Producto)
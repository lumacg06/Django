from django.db import models

# Create your models here.

class Producto(models.Model):
    tipo_prenda = models.CharField(max_length=100)  # Ejemplo: Camiseta, Pantalón, etc.
    talla = models.CharField(max_length=10)         # Ejemplo: S, M, L, XL
    genero = models.CharField(
        max_length=10,
        choices=[
            ('Hombre', 'Hombre'),
            ('Mujer', 'Mujer'),
            ('Unisex', 'Unisex')
        ]
    )
    marca = models.CharField(max_length=100)       # Ejemplo: Nike, Adidas, etc.
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    fecha_agregado = models.DateTimeField(auto_now_add=True)       # Fecha de creación del registro

    def __str__(self):
        return f"{self.tipo_prenda} - {self.marca} - {self.talla}"

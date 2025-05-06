from django.shortcuts import redirect, render
from .models import Producto


def lista_productos(request):
    if request.method == 'POST':
        tipo_prenda = request.POST.get('tipo_prenda')
        talla = request.POST.get('talla')
        genero = request.POST.get('genero')
        marca = request.POST.get('marca')
        precio = request.POST.get('precio')
        Producto.objects.create(
            tipo_prenda=tipo_prenda,
            talla=talla,
            genero=genero,
            marca=marca,
            precio=precio
        )

        return redirect('lista_productos')

    
    productos = Producto.objects.all()

    
    return render(request, 'lista_productos.html', {'productos': productos})

# Vista para agregar un producto (opcional)
def agregar_producto(request):
    if request.method == 'POST':
        tipo_prenda = request.POST.get('tipo_prenda')
        talla = request.POST.get('talla')
        genero = request.POST.get('genero')
        marca = request.POST.get('marca')
        precio = request.POST.get('precio')

        # Creación del nuevo producto
        Producto.objects.create(
            tipo_prenda=tipo_prenda,
            talla=talla,
            genero=genero,
            marca=marca,
            precio=precio
        )

        return redirect('lista_productos')  

    return render(request, 'agregar_producto.html')  

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.tipo_prenda = request.POST.get('tipo_prenda')
        producto.talla = request.POST.get('talla')
        producto.genero = request.POST.get('genero')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.save()
        return redirect('lista_productos')
    return render(request, 'editar_producto.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

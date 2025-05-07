from django.shortcuts import redirect, render
from .models import Producto

# Vista que muestra la lista de productos y permite agregar un producto desde la misma vista si se envía un POST
def lista_productos(request):
    if request.method == 'POST':
        tipo_prenda = request.POST.get('tipo_prenda')
        talla = request.POST.get('talla')
        genero = request.POST.get('genero')
        marca = request.POST.get('marca')
        precio = request.POST.get('precio')
        # Se crea un nuevo objeto Producto
        Producto.objects.create(
            tipo_prenda=tipo_prenda,
            talla=talla,
            genero=genero,
            marca=marca,
            precio=precio
        )
        return redirect('lista_productos')
     # Si la petición es GET, obtiene todos los productos 
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

# Vista para mostrar un formulario dedicado para agregar productos
def agregar_producto(request):
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
    return render(request, 'agregar_producto.html')  

# Vista para editar un producto existente
def editar_producto(request, id):
    # Se obtiene el producto por su ID
    producto = Producto.objects.get(id=id) 
    if request.method == 'POST':
        producto.tipo_prenda = request.POST.get('tipo_prenda')
        producto.talla = request.POST.get('talla')
        producto.genero = request.POST.get('genero')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        # Guarda los cambios en la base de datos
        producto.save()
        return redirect('lista_productos')
    return render(request, 'editar_producto.html', {'producto': producto})

# Vista para eliminar un producto existente
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        # Elimina el producto de la base de datos
        producto.delete() 
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

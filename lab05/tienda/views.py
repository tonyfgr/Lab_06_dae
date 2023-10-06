from django.shortcuts import render

# Create your views here.
from .models import Cliente, Categoria, Producto

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tienda/lista_clientes.html', {'clientes': clientes})

def cambiar_precio(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        categoria_id = request.POST.get('categoria')
        nuevo_precio = float(request.POST.get('nuevo_precio'))
        productos = Producto.objects.filter(categoria_id=categoria_id)
        productos.update(precio=nuevo_precio)
    categorias_con_productos = []
    for categoria in categorias:
        productos = Producto.objects.filter(categoria=categoria)
        categorias_con_productos.append({'categoria': categoria, 'productos': productos})

    return render(
        request,
        'tienda/cambiar_precio.html',  
        {'categorias_con_productos': categorias_con_productos}
    )

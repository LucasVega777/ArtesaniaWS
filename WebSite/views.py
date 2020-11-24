from django.shortcuts import render
from .models import Producto


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


def productos(request):
    lista_productos = Producto.objects.order_by("nombre")
    nombre_productos = {'productos' : lista_productos}
    return render(request, 'productos.html', nombre_productos)

# def contacto(request):
#     return render(request, 'contacto.html')


from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from carritoApp.models import Producto
from carritoApp.carrito import Carrito
from .forms import UserRegistrationForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = UserRegistrationForm()
    return render(request, 'singup.html', {'form': form})
              




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Cambia 'home' por la URL a la que quieres redirigir después del login
    else:
        form = AuthenticationForm()
    return render(request, 'singin.html', {'form': form})

def cerrarSesion(request):
    logout(request)
    return redirect('index') 



#CARRITO
def tienda(request):
    productos = Producto.objects.all()
    return render(request,'tienda.html',{'productos':productos})
def carritop(request):
    return render(request,'carrito.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('Tienda')

def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto =Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('carritop')

def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto =Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('carritop')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('carritop')




      

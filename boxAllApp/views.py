from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from .forms import UsuarioForm
from django.contrib.auth.models import User
from carritoApp.models import Producto
from carritoApp.carrito import Carrito
from .forms import SinginForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

    
def singup(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            # Redirigir a alguna página de éxito o a donde sea necesario después del registro

            return redirect('index')
        
    else:
        form = UsuarioForm
        
    
    return render(request, 'singup.html', {'form': form})
              
def index(request):

    return render(request,'index.html')


def cerrarSesion(request):
    logout(request)
    return redirect('index') 

def singin(request):
    if request.method == 'POST':
        form = SinginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']

            user = authenticate(request, username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                # Redirigir a la página de inicio o a otra página deseada
                return redirect('inicio')
            else:
                # Manejar el caso de credenciales inválidas
                return HttpResponse('Credenciales inválidas')
        else:
            # El formulario no es válido, puedes manejar este caso como desees
            return HttpResponse('Formulario inválido')

    else:
        # Si la solicitud no es POST, mostrar el formulario vacío
        form = SinginForm()

    return render(request, 'singin.html', {'form': form})




#CARRITO
def tienda(request):
    productos = Producto.objects.all()
    return render(request,'tienda.html',{'productos':productos})
def carritop(request):
    productos = Producto.objects.all()
    return render(request,'carrito.html',{'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('Tienda')

def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto =Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('Tienda')

def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto =Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('Tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('Tienda')




      

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import UsuarioForm

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
        form = UsuarioForm()
        
    
    return render(request, 'singup.html', {'form': form})
              
def index(request):

    return render(request,'index.html')


def cerrarSesion(request):
    logout(request)
    return redirect('index') 

def singin(request):
    if request.method == 'GET':
        return render(request,'singin.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['correo'],password=request.POST['contraseña'])

        if user is None:
             return render(request,'singin.html',{
            'form':AuthenticationForm,
            'error': 'Username o Password incorrecto'
        })

        else:
            login(request,user)
            return redirect('index')

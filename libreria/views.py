from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm , UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from .models import Libro , Avatar
from django.contrib.auth import logout


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

@login_required
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario}) 

@login_required
def editar(request,id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

@login_required
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

def loginvista(request):
    return render(request, 'paginas/loginvista.html')

def registrarvista(request):
    return render(request, 'paginas/registrarvista.html')

    

def leermas(request):
    return render(request, 'paginas/leermas.html')


#LOGIN

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                
            

            else:
                return render(request , "base.html" , {"mensaje": "Error, datos incorrectos"}) 

        else:
            return render(request , "base.html" , {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "paginas/loginvista.html" , {"form":form})


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            

    else:
        form = UserCreationForm()
    return render(request , "paginas/registrarvista.html" , {"form":form})

def editarperfil(request):

    usuario = request.user

    if request.method == "POST":

        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request , "paginas/inicio.html")

    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})

    return render (request , "paginas/editarperfil.html" , {"mi_formulario":mi_formulario , "usuario":usuario})

def logoutUser(request):
    logout(request)      
    template = 'paginas/logout.html'
    return render (request, template )
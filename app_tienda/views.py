from django.shortcuts import render
from app_tienda.forms import *
from app_tienda.models import *

# Create your views here.

def vista_inicio(request):
    return render(request, "app_tienda/index.html")

def vista_registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = Usuario(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"], nombre_usuario = data["nombre_usuario"], contrasenia = data["contrasenia"])
            user.save()
    formulario = UsuarioForm()
    return render(request, "app_tienda/registro.html", {"formulario": formulario})

def vista_cafe(request):
    if request.method == "POST":
        formulario = CafeForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cafe = Cafe(nombre_cafe = data["nombre_cafe"], precio = data["precio"], descripcion = data["descripcion"])
            cafe.save()
    formulario = CafeForm()
    return render(request, "app_tienda/cafe.html" , {"formulario": formulario})

def vista_tortas(request):
    if request.method == "POST":
        formulario = TortaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            torta = Torta(nombre_torta = data["nombre_torta"], precio = data["precio"], descripcion = data["descripcion"])
            torta.save()
    formulario = TortaForm()
    return render(request,"app_tienda/tortas.html",  {"formulario": formulario})

def vista_inicio_sesion(request):
    return render(request, "app_tienda/iniciar_sesion.html")

def vista_busqueda(request):
    return render(request, "app_tienda/busqueda.html")

def vista_resultado(request): 
    nombre_torta = request.GET["nombre_torta"]
    tortas = tortas.objects.filter(nombre_torta__icontains=nombre_torta)
    return render(request, "app_tienda/resultados_busqueda.html", {"torta": tortas})
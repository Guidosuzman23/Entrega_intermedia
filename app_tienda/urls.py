from django.urls import path
from app_tienda.views import *

urlpatterns = [
    path("inicio/", vista_inicio, name = "app_tienda-inicio"),
    path("registro/", vista_registro, name = "app_tienda-registro"),
    path("cafe/", vista_cafe, name = "app_tienda-cafe"),
    path("torta/", vista_tortas, name= "app_tienda-tortas"),
    path("iniciar_sesion/", vista_inicio_sesion, name="app_tienda-iniciar-sesion"),
    path("busqueda/", vista_busqueda, name="app_tienda-busqueda"),
    path("resultado_busqueda/", vista_resultado, name="app_tienda-resultado"),

]
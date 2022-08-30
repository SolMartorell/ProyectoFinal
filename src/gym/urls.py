from django.urls import path
from gym.views import *

urlpatterns = [
    path("", inicio, name= "Inicio"),
    path("sobre_mi/", sobre_mi, name= "Sobre mi"),
    
    path("actividades/", actividades, name= "Actividades"),
    path("actividades/editar/<id_actividad>", editar_actividad, name="editar_actividad"),
    path("actividades/borrar/<id_actividad>", borrar_actividad, name="borrar_actividad"),
    path("actividades/buscar/", buscar_actividad, name="buscar_actividad"),
    path("actividades/<pk>", ActividadesDetail.as_view(), name="detalle_actividad"),
        
    path("socios/", socios, name="Socios"),
    path("socios/editar/<id_socio>", editar_socio,name="editar_socio"),
    path("socios/borrar/<id_socio>", borrar_socio, name="borrar_socio"),
    path("socios/buscar/", buscar_socio, name="buscar_socio"),
    path("socios/<pk>", SociosDetail.as_view(), name="detalle_socio"),
  
    path("planes/", planes, name="Planes"),
    path("planes/editar/<id_plan>", editar_plan, name="editar_plan"),
    path("planes/borrar/<id_plan>", borrar_plan, name="borrar_plan"),
    path("planes/buscar/", buscar_plan, name="buscar_plan"),
    path("planes/<pk>", PlanesDetail.as_view(), name="detalle_plan")
]

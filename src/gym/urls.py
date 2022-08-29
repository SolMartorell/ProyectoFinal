from django.urls import path
from gym.views import *

urlpatterns = [
    path("", inicio, name= "Inicio"),
    path("sobre_mi/", sobre_mi, name= "Sobre mi"),
    
    path("actividades/", actividades, name= "Actividades"),
    path("actividades/editar/<id_actividad>", editar_actividad, name="editar_actividad"),
    path("actividades/borrar/<id_actividad>", borrar_actividad, name="borrar_actividad"),
    path("resultados/", buscar_actividad, name="buscar_actividad"),
    path("actividades/<pk>", ActividadesDetail.as_view(), name="detalle_actividad"),
        
    path("socios/", SociosList.as_view(), name="Socios"),
    path("socios/crear", SociosCreate.as_view(), name="crear_socio"),
    path("socios/editar/<pk>", SociosUpdate.as_view(), name="editar_socio"),
    path("socios/borrar/<pk>", SociosDelete.as_view(), name="borrar_socio"),
    path("socios/<pk>", SociosDetail.as_view(), name="detalle_socio"),
    path("resultados/", buscar_socio, name="buscar_socio"),
    
    path("planes/", PlanesList.as_view(), name="Planes"),
    path("planes/editar/<pk>", PlanesUpdate.as_view(), name="editar_plan"),
    path("planes/borrar/<pk>", PlanesDelete.as_view(), name="borrar_plan"),
    path("planes/<pk>", PlanesDetail.as_view(), name="detalle_plan"),
    path("resultados/", buscar_plan, name="buscar_plan"),
    path("planes/crear", PlanesCreate.as_view(), name="planes_create")
]

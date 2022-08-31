from django.urls import path
from registro.views import *


urlpatterns = [
    path('registrarse/', registrarse, name="registrarse"),
    path("editar/", editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name="agregar_avatar"),
    path("contacto/", contacto, name= "Contacto"),
    path("contacto/borrar/<id_contacto>", borrar_contacto, name="borrar_contacto")
]
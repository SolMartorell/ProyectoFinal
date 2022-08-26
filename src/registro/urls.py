from django.urls import path
from registro.views import registrarse, editar_usuario, agregar_avatar, contacto

urlpatterns = [
    path('registrarse/', registrarse, name="registrarse"),
    path("editar/", editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name="agregar_avatar"),
    path("contacto/", contacto, name= "Contacto"),
]
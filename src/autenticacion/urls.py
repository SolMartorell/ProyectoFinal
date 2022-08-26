from django.urls import path
from autenticacion.views import iniciar_sesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', LogoutView.as_view(template_name="autenticacion/logout.html"), name="cerrar_sesion")
]
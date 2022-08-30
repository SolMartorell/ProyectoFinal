from django import forms
from django.forms import Form, CharField, EmailField, PasswordInput, ImageField, DateTimeField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from registro.models import Contacto


class UserCustomCreationForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { "username": "", "email": "", "password1": "", "password2": "" }


class UserEditForm(UserCreationForm):
    first_name = CharField(label="Nombre")
    last_name = CharField(label="Apellido")
    email = EmailField(label="Correo nuevo")
    password1 = CharField(label="Contraseña nueva", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña nueva", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {"email": "", "password1": "", "password2": "" }


class AvatarForm(Form):
    imagen = ImageField()

class ContactoFormulario(Form):
    nombre = CharField(max_length=100)
    email = EmailField()
    mensaje = CharField(max_length=500)


    class Meta:
        model = Contacto
        fields = ["nombre", "email", "mensaje"]
 


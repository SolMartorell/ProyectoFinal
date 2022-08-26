from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registro.forms import UserCustomCreationForm
from registro.forms import UserEditForm, AvatarForm
from registro.models import Avatar


def registrarse(request):

    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "registro/registrarse.html", {"form": formulario})
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("Inicio")
        else:
            context = {
                "error": "FORMULARIO NO VALIDO",
                "form": formulario
            }
            return render(request, "registro/registrarse.html", context)







def contacto (request):
    return render(request, "registro/contacto.html")



@login_required
def editar_usuario(request):

    if request.method == "GET":
        form = UserEditForm(initial={"first_name": request.user.first_name, "last_name": request.user.last_name, "email": request.user.email})
        return render(request, "registro/editar_usuario.html", {"form": form})
    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
            return redirect("Inicio")
        else:
            return render(request, "registro/editar_usuario.html", {"form": form})


@login_required
def agregar_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form": form}
        return render(request, "registro/agregar_avatar.html", contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.filter(username=request.user.username).first()
            avatar = Avatar(usuario=usuario,imagen=data["imagen"])

            avatar.save()
            return redirect("Inicio")
            
        contexto = {"form": form}
        return render(request, "registro/agregar_avatar.html", contexto)
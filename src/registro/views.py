from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registro.forms import UserEditForm, AvatarForm, ContactoFormulario, UserCustomCreationForm
from registro.models import Avatar, Contacto



def registrarse(request):

    if request.method == "GET":
        formulario = UserCustomCreationForm()
        contexto = {
            "form": formulario
            }
        return render(request, "registro/registrarse.html", contexto)
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("Inicio")
        else:
            contexto = {
                "error": "FORMULARIO NO VALIDO",
                "form": formulario
            }
            return render(request, "registro/registrarse.html", contexto)


@login_required
def editar_usuario(request):

    if request.method == "GET":
        formulario= UserEditForm(initial={"first_name": request.user.first_name, "last_name": request.user.last_name, "email": request.user.email})
        
        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "formulario": formulario,
            "imagen": imagen
        }

        return render(request, "registro/editar_usuario.html", contexto)
    
    else:
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
            return redirect("Inicio")
        
        else:
            return render(request, "registro/editar_usuario.html", {"formulario": formulario})


@login_required
def agregar_avatar(request):
   
    if request.method == "POST":
        
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            
            usuario = request.user
            avatar = Avatar.objects.filter(usuario=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()
            
            else:
                avatar = Avatar(usuario=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
        
        return redirect("Inicio")

    else:
        formulario = AvatarForm()

        contexto = {
            "formulario": formulario
        }

        return render(request, "registro/agregar_avatar.html", contexto)
    

@login_required
def contacto (request):
    contactos = Contacto.objects.all()
    
    if request.method == "GET":
        formulario = ContactoFormulario()

        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "contactos": contactos,
            "formulario": formulario,
            "imagen": imagen
        }
        
        return render(request, "registro/contacto.html", contexto)

    else:
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():        
            data = formulario.cleaned_data
        
            nombre = data.get("nombre")
            email = data.get("email")
            mensaje = data.get("mensaje")
                   
            contacto = Contacto(nombre=nombre, email=email, mensaje=mensaje)
            contacto.save()

        formulario = ContactoFormulario()
        
        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "contactos": contactos,
            "formulario": formulario,
            "imagen": imagen
        }
        
        return render(request, "registro/contacto.html", contexto)

@login_required
def borrar_contacto(request, id_contacto):
    try:
        contacto = Contacto.objects.get(id=id_contacto)
        contacto.delete()
        return redirect("Contacto")
    except:
        return redirect("Inicio")


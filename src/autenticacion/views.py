from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate




def iniciar_sesion(request):
    
    if request.method == "GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }

        return render(request, "autenticacion/login.html", context)

    else:
        formulario  = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("Inicio")
            
        
        context = {
            "error": "FORMULARIO NO VALIDO",
            "form": formulario
        }
        return render(request, "autenticacion/login.html", context)



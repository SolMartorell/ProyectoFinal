from django.shortcuts import render, redirect
from django.http import HttpResponse
from gym.models import Actividades, Socios, Planes
from gym.forms import *
from django.views.generic.detail import DetailView
from registro.models import Avatar
from django.contrib.auth.decorators import login_required



# INICIO

def inicio(request):

    context = {
        "mensaje": "Página de inicio"    
    }

    if not request.user.is_anonymous:
        avatares = Avatar.objects.filter(usuario = request.user).last()
        context.update({"avatares": avatares})

    return render(request, "gym/index.html", context)

# SOBRE MI

def sobre_mi (request):
    context = {
        "mensaje1": "Mi nombre es María Sol Martorell, tengo 36 años y este es mi primer curso de programación.", 
        "mensaje2": "Soy Lic. en Química y Tecnología Ambiental, y busco potenciar mi desarrollo profesional metiéndome en el mundo IT",
        "mensaje3": "Un camino totalmente desconocido pero con muchas ganas de recorrerlo y aprender! Espero que sea el primero de muchos otros!"
    }
    return render(request, "gym/sobre_mi.html", context)



# ACTIVIDADES

@login_required
def actividades (request):
    actividades = Actividades.objects.all()

    if request.method == "GET":
        formulario = ActividadesFormulario()
    
        context = {
            "actividades":actividades,
            "formulario": formulario
        }
        return render(request, "gym/actividades/actividades.html", context)

    else:
        formulario = ActividadesFormulario(request.POST)
        if formulario.is_valid():        
            data = formulario.cleaned_data
            
            nombre = data.get("nombre")
            dia = data.get("dia")
            horario = data.get("horario")
            cupo = data.get("cupo")
            
            actividad = Actividades(nombre=nombre, dia=dia, horario=horario, cupo=cupo)
            actividad.save()

        formulario = ActividadesFormulario()
        context = {
            "actividades": actividades,
            "formulario": formulario
        }
        return render(request, "gym/actividades/actividades.html", context)

@login_required
def borrar_actividad(request, id_actividad):
    try:
        actividad = Actividades.objects.get(id=id_actividad)
        actividad.delete()
        return redirect("Actividades")
    except:
        return redirect("Inicio")

@login_required
def editar_actividad(request, id_actividad):

    if request.method == "GET":
        formulario = ActividadesFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "gym/actividades/actividades_editar.html", contexto)
    
    else:
        formulario = ActividadesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                actividad = Actividades.objects.get(id=id_actividad)

                actividad.nombre = data.get("nombre")
                actividad.dia = data.get("dia")
                actividad.horario = data.get("horario")
                actividad.cupo = data.get("cupo")
                actividad.save()
            except:
                return HttpResponse("Error en la actualización")
   
        return redirect("Actividades")

@login_required
def buscar_actividad(request):

    actividad_nombre = request.GET.get("actividad", None)

    if not actividad_nombre:
        return HttpResponse("No indicaste ningún nombre")

    actividades_lista = Actividades.objects.filter(nombre__icontains=actividad_nombre)
    return render(request, "gym/actividades/actividades_resultado_busqueda.html", {"actividades": actividades_lista})

class ActividadesDetail(DetailView):
    model = Actividades
    template_name = "gym/actividades/actividades_detalle.html"


# SOCIOS

@login_required
def socios (request):
    socios = Socios.objects.all()

    if request.method == "GET":
        formulario = SociosFormulario()
    
        context = {
            "socios": socios,
            "formulario": formulario
        }
        return render(request, "gym/socios/socios.html", context)

    else:
        formulario = SociosFormulario(request.POST)
        if formulario.is_valid():        
            data = formulario.cleaned_data
            
            nombre = data.get("nombre")
            apellido = data.get("apellido")
            email = data.get("email")
            cuota_paga = data.get("cuota_paga")
            
            socio = Socios(nombre=nombre, apellido=apellido, email=email, cuota_paga=cuota_paga)
            socio.save()

        formulario = SociosFormulario()
        context = {
            "socios": socios,
            "formulario": formulario
        }
        return render(request, "gym/socios/socios.html", context)

@login_required
def borrar_socio(request, id_socio):
    try:
        socio = Socios.objects.get(id=id_socio)
        socio.delete()
        return redirect("Socios")
    except:
        return redirect("Inicio")

@login_required
def editar_socio(request, id_socio):

    if request.method == "GET":
        formulario = SociosFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "gym/socios/socios_editar.html", contexto)
    
    else:
        formulario = SociosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                socio= Socios.objects.get(id=id_socio)

                socio.nombre = data.get("nombre")
                socio.apellido = data.get("apellido")
                socio.email = data.get("email")
                socio.cuota_paga= data.get("cuota_paga")

                socio.save()
            except:
                return HttpResponse("Error en la actualización")
   
        return redirect("Socios")

@login_required
def buscar_socio(request):

    socio_nombre = request.GET.get("nombre", None)
    
    if not socio_nombre:
        return HttpResponse("No indicaste ningún nombre")

    socios_lista = Socios.objects.filter(nombre__icontains=socio_nombre)
    
    return render (request, "gym/socios/socios_resultado_busqueda.html", {"socios": socios_lista})



class SociosDetail(DetailView):
    model = Socios
    template_name = "gym/socios/socios_detalle.html"


# PLANES

@login_required
def planes (request):
    planes = Planes.objects.all()

    if request.method == "GET":
        formulario = PlanesFormulario()
    
        context = {
            "planes": planes,
            "formulario": formulario
        }
        return render(request, "gym/planes/planes.html", context)

    else:
        formulario = PlanesFormulario(request.POST)
        if formulario.is_valid():        
            data = formulario.cleaned_data
            
            nombre = data.get("nombre")
            cantidad_clases = data.get("cantidad_clases")
            precio = data.get("precio")
                        
            plan = Planes(nombre=nombre, cantidad_clases=cantidad_clases, precio=precio)
            plan.save()

        formulario = PlanesFormulario()
        context = {
            "planes": planes,
            "formulario": formulario
        }
        return render(request, "gym/planes/planes.html", context)

@login_required
def borrar_plan(request, id_plan):
    try:
        plan = Planes.objects.get(id=id_plan)
        plan.delete()
        return redirect("Planes")
    except:
        return redirect("Inicio")

@login_required
def editar_plan(request, id_plan):

    if request.method == "GET":
        formulario = PlanesFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "gym/planes/planes_editar.html", contexto)
    
    else:
        formulario = PlanesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                plan= Planes.objects.get(id=id_plan)

                plan.nombre = data.get("nombre")
                plan.cantidad_clases = data.get("cantidad_clases")
                plan.precio = data.get("precio")

                plan.save()
            except:
                return HttpResponse("Error en la actualización")
   
        return redirect("Planes")

@login_required
def buscar_plan(request):

    plan_nombre = request.GET.get("plan", None)

    if not plan_nombre:
        return HttpResponse("No indicaste ningún nombre")

    planes_lista = Planes.objects.filter(nombre__icontains=plan_nombre)
    return render(request, "gym/planes/planes_resultado_busqueda.html", {"planes": planes_lista})

class PlanesDetail(DetailView):
    model = Planes
    template_name = "gym/planes/planes_detalle.html"
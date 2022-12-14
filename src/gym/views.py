from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from gym.models import Actividades, Socios, Planes
from gym.forms import *
from registro.models import Avatar
from django.contrib.auth.decorators import login_required



# INICIO

def inicio(request):
    
    date = datetime.now()
    
    if request.user.username:
        avatar = Avatar.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen
        else:
            imagen = None
    else:
        imagen = None
    
    contexto= {
        "mensaje": "Página de inicio",
        "date": date,
        "imagen": imagen
    }

    return render(request, "gym/index.html", contexto)
    

# SOBRE MI

def sobre_mi (request):

    if request.user.username:
        avatar = Avatar.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen
        else:
            imagen = None
    else:
        imagen = None
    
    contexto = {
        "mensaje1": "Mi nombre es María Sol Martorell, tengo 36 años y este es mi primer curso de programación.", 
        "mensaje2": "Soy Lic. en Química y Tecnología Ambiental, y busco potenciar mi desarrollo profesional metiéndome en el mundo IT.",
        "mensaje3": "Un camino totalmente desconocido pero con muchas ganas de recorrerlo y aprender! Espero que sea el primero de muchos otros!",
        "imagen": imagen}
        
    return render(request, "gym/sobre_mi.html", contexto)


# ACTIVIDADES

@login_required
def actividades (request):
    actividades = Actividades.objects.all()

    if request.method == "GET":
        formulario = ActividadesFormulario()

        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "actividades":actividades,
            "formulario": formulario,
            "imagen": imagen
        }

        return render(request, "gym/actividades/actividades.html", contexto)

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

        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "actividades":actividades,
            "formulario": formulario,
            "imagen": imagen
        }

        return render(request, "gym/actividades/actividades.html", contexto)


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

    if request.method == "GET":
        actividad_nombre = request.GET.get("actividad")

        actividades_lista = Actividades.objects.filter(nombre__icontains=actividad_nombre)
        
        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "actividades": actividades_lista,
            "query": actividad_nombre,
            "imagen": imagen
        }

        return render(request, "gym/actividades/actividades_resultado_busqueda.html", contexto)
        

@login_required
def actividades_detalle(request,pk):
    
    actividad_id = Actividades.objects.get(pk=pk)

    if request.user.username:
        avatar = Avatar.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen
        else:
            imagen = None
    else:
        imagen = None
    
    contexto = {
        "actividad": actividad_id,
        "imagen": imagen
    }
            
    return render(request, "gym/actividades/actividades_detalle.html", contexto)


# SOCIOS

@login_required
def socios (request):
    socios = Socios.objects.all()

    if request.method == "GET":
        formulario = SociosFormulario()

        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "socios": socios,
            "formulario": formulario,
            "imagen": imagen
        }

        return render(request, "gym/socios/socios.html", contexto)

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
        
        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "socios": socios,
            "formulario": formulario,
            "imagen": imagen
        }

        return render(request, "gym/socios/socios.html", contexto)


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

    if request.method == "GET":
        socio_apellido = request.GET.get("socio")

        socios_lista = Socios.objects.filter(apellido__icontains=socio_apellido)

        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "socios": socios_lista,
            "query": socio_apellido,
            "imagen": imagen
        }

        return render(request, "gym/socios/socios_resultado_busqueda.html", contexto)


@login_required
def socios_detalle(request,pk):
    
    socio_id = Socios.objects.get(pk=pk)

    if request.user.username:
        avatar = Avatar.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen
        else:
            imagen = None
    else:
        imagen = None
    
    contexto = {
        "socio": socio_id,
        "imagen": imagen
    }
      
    return render(request, "gym/socios/socios_detalle.html", contexto)


# PLANES

@login_required
def planes (request):
    planes = Planes.objects.all()

    if request.method == "GET":
        formulario = PlanesFormulario()

        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None

        contexto = {
            "planes": planes,
            "formulario": formulario,
            "imagen": imagen
        }
        
        return render(request, "gym/planes/planes.html", contexto)

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
        
        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None

        contexto = {
            "planes": planes,
            "formulario": formulario,
            "imagen": imagen
        }
        
        return render(request, "gym/planes/planes.html", contexto)


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
    
    if request.method == "GET":
        plan_nombre = request.GET.get("plan")

        planes_lista = Planes.objects.filter(nombre__icontains=plan_nombre)
        
        if request.user.username:
            avatar = Avatar.objects.filter(usuario=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen
            else:
                imagen = None
        else:
            imagen = None
    
        contexto = {
            "planes": planes_lista,
            "query": plan_nombre,
            "imagen": imagen
        }

        return render(request, "gym/planes/planes_resultado_busqueda.html", contexto)


@login_required
def planes_detalle(request,pk):
    
    plan_id = Planes.objects.get(pk=pk)

    if request.user.username:
        avatar = Avatar.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen
        else:
            imagen = None
    else:
        imagen = None
    
    contexto = {
        "plan": plan_id,
        "imagen": imagen
    }
    
    return render(request, "gym/planes/planes_detalle.html", contexto)
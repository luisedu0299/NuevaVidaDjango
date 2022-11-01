from django.shortcuts import render, redirect
from django.contrib import messages
import datetime

# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

from..models import Usuario, DetalleFuneral

def index(request):
    context = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        context = {"sesion" : permisos}
    return render (request,'index.html', context)

def listarDetalle (request):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        q = DetalleFuneral.objects.all() #DICCIONARIO CON LOS DATOS 
        context = {"datos":q, "sesion":permisos}
        return render(request, 'detalleFuneral/listarDetalle.html',context)
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html')


def formularioDetalle(request, id):
    permisos = {}
    print(id)
    if id != 0:
        
        p = Usuario.objects.all()
        
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"Usuario": p,"sesion" : permisos}
            return render(request, 'detalleFuneral/agregarDetalle.html',context)
        else:
            messages.warning(request,"para ingresar debe iniciar sesion...")
            return render (request,'index.html') 
    else:
        t = {'id':id}
        p = Usuario.objects.all()
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"DetalleFuneral":t, "Usuario": p, "sesion":permisos}
            return render(request,'detalleFuneral/agregarDetalle.html', context)
        else:
            messages.warning(request,"para ingresar debe iniciar sesion...")
            return render (request,'index.html')


def guardarDetalle (request):
    try:
        if request.method=="POST":
            q = DetalleFuneral(
                fechaEntierro = datetime.datetime.strptime(request.POST["fechaEntierro"],"%Y-%m-%d").date(),
                detalles = request.POST["detalles"],
                cantidadBebidas = request.POST["cantidadBebidas"],
                precioBebidas = request.POST["precioBebidas"],
                totalBebidas = request.POST["totalBebidas"],
                nombreCementerio = request.POST["nombreCementerio"],
                cedulaUsuario = Usuario.objects.get(pk = request.POST["idUsuario"]),
                
                
            )
            q.save()
        #si todo esta bien.
            messages.success(request," Datos guardados perfectamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarUsuario')
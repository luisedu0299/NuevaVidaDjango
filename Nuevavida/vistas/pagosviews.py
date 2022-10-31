
from email.policy import HTTP
from multiprocessing import context
from time import strftime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime


# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from..models import Pagos, Factura, Usuario


def index(request):
    context = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        context = {"sesion" : permisos}
    return render (request,'index.html', context)

def listarPagos (request):
    permisos = {}
    q = None
    if "rol" in request.session:
        if request.session["rol"] == '1':
            q = Pagos.objects.all() #DICCIONARIO CON LOS DATOS 
        else:
            us = Pagos.objects.get(cedulaUsuario = request.session["idUser"])
            q = [us]
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html')        
    
    context = {"datos":q,"sesion":permisos}
    return render(request, 'pagos/listarPagos.html',context)


def formularioPagos (request):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        p = Usuario.objects.all()
        context = {"Usuarios": p, "sesion": permisos}
        return render(request, 'pagos/agregarPagos.html',context)
    else:
        t = {'id':id}
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"Plan":t, "sesion":permisos}
            return render(request,'planes/agregarPlan.html', context)
        else:
            messages.warning(request,"para ingresar debe iniciar sesion...")
            return render (request,'index.html') 



def guardarPagos (request):
    try:
        if request.method=="POST":
            usuario = Usuario.objects.get(pk = request.POST["usuario"])
            print(usuario.idplan.precio)
            print(int(request.POST["cuota"]))
            print(usuario.idplan.precio - int(request.POST["cuota"]))
            usuario.deuda = usuario.idplan.precio - int(request.POST["cuota"])
            usuario.save()
            factura = Factura(
                fechaPago = datetime.datetime.now(),
                totalDeuda = usuario.deuda,
                totalPago = request.POST["cuota"]
            )
            factura.save()
            q = Pagos(
                valor = request.POST["valor"],
                fechaPago = datetime.datetime.now(),
                cedulaUsuario= usuario,
                cuota = request.POST["cuota"],
                idFactura = factura
            )
            q.save()
            messages.success(request," El pago fue guardado correctamente!")
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPagos')

        


def buscarUsuario(request):
    print(request.POST["usuario"])
    usuario = Usuario.objects.get(pk = request.POST["usuario"])
    usuario.idplan.precio = usuario.idplan.precio + usuario.deuda
    p = Usuario.objects.all()
    context = {"Usuarios": p ,"Usuario": usuario}
    return render(request, 'pagos/agregarPagos.html',context)
    

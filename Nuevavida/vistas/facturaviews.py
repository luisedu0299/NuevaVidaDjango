from ast import Pass
from email.policy import HTTP
from multiprocessing import context
from time import strftime
from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime


# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from..models import Usuario, Factura, Pagos


def index(request):
    ontext = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        context = {"sesion" : permisos}
    return render (request,'index.html', context)

def listarFactura (request):
    permisos = {}
    q = None
    u = None
    if "rol" in request.session:
        if request.session["rol"] == '1':
            q = []
            fs = Factura.objects.all()
            for f in fs:
                pago = Pagos.objects.get(idFactura = f.pk)
                us = Usuario.objects.get(pk = pago.cedulaUsuario.pk)
                q.append({"nombre" : us.nombre, 
                "fechaPago" : f.fechaPago,
                "totalDeuda" : f.totalDeuda,
                "totalPago" : f.totalPago,
                "id" : f.pk})
        else:
            facturas = []
            pagos = []
            pagos.append(Pagos.objects.get(cedulaUsuario_id = request.session["idUser"]))
            for p in pagos:
                facturas.append(Factura.objects.get(pk = p.idFactura.id))
            print("facturas "+str(len(facturas)))
            q = facturas
            u = Usuario.objects.get(pk = request.session['idUser'])
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        context = {"datos":q,"sesion":permisos, "usuario" : u}
        return render(request, 'factura/listarFactura.html',context)
    
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html')

    

def verFactura (request, id):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser']}
        f = Factura.objects.get(pk = id)
        p = list(Pagos.objects.filter(idFactura = id).values('cedulaUsuario'))
        c = Usuario.objects.get(pk = p[0]["cedulaUsuario"])
        context = {"Factura":f, "Pago" : p, "Usuario" : c, "sesion":permisos, "userName" : request.session['userName']}
        return render(request, 'factura/verFactura.html',context)

    else:
        messages.warning(request,"USTED NO TIENE PERMISOS PARA ACCEDER A ESTE MODULO")
        return render (request,'index.html', context) 

def verFacturaPago(request, id):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
    p = Pagos.objects.get(pk = id)
    f = Factura.objects.get(pk = p.idFactura.id)
    c = Usuario.objects.get(pk = p.cedulaUsuario.id)
    context = {"Factura":f, "Pago" : p, "Usuario" : c,"sesion":permisos}
    return render(request, 'factura/verFactura.html',context)


def descargarFactura(request, id):
    pass


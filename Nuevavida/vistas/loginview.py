import hashlib
from django.shortcuts import render, redirect
from django.contrib import messages

from..models import Usuario

def encryptPass(password):
    password = password.encode('utf-8')
    return hashlib.sha512(password).hexdigest()

def login(request):
    context = {}
    try:
        if request.method=="POST":
            usuario = Usuario.objects.get(correo = request.POST["correo"])
            print(usuario.rol + " " + usuario.nombre)
            if usuario.rol == '1' or usuario.rol == '2':
                pass1 = encryptPass(request.POST["password"])
                if pass1 == usuario.password:
                    request.session['rol'] = usuario.rol
                    request.session['idUser'] = usuario.pk
                    request.session['userName'] = usuario.nombre
                    permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
                    context = {"sesion" : permisos}
                else:
                    messages.warning(request,"Contraseña incorrecta")
            else:
                messages.warning(request,"Usuario no existe")
            print(usuario)
            messages.success(request," ha iniciado sesion correctamente!")
        else:
            messages.warning(request,"Error al enviar datos")
    except Exception as e:
        messages.error(request,f"error: {e}")
    print(context)       
    return render(request,'index.html', context)
  



def logout (request):
    try:
        del request.session['rol']
        del request.session['idUser']
        del request.session['userName']
    except Exception as e:
        print(request,f"error: {e}")
    return redirect('Nuevavida:index')




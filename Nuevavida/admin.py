from django.contrib import admin
from .models import Usuario, Plan,  Factura, Beneficiario, Pagos, DetalleFuneral


# Register your models here.

@admin.register(Usuario) #decorador
class UsuarioAdmin (admin.ModelAdmin):
    list_display =('cedula','nombre','apellido','correo','telefono','fechaNacimiento','deuda') 
    search_fields=['nombre', 'cedula','deuda'] 


@admin.register(Beneficiario)
class BeneficiarioAdmin (admin.ModelAdmin):
    list_display = ('cedulaBeneficiario','nombreBeneficiario','apellidoBeneficiario','fechaNacimiento','cedulaUsuario')
    search_fields =['nombreBeneficiario','cedulaBeneficiario']



@admin.register(Plan)
class PlanAdmin (admin.ModelAdmin):
    list_display= ('nombrePlan','precio','caracteristicas')
    search_fields =['nombrePlan',]


    


@admin.register(Factura)
class FacturaAdmin (admin.ModelAdmin):
    list_display= ('fechaPago','totalDeuda','totalPago')
    search_fields =['totalPago']


@admin.register(Pagos)
class PagosAdmin (admin.ModelAdmin):
    list_display = ('valor','fechaPago','cuota','idFactura','cedulaUsuario')
    search_fields = ['cedulaUsuario','fechaPago','valor']

@admin.register(DetalleFuneral)
class DetalleFuneralAdmin (admin.ModelAdmin):
    list_display= ('fechaEntierro','horaInicio','horaFinal','cantidadBebidas','precioBebidas','totalBebidas','lugarVelacion','nombreCementerio')
    search_fields= ['fechaEntierro']


    
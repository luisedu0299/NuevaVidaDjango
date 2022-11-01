from django.urls import path
from Nuevavida.models import Usuario
from .vistas import detallefuneralviews, usuarioviews, planviews, facturaviews, pagosviews, beneficiarioviews,loginview




 
app_name= "Nuevavida"
urlpatterns = [
    path('', usuarioviews.index,name="index"), 

# crud usuarios
    
    path('Usuario/',usuarioviews.listarUsuario, name="listarUsuario"),
    path('editarUsuario/<int:id>',usuarioviews.editarUsuario, name="editarUsuario"),
    path ('formularioUsuario/<int:id>',usuarioviews.formularioUsuario, name="formularioUsuario"),
    path ('agregarUsuario/',usuarioviews.guardarUsuario, name="agregarUsuario"),
    path('eliminarUsuario/<int:id>',usuarioviews.eliminarUsuario, name="eliminarUsuario"),


# crud Plan

    path('listarPlan/',planviews.listarPlan, name="listarPlan"),
    path('editarPlan/<int:id>',planviews.editarPlan, name="editarPlan"),
    path ('formularioPlan/<int:id>',planviews.formularioPlan, name="formularioPlan"),
    path ('guardarPlan/',planviews.guardarPlan, name="guardarPlan"),
    path('eliminarPlan/<int:id>',planviews.eliminarPlan, name="eliminarPlan"),


    
# crud Factura

    path('Factura/',facturaviews.listarFactura, name="listarFactura"),
    path('verFactura/<int:id>',facturaviews.verFactura, name="verFactura"),
    path('verFacturaPago/<int:id>',facturaviews.verFacturaPago, name="verFacturaPago"),
    path ('descargarFactura/<int:id>',facturaviews.descargarFactura, name="descargarFactura"),


#crud Pagos

    path('Pagos/',pagosviews.listarPagos, name="listarPagos"),
    path ('formularioPagos/',pagosviews.formularioPagos, name="formularioPagos"),
    path ('agregarPagos/',pagosviews.guardarPagos, name="agregarPagos"),
    path ('buscarUsuario/',pagosviews.buscarUsuario, name="buscarUsuario"),

#crud Beneficiarios

    path('Beneficiario/',beneficiarioviews.listarBeneficiario, name="listarBeneficiario"),
    path('editarBeneficiario/<int:id>',beneficiarioviews.editarBeneficiario, name="editarBeneficiario"),
    path ('formularioBeneficiario/<int:id>',beneficiarioviews.formularioBeneficiario, name="formularioBeneficiario"),
    path ('agregarBeneficiario/',beneficiarioviews.guardarBeneficiario, name="agregarBeneficiario"),
    path('eliminarBeneficiario/<int:id>',beneficiarioviews.eliminarBeneficiario, name="eliminarBeneficiario"),

#login
    path('login/',loginview.login, name="login"),
    path('logout/',loginview.logout, name="logout"),


# crud Detalle de Funeral
    
    path('formularioDetalle/<int:id>',detallefuneralviews.formularioDetalle, name="formularioDetalle"),
    path('guardarDetalle/',detallefuneralviews.guardarDetalle, name="guardarDetalle"),


]



from django import forms

#Creamos nuestros formularios
class ExportadorForm(forms.Form): #Hereda de la clase forms. Form para crear tu formulario personalizado.
    nombre = forms.CharField()
    domicilio = forms.CharField()
    email = forms.EmailField()
    cuit = forms.IntegerField()

class ImportadorForm(forms.Form):
    nombre = forms.CharField()
    domicilio = forms.CharField()
    email = forms.EmailField()
    cuit = forms.IntegerField()

class MercaderiaForm(forms.Form):   
    nomb_mer = forms.CharField()
    unidad_venta = forms.CharField()

class OperacionForm(forms.Form):
    fecha_operacion = forms.DateField()
    fecha_cump = forms.DateField()
    nro_permiso = forms.IntegerField()
    cantidad = forms.IntegerField()
       
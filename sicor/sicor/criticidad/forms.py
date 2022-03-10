from django import forms
from .models import *
#FORMULARIO CRITICIDAD SIMPLE SECUNDARIA
class FormularioCriticidad(forms.ModelForm):
    class Meta:
        model = Criticidad
        fields = [
            'activo',
            'nombre',
            'po',
            'ps',
            'fua',
            'pe',
            'sh',
            'ma',
            'r',
        ]
        labels = {
            'activo':'Activo',
            'nombre':'Nombre',
            'po':'¿Es parte de un proceso operativo?',
            'ps':'¿Es parte de un sistema?',
            'fua':'¿Se ha producido alguna una falla en el último año?',
            'pe':'¿Su pérdida de función puede producir afectación económica?',
            'sh':'¿Su pérdida de función puede producir afectación a la salud del personal?',
            'ma':'¿Su pérdida de función puede producir afectación al medio ambiente?',
            'r':'Redundancia',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'po': forms.Select(attrs={'id':'po','class':'form-control','title':'hh:mm:ss'}),
            'ps': forms.Select(attrs={'id':'ps','class':'form-control','title':'hh:mm:ss'}),
            'fua': forms.Select(attrs={'id':'fua','class':'form-control','title':'hh:mm:ss'}),
            'pe': forms.Select(attrs={'id':'pe','class':'form-control','title':'hh:mm:ss'}),
            'sh': forms.Select(attrs={'id':'sh','class':'form-control','title':'hh:mm:ss'}),
            'ma': forms.Select(attrs={'id':'ma','class':'form-control','title':'hh:mm:ss'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control','title':'hh:mm:ss'}),
          }

#FORMULARIO CRITICIDAD SIMPLE PRIMARIA

class FormularioCriticidadPr(forms.ModelForm):
    class Meta:
        model = CriticidadPr
        fields = [
            'activo',
            'nombre',
            'po',
            'ps',
            'fua',
            'pe',
            'sh',
            'ma',
            'r',
        ]
        labels = {
            'activo':'Activo',
            'nombre':'Nombre',
            'po':'¿Es parte de un proceso operativo?',
            'ps':'¿Es parte de un sistema?',
            'fua':'¿Se ha producido alguna una falla en el último año?',
            'pe':'¿Su pérdida de función puede producir afectación económica?',
            'sh':'¿Su pérdida de función puede producir afectación a la salud del personal?',
            'ma':'¿Su pérdida de función puede producir afectación al medio ambiente?',
            'r':'Redundancia',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'po': forms.Select(attrs={'id':'po','class':'form-control','title':'hh:mm:ss'}),
            'ps': forms.Select(attrs={'id':'ps','class':'form-control','title':'hh:mm:ss'}),
            'fua': forms.Select(attrs={'id':'fua','class':'form-control','title':'hh:mm:ss'}),
            'pe': forms.Select(attrs={'id':'pe','class':'form-control','title':'hh:mm:ss'}),
            'sh': forms.Select(attrs={'id':'sh','class':'form-control','title':'hh:mm:ss'}),
            'ma': forms.Select(attrs={'id':'ma','class':'form-control','title':'hh:mm:ss'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control','title':'hh:mm:ss'}),
          }


#FORMULARIO CRITICIDAD COMPLETA PRIMARIA

class FormularioCriticidadCPr(forms.ModelForm):
    class Meta:
        model = CriticidadCPr
        fields = [
            'tag',
            'activo',
            'nombre',
            'r',
            'ocurrencia',
            'segysa',
            'md',
            'cm',
            'pp',
            'ex',
        ]
        labels = {
            'tag':'Tag',
            'activo':'Activo',
            'nombre':'Nombre',
            'r':'Redundancia',
            'ocurrencia':'Ocurrencia',
            'segysa':'Seguridad y Salud',
            'md':'Medio Ambiente',
            'cm':'Costo de Mantenimiento',
            'pp':'Pérdida de Producción',
            'ex':'Exposición',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control'}),
            'ocurrencia': forms.Select(attrs={'id':'ocurrencia','class':'form-control'}),
            'segysa': forms.Select(attrs={'id':'segysa','class':'form-control'}),
            'md': forms.Select(attrs={'id':'md','class':'form-control'}),
            'cm': forms.Select(attrs={'id':'cm','class':'form-control'}),
            'pp': forms.Select(attrs={'id':'pp','class':'form-control'}),
            'ex': forms.Select(attrs={'id':'ex','class':'form-control'}),
          }

#FORMULARIO CRITICIDAD COMPLETA SECUNDARIA

class FormularioCriticidadCSec(forms.ModelForm):
    class Meta:
        model = CriticidadCSec
        fields = [
            'tag',
            'activo',
            'nombre',
            'r',
            'ocurrencia',
            'segysa',
            'md',
            'cm',
            'pp',
            'ex',
        ]
        labels = {
            'tag':'Tag',
            'activo':'Activo',
            'nombre':'Nombre',
            'r':'Redundancia',
            'ocurrencia':'Ocurrencia',
            'segysa':'Seguridad y Salud',
            'md':'Medio Ambiente',
            'cm':'Costo de Mantenimiento',
            'pp':'Pérdida de Producción',
            'ex':'Exposición',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control'}),
            'ocurrencia': forms.Select(attrs={'id':'ocurrencia','class':'form-control'}),
            'segysa': forms.Select(attrs={'id':'segysa','class':'form-control'}),
            'md': forms.Select(attrs={'id':'md','class':'form-control'}),
            'cm': forms.Select(attrs={'id':'cm','class':'form-control'}),
            'pp': forms.Select(attrs={'id':'pp','class':'form-control'}),
            'ex': forms.Select(attrs={'id':'ex','class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN REDUNDANCIA
class FormularioRedundancia(forms.ModelForm):
    class Meta:
        model = Redundancia
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN OCURRENCIA
class FormularioOcurrencia(forms.ModelForm):
    class Meta:
        model = Ocurrencia
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN SEGYSA
class FormularioSegysa(forms.ModelForm):
    class Meta:
        model = Segysa
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN MDA
class FormularioMdA(forms.ModelForm):
    class Meta:
        model = MdA
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }
#FORMULARIO CONFIGURACIÓN COSTO
class FormularioCosto(forms.ModelForm):
    class Meta:
        model = Costo
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN PERDIDA
class FormularioPerdida(forms.ModelForm):
    class Meta:
        model = Perdida
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN EXPOSICIÓN
class FormularioExposicion(forms.ModelForm):
    class Meta:
        model = Exposicion
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }


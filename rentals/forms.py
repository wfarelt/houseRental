from django.forms import *
from .models import Contact

class ContactoForm (ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
        labels ={
             'Name':'descripcion'
        }
        widgets={
            'name':TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre'
                }
            ),
             'email':TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electronico'
                }
            ),
             'mensaje':Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su consulta',
                    'rows':3,
                    'cols':3
                }
            )
            
        }

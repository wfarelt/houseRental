from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude=['created', 'visits', 'user', 'status']
        labels = {'property_type': 'Tipo de Propiedad', 
            'name': 'Titulo', 
            'description': 'Descripción', 
            'price': 'Precio', 
            'rooms': 'Habitaciones', 
            'bathrooms': 'Baños', 
            'garage': 'Garajes',
            'area': 'Area', 
            'pets': 'Mascotas',
            'address': 'Dirección', 
            'comfort': 'Confort', 
            'scuare_meters': 'Metros Cuadrados',
            'image': 'Imagen',    
            }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['property_type'].empty_label = "Seleccione una opción"
        self.fields['pets'].widget.attrs.update({'class': 'form-check-input ml-2'})
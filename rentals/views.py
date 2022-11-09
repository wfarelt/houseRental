from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

from .models import PropertyType, Property,Contact

from django.contrib.auth.views import LoginView
from .forms import ContactoForm
from django.http import HttpResponse


# Create your views here.

def index(request):
    property_types = PropertyType.objects.filter(status=True)
    propertys = Property.objects.filter(status='1', visits__gte=1).order_by('-visits')[:4]
    context = { 'property_types' : property_types, 'propertys' : propertys }
    return render(request, 'rentals/index.html', context )

class LoginView(LoginView):
    template_name = 'login.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')

def property_detail(request, pk):
    property = Property.objects.get(id=pk)
    property.visits_count()
    conforts = property.confort.all()
    property_types = PropertyType.objects.filter(status=True)
    context = { 'property' : property, 'property_types' : property_types, 'conforts' : conforts }
    return render(request, 'rentals/property_detail.html', context )

def properties_by_type(request, pk):
    if pk == 0:
        property_type = PropertyType.objects.filter(status=True)
    else:
        property_type = PropertyType.objects.get(id=pk)
    
    property_types = PropertyType.objects.filter(status=True)
    propertys = Property.objects.filter(status='1', property_type=property_type)

    context = { 'property_types' : property_types, 'propertys' : propertys, 'property_type' : property_type }
    return render(request, 'rentals/properties_by_type.html', context )
    
class PropertyCreateView(CreateView):
    model = Property
    template_name = 'rentals/property_create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')



#def contacto(request):
class ContactCreateView(CreateView):
    model = Contact
    form_class=ContactoForm
    template_name = 'rentals/contact.html'
   
    success_url = reverse_lazy('index')
   

def myfirstView(request):
    return HttpResponse("hola mundo")    
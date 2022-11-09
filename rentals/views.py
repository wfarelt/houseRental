from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PropertyType, Property, Contact
from .forms import PropertyForm
from django.contrib.auth.views import LoginView
from .forms import ContactoForm
from django.http import HttpResponse


# Create your views here.

# Index
def index(request):
    property_types = PropertyType.objects.filter(status=True)
    propertys = Property.objects.filter(status='1', visits__gte=1).order_by('-visits')[:4]
    context = { 'property_types' : property_types, 'propertys' : propertys }
    return render(request, 'rentals/index.html', context )

# Login
class LoginView(LoginView):
    template_name = 'login.html'

# Register
class UserCreateView(CreateView):
    property_types = PropertyType.objects.filter(status=True)
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_types'] = self.property_types
        return context

# PropertyView
def property_detail(request, pk):
    property = Property.objects.get(id=pk)
    property.visits_count()
    conforts = property.confort.all()
    property_types = PropertyType.objects.filter(status=True)
    context = { 'property' : property, 'property_types' : property_types, 'conforts' : conforts }
    return render(request, 'rentals/property_detail.html', context )

# Property Views by Type
def properties_by_type(request, pk):
    if pk == 0:
        property_type = PropertyType.objects.filter(status=True)
    else:
        property_type = PropertyType.objects.get(id=pk)
    
    property_types = PropertyType.objects.filter(status=True)
    propertys = Property.objects.filter(status='1', property_type=property_type)

    context = { 'property_types' : property_types, 'propertys' : propertys, 'property_type' : property_type }
    return render(request, 'rentals/properties_by_type.html', context )


# Property Views by User
@login_required(login_url='/accounts/login/')
def properties_by_id(request):
    user = request.user.id
    if user:
        propertys = Property.objects.filter(status='1', user=user)
    property_types = PropertyType.objects.filter(status=True)
    context = {'propertys' : propertys, 'property_types' : property_types}
    return render(request, 'rentals/property_list.html', context )
    
# Property Create
class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    template_name = 'rentals/property_create.html'
    form_class = PropertyForm
    success_message: str = "Sub-Categoria Creada"
    success_url = reverse_lazy('index')
    login_url = 'accounts:login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    



#def contacto(request):
class ContactCreateView(CreateView):
    model = Contact
    form_class=ContactoForm
    template_name = 'rentals/contact.html'
    success_url = reverse_lazy('index')
   


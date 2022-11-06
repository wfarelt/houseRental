from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

from .models import PropertyType

from django.contrib.auth.views import LoginView

# Create your views here.

def index(request):
    propertys = PropertyType.objects.filter(status=True)
    context = { 'propertys' : propertys }
    return render(request, 'rentals/index.html', context )

class LoginView(LoginView):
    template_name = 'login.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')

    

    
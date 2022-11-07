from django.urls import path, include

from .views import index, UserCreateView, LoginView, property_detail, properties_by_type, \
    PropertyCreateView

urlpatterns = [
    path('', index, name='index'),
    path("accounts/", include(("django.contrib.auth.urls",'accounts'), namespace='accounts')),
    path("accounts/register/", UserCreateView.as_view(), name='register'),
    
    path('property/<int:pk>', property_detail, name='property_detail'),
    path('property_type/<int:pk>', properties_by_type, name='properties_by_type'),
    path('property_create/', PropertyCreateView.as_view(), name='property_create'),
]
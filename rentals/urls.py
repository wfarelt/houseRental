from django.urls import path, include

from .views import index, UserCreateView, LoginView

urlpatterns = [
    path('', index, name='index'),
    path("accounts/", include(("django.contrib.auth.urls",'accounts'), namespace='accounts')),
    path("accounts/register/", UserCreateView.as_view(), name='register'),
]
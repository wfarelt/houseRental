from django.contrib import admin


# Register your models here.

from .models import PropertyType

admin.site.register(PropertyType)

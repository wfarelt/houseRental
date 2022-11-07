from django.contrib import admin


# Register your models here.

from .models import PropertyType, Property, Comfort

admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(Comfort)



from django.db import models

# Create your models here.

# MODELO TIPO DE PROPIEDAD

class PropertyType(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Propiedad"
        verbose_name_plural = "Tipos de Propiedades"
        ordering = ['name']

    
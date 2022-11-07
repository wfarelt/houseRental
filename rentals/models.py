from django.db import models
from django.contrib.auth.models import User

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


# MODELO COMODIDAD
class Comfort(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Comodidad"
        verbose_name_plural = "Comodidades"
        ordering = ['name']

# MODELO PROPIEDAD

STATUS_CHOICES =(
    ("1", "DISPONIBLE"),
    ("2", "OCUPADO"),
    ("3", "RESERVADO"),
    ("4", "MANTENIMIENTO"),
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    scuare_meters = models.IntegerField()
    pets = models.BooleanField(default=True)
    image = models.ImageField(upload_to='property', null=True, blank=True)
    #geo_location = models.PointField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    confort = models.ManyToManyField(Comfort, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ['created']
    
    def visits_count(self):
        self.visits += 1
        self.save()



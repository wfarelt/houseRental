# Generated by Django 4.1.3 on 2022-11-06 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('address', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rooms', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('garage', models.IntegerField(default=0)),
                ('scuare_meters', models.IntegerField()),
                ('pets', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='property')),
                ('status', models.CharField(choices=[('1', 'DISPONIBLE'), ('2', 'OCUPADO'), ('3', 'RESERVADO'), ('4', 'MANTENIMIENTO')], default='1', max_length=1)),
                ('visits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.propertytype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Propiedad',
                'verbose_name_plural': 'Propiedades',
                'ordering': ['created'],
            },
        ),
    ]

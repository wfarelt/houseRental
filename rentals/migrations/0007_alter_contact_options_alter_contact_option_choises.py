# Generated by Django 4.1.3 on 2022-11-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.AlterField(
            model_name='contact',
            name='option_choises',
            field=models.IntegerField(choices=[['0', 'CONSULTA'], ['1', 'RECLAMO'], ['2', 'SUGERENCIA'], ['3', 'FELICITACIONES']]),
        ),
    ]
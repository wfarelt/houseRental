# houseRental
Proyecto de SW1 sobre contratos inteligentes

#Integrantes

- Roger Andia
- Wilson Farel

## Entorno virtual
python -m venv mvirtual

# Requerimientos
pip install -r requirements.txt

# Migración
python manage.py migrate

# Levantar servidor
python manage.py runserver

# Uso de PostgreSQL con Django
https://djangocentral.com/using-postgresql-with-django/

# Comandos de psql
https://www.librebyte.net/base-de-datos/comandos-para-administrar-postgres/

# Creating A Super User In Django
https://djangocentral.com/creating-super-user-in-django/

# Dumpdata and Loaddata
python manage.py dumpdata rentals.PropertyType > PropertyType.json
python manage.py loaddata PropertyType.json

# Bootstrap example
https://bootstrapmade.com/demo/NiceAdmin/
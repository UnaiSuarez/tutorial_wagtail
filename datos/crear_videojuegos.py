'''
crear videojuegos

ejecutar:

python manage.py shell < datos/crear_generos.py
'''

from django.utils.text import slugify
import csv
import os
from csv import DictReader
from videojuegos.models import Consola, Genre, Videojuego
from decimal import Decimal

#lista de películas del json
f = open("videojuegos/juegos.csv")
lector = DictReader(f)

for v in Videojuego.objects.all():
    v.delete()
    


for l in lector:
    v = Videojuego()
    v.title = l["titulo"]
    v.descripcion = l["categoria"]
    v.precio = Decimal(l["precio"])
    v.rating = Decimal(l["Rating"])
    v.link = "https://as.com/" + l["link"]
    v.imagen = l["img"]
    v.save()
    for genero in l['genero'].split('\n'):
        genobj, created = Genre.objects.get_or_create(nombre=genero) # Recupera o crea el género si no existe
        v.generos.add(genobj) # añade la relación m2m
    for consola in l['plataformas'].split('\n'):
        genobj, created = Consola.objects.get_or_create(nombre=consola) # Recupera o crea el género si no existe
        v.consolas.add(genobj) # añade la relación m2m
    
    

# generos = [j["genero"] for j in lector]
# generos = set(generos)
# generos_all = []
# for genero in generos:
#     generos_all.extend(genero.split("\n"))
# generos = set(generos_all)
# print(generos)
# for p in lector:
#     videojuego = Videojuego.objects.get(title=p["title"])
#     for genero in generos:
#             genobj, created = Genre.objects.get_or_create(nombre=genero) # Recupera o crea el género si no existe
#             videojuego.generos.add(genobj) # añade la relación m2m

# consolas = [j["plataformas"] for j in lector]
# consolas = set(consolas)
# consolas_all = []
# for consola in consolas:
#     consolas_all.extend(consola.split("\n"))
# consolas = set(consolas_all)
# print(consolas)
# for p in lector:
#     videojuego = Videojuego.objects.get(title=p["title"])
#     for consola in consolas:
#             genobj, created = Consola.objects.get_or_create(nombre=consola) # Recupera o crea el género si no existe
#             videojuego.consolas.add(genobj) # añade la relación m2m


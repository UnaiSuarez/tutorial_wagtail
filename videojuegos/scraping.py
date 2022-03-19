from turtle import st
from bs4 import BeautifulSoup
import requests
import random

import csv

contador = 0
title=[]

for x in range(10):
    page_link = 'https://as.com/meristation/juegos/listado/{}/'.format(x)
    page_response = requests.get(page_link, timeout=5)
    soup  = BeautifulSoup(page_response.content, "html.parser")

    for link in soup.select('div[class=mod-ga-det]'):
        precioAleatorio = random.randint(0, 100)
        rankAleatorio = random.randint(0,10)
        imagen = link.find('div', class_='ga-art').find('figure')

        ranking = {
            'titulo': link.find('div', class_='ga-inf').find('h2', class_='ga-tl').text,
            'precio': precioAleatorio,
            'Rating' : rankAleatorio,
            'plataformas': link.find('div', class_="ga-inf").find('ul', class_='rel-tags').text,
            'categoria': link.find('div', class_ ='ga-inf').find('div', class_='ga-plot').text,
            'genero': link.find('div', class_ ='ga-inf').find('ul', class_='ga-gen').text,
            'link': link.find('div', class_='ga-inf').find('h2', class_='ga-tl').find('a')['href'],
            'img': imagen
            # 'URL' : link.find('div', class_="di-ib clearfix").find('a')['href'],

        }
        title.append(ranking)
        contador = contador + 1
    print(ranking['img'])

#     def write_csv(items, path):
#         # Open the file in write mode
#         with open(path, 'w', encoding='utf-8') as f:
#             csvwriter = csv.writer(f, dialect='excel')
#             # Return if there's nothing to write
#             if len(items) == 0:
#                 return

#             # Write the headers in the first line
#             headers = list(items[0].keys())
#             # f.write(','.join(headers) + '\n')
#             csvwriter.writerow(headers)
            

#             # Write one item per line
#             for item in items:
#                 values = list(item.values())
#                 # for header in headers:
#                 #     registros = item.get(header, "")
#                 #     values.append(str(registros))
#                 # f.write(','.join(values) + "\n")
#                 csvwriter.writerow([str(v).strip() for v in values])

# write_csv(title, "juegos.csv")
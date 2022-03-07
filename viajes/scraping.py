from turtle import st
from bs4 import BeautifulSoup
import requests
import random

import csv

contador = 0
title=[]

page_link = 'https://destinia.com/viajes/mar-caribe-go66391'
page_response = requests.get(page_link, timeout=5)
soup  = BeautifulSoup(page_response.content, "html.parser")

for link in soup.select('div[class=packages-list-container]'):
    precioAleatorio = random.randint(0, 100)
    rankAleatorio = random.randint(0,10)

    ranking = {
        'destino': link.find('div', class_='package-container').find('div', class_='gradient-title hidden-xs'),
        # 'precio': precioAleatorio,
        # 'Rating' : rankAleatorio,
        # 'plataformas': link.find('div', class_="ga-inf").find('ul', class_='rel-tags').text,
        # 'categoria': link.find('div', class_ ='ga-inf').find('div', class_='ga-plot').text,
        # 'genero': link.find('div', class_ ='ga-inf').find('ul', class_='ga-gen').text,
        # 'link': link.find('div', class_='ga-inf').find('h2', class_='ga-tl').find('a')['href'],
        # 'img': link.find('div', class_='ga-art').find('figure').find('img')['src']

        }
    title.append(ranking)
    contador = contador + 1
    print(ranking)

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
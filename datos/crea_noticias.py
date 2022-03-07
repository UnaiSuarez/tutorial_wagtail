'''


ejecutar:

python manage.py shell < datos/crear_generos.py
'''


from email.mime import image
from django.utils.text import slugify
import csv
import os
from csv import DictReader
from noticias.models import Noticia

for v in Noticia.objects.all():
    v.delete()

resumen = ['primera','segunda','tercera','cuarta','quinta']

noticia = ['La invasión rusa en Ucrania entra en su duodécima jornada intensificando los ataques en Járkov y rodeando ya la capital de Ucrania, Kiev. Desde el inicio de la guerra ya son más de 1,5 millones los refugiados que han abandonado el país.',
'La guerra en Ucrania ha entrado en su décimo segundo día este lunes. El Ejército ruso prosigue con su ofensiva y durante la madrugada ha bombardeado de nuevo la ciudad de Járkov, en el noreste, e Irpin, cerca de Kiev. Además, ha estrechado el cerco sobre la capital. ',
'El presidente ruso, Vladímir Putin, ha advertido este domingo que no tiene intención de renunciar a los cuatro objetivos que se ha marcado con la invasión de Ucrania, y que los logrará "o por la negociación o por la guerra". El líder ruso se ha mostrado inflexible en sus exigencias a Kiev durante una conversación telefónica con su homólogo francés, Emmanuel Macron, en la que también ha asegurado que no tiene intención de atacar las instalaciones nucleares.',
'La guerra en Ucrania deja ya más de 1,5 millones de personas desplazadas y al menos 2.000 civiles fallecidos, según el balance ucraniano. Mientras continúa la ofensiva rusa en el país, millones de ciudadanos que lo han perdido todo tratan de huir de los bombardeos. En España, varias ONG han puesto a disposición de los ciudadanos canales para enviar ayuda a los damnificados por el conflicto.',
'Un llamativo helicóptero, sin ningún logo identificativo, y del que cuelga un cable con un raro disco que parece un gran atrapasueños, ha despertado la curiosidad de los vecinos de la zona de Aználcollar que desde hace días lo ven sobrevolando por puntos deshabitados de las sierras de Sevilla y Huelva. Una aparición con la que las administraciones dicen no tener nada que ver y que podría tratarse de un sistema para la realización de estudios geológicos y la búsqueda de acuíferos de agua subterránea.',
'El puente de la Cincomarzada (para los escolares, hasta ¡cuatro días! de fiesta consecutivos), no ha tenido secretos en cuanto a la cesta de la compra y tiendas en general se refiere. El fin de semana ha sido gemelo a cualquier otro, mientras que este lunes día 7 de marzo es festivo no comercial, es decir, que el Gobierno de Aragón no lo tiene señalado en el calendario para la apertura de grandes superficies.']

imagenes = ['https://img2.rtve.es/i/?w=1600&i=1646602997571.jpg',
'https://img2.rtve.es/i/?w=1600&i=1646569378663.jpg',
'https://img2.rtve.es/i/?w=1600&i=1646581772612.jpg',
'https://images.ecestaticos.com/A6s3OAJCt7n_nqxh2aJ7MB8vWpI=/0x0:2272x1704/557x418/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2F901%2F923%2F63a%2F90192363ae3c9f40abfcb968fed1876d.jpg',
'https://estaticos-cdn.prensaiberica.es/clip/e7ad65d3-368a-4d18-9c3c-c0613495855b_16-9-aspect-ratio_default_0.jpg']
# recorre datos del json
for i in range(5):
    p = Noticia()
    p.title ='noticia '+ str(i)
    p.resumen = 'esta es la '+resumen[i]+ ' noticia'
    p.descripcion = noticia[i]
    p.imagen = imagenes[i]
    p.save()
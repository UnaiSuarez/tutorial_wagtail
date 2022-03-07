'''


ejecutar:

python manage.py shell < datos/crear_generos.py
'''


from email.mime import image
from django.utils.text import slugify
import csv
import os
from csv import DictReader
from viajes.models import Viaje

for v in Viaje.objects.all():
    v.delete()

direccion = ['Caybeach PrincessSe','Punta Cana','Hotel Riu Creole','Hotel Salt of Palmar','Hotel Centara Ras Fushi Resort & Spa Maldives']

descripcion = ['El Caybeach Princess se encuentra en Maspalomas y ofrece restaurante, piscina al aire libre, bar y jardín. Ofrece habitaciones familiares y parque infantil. Hay recepción 24 horas, club infantil y servicio de cambio de divisa.',
'¿Quién no ha soñado alguna vez con viajar a Punta Cana? Su fama no es inmerecida. En Punta Cana encontrarás todo lo que estás buscando para vivir unas vacaciones de ensueño. Sólo tienes que preocuparte de disfrutar, nosotros hacemos el resto. Viajarás con la mayor comodidad, ya que incluye vuelo directo, traslados del aeropuerto al hotel y muchas sorpresas más. ',
'El Hotel Riu Creole (All Inclusive 24h), junto con el Hotel Riu Le Morne, conforman el primer RIU Resort en Mauricio, que ha abierto sus puertas a los huéspedes después de una remodelación en el verano de 2014. Se encuentra justo al lado de la playa de Le Morne, en al sudoeste de la isla, al pie del majestuoso Mont Brabant. Su cocina se centra en los productos frescos utilizados para hacer platos fríos y calientes cocinados a pedido, servidos en su restaurante principal con asientos al aire libre. Los huéspedes también pueden disfrutar del restaurante asiático. Los bares del vestíbulo, el salón y la playa completan el reconocido servicio Todo Incluido del hotel. Es el lugar ideal para alojarse. Además de su piscina y su hamaca, sombrilla y servicio de toallas, ofrece una amplia gama de actividades. Es un lugar inmejorable para disfrutar de deportes acuáticos como windsurf, kayak, esnórquel o paddle surf, entre otras actividades. Aquellos que quieran dar rienda suelta a su lado creativo también pueden participar en el exclusivo programa RiuArt.',
'Gran hotel boutique en la costa de Mauricio para los amantes de la comida, los viajes y lo local. De una belleza innegable y exótica. Volcánico, blanco, azul y verde. Es indio, francés, criollo, chino y africano. Sus colores, historias, costumbres, sonidos y sabores forman una mezcla brillante y embriagadora que es imposible ignorar u olvidar. Si lo experimentas.',
'Sumérgete en la serenidad absoluta. El Centara Ras Fushi Resort & Spa Maldives es un refugio solo para adultos ideal para parejas y recién casados. Las villas amplias y luminosas, con suelos de madera y telas naturales, ofrecen sensacionales vistas del Océano Índico y ofrecen la opción de alojamiento junto a la playa o sobre agua. Arena blanca pura y una laguna azul brillante hacen de este un lugarperfecto para los juegos de playa, buceo y deportes acuáticos. Como complejo solo para adultos, los huéspedes deben tener 12 años o más.',
'Bueco Incluido (Mayores de 18 años): Los clientes que reserven en régimen de Todo Incluido Gold tienen la posibilidad de cambiar el bono de 50 usd para el Spa en los días que elijan por inmersiones tal como sigue: 3 inmersiones por villa y estancia de 7 noches limitadas a una inmersión al día. Las 3 inmersiones incluyen una sesión de orientación y 2 inmersiones. Cada inmersión, incluida la de orientación, dura un máximo de 45 minutos. Los participantes deben tener certificado de buceo en aguas abiertas para realizar la sesión de orientación. (Las inmersiones están sujetas a las condiciones meteorológicas y la última debe realizarse con un máximo de 24 hrs. de antelación al último día en el hotel).']

imagenes = ['https://t-cf.bstatic.com/xdata/images/hotel/max1024x768/261897126.jpg?k=db408a09e816c9e760601e9a76fe6174473b0852255c1060208483783c5e125d&o=&hp=1',
'https://d2l4159s3q6ni.cloudfront.net/resize/550x310/filters:max_age(2604800):quality(65):format(webp)/s3/dam/photos/a0/d9/77/52/12b6facc080a3be44789bf905a2259516547a317f28ae83ceec40af5.jpg',
'https://d2poxrheyfxwbo.cloudfront.net/resize/780x500/filters:max_age(2604800):quality(65):format(webp)/s3/hotel/b6f84721-8bc7-4548-adfe-79a87247f5b7',
'https://d2poxrheyfxwbo.cloudfront.net/resize/780x500/filters:max_age(2604800):quality(65):format(webp)/s3/hotel/751816b0-6fd6-40e7-b554-d3bd7033cf93',
'https://d2poxrheyfxwbo.cloudfront.net/resize/780x500/filters:max_age(2604800):quality(65):format(webp)/s3/hotel/18dfa897-f705-44f0-b221-7146e70fab7f']

coordenadas = ['27.756633825899414, -15.599565590788904','-20.206347249933316, 57.79040335713412','-20.46799029732964, 57.31413020895419','4.201215000162426, 73.41340072883582','3.8491918147577278, 73.45543450925359']

# recorre datos del json
for i in range(5):
    p = Viaje()
    p.destino =direccion[i]
    p.descripcion = descripcion[i]
    p.imagen = imagenes[i]
    p.coordenadas = coordenadas[i]
    p.save()
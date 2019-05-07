import requests
from bs4 import BeautifulSoup
import json
url='http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
r = requests.get(url)
r.encoding='utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
items=soup.find('table')
#print(items)
contenido=items.find_all('tr')
#print(contenido)
#cont=contenido[5]
#print(cont)
#datos=cont.find_all(class_='tddatos')
#1621

lista=[]
for i in range(1533,1542,3):
    cont=contenido[i]
    datos=cont.find_all(class_='tddatos')
    registro={
        "NRC":datos[0].text,
        "Clave":datos[1].a.text,
        "Materia":datos[2].a.text,
        "Seccion":datos[3].text,
        "Creditos":datos[4].text,
        "Cupos":datos[5].text,
        "Disponible":datos[6].text,
        "Hora":cont.find(align='center').find('table').find('tr').find_all('td')[1].text,
        "Dias":cont.find(align='center').find('table').find('tr').find_all('td')[2].text,
        "Edificio":cont.find(align='center').find('table').find('tr').find_all('td')[3].text,
        "Aula":cont.find(align='center').find('table').find('tr').find_all('td')[4].text,
        "Periodo":cont.find(align='center').find('table').find('tr').find_all('td')[5].text,
        "Profesor":datos[7].find_all(class_='tdprofesor')[1].text
    }
    print(registro)
    lista.append(registro)

# with open('INCE.json','a') as archivo:
#     json.dump(lista, archivo, sort_keys=False, indent = 4)
# nrc=datos[0].text
# print(nrc)
# clave=datos[1].a.text
# print(clave)
# materia=datos[2].a.text
# print(materia)
# seccion=datos[3].text
# print(seccion)
# creditos=datos[4].text
# print(creditos)
# cupos=datos[5].text
# print(cupos)
# disponible=datos[6].text
# print(disponible)
# hora=cont.find(align='center').find('table').find('tr').find_all('td')[1].text
# print(hora)
# dias=cont.find(align='center').find('table').find('tr').find_all('td')[2].text
# print(dias)
# edificio=cont.find(align='center').find('table').find('tr').find_all('td')[3].text
# print(edificio)
# aula=cont.find(align='center').find('table').find('tr').find_all('td')[4].text
# print(aula)
# periodo=cont.find(align='center').find('table').find('tr').find_all('td')[5].text
# print(periodo)
# profe=datos[7].find_all(class_='tdprofesor')[1].text
# print(profe)
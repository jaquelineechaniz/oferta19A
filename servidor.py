from flask import Flask, jsonify
app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(
    user='jaqueline',
    password='12345',
    database='proyecto'
)

cursor=conexion.cursor()

@app.route("/api/v1/oferta/")
def hello():
    query = "SELECT * FROM oferta"
    selectMat = 'SELECT * FROM materia WHERE id = %s'
    selectHora = 'SELECT * FROM horas WHERE id = %s'
    selectDia = 'SELECT * FROM dias WHERE id = %s'
    selectPer = 'SELECT * FROM periodo WHERE id = %s'
    selectProfe = 'SELECT * FROM profesores WHERE id = %s'
    selectCarrera = 'SELECT * FROM carrera WHERE id = %s'
    selectAula = 'SELECT * FROM aula WHERE id = %s'
    selectEdif = 'SELECT * FROM edificio WHERE id = %s'
    cursor.execute(query)
    ofertas = cursor.fetchall()
    lista_oferta = []
    for oferta in ofertas:
        cursor.execute(selectMat, (oferta[6],))
        materia = cursor.fetchall()
        cursor.execute(selectHora, (oferta[7],))
        hora = cursor.fetchall()
        cursor.execute(selectDia, (oferta[8],))
        dia = cursor.fetchall()
        cursor.execute(selectPer, (oferta[10],))
        periodo = cursor.fetchall()
        cursor.execute(selectProfe, (oferta[11],))
        profesor = cursor.fetchall()
        cursor.execute(selectCarrera, (oferta[12],))
        carrera = cursor.fetchall()
        cursor.execute(selectAula, (oferta[9],))
        aula = cursor.fetchall()
        cursor.execute(selectEdif, (aula[0][2],))
        edificio = cursor.fetchall()
        o = {
            'ID':oferta[0],
            'Carrera':carrera[0][1],
            'NRC':oferta[1],
            'Clave':materia[0][1],
            'Materia':materia[0][2],
            'Seccion':oferta[2],
            'Creditos':oferta[3],
            'Cupos':oferta[4],
            'Disponible':oferta[5],
            'Hora':hora[0][1],
            'Dias':dia[0][1],
            'Edificio':edificio[0][1],
            'Aula':aula[0][1],
            'Periodo':periodo[0][1],
            'Profesor':profesor[0][1]
        }
        lista_oferta.append(o)
    return jsonify(lista_oferta)

app.run()
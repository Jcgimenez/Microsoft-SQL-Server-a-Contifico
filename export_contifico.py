import pyodbc
import requests
import json
from decimal import Decimal

# CONFIGURACION DE LA CONEXION A SQL SERVER
server = ''
database = ''
driver = '{ODBC Driver 17 for SQL Server}'

# CADENA DE CONEXION
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# NOMBRE DE LAS TABLA QUE SE DESEA EXPORTAR CLIENTES
nombre_tabla = ''

# CONSULTA SQL PARA SELECCIONAR LOS DATOS
consulta_sql = f'SELECT * FROM {nombre_tabla}'

# EJECUTAR LA CONSULTA
cursor.execute(consulta_sql)

# OBTENER TODOS LOS RESULTADOS DE LA CONSULTA
resultados = cursor.fetchall()

# CERRAR LA CONEXION A SQL SERVER
conn.close()

# URL DEL ENDPOINT PARA REALIZAR LA SOLICITUD POST EN CONTIFICO
url_contifico = ''

# API KEY PERSONALIZADA PARA LA AUTORIZACION
api_key = ''

# ITERAR SOBRE LOS RESULTADOS Y REALIZAR UNA SOLICITUD POST PARA CADA ELEMENTO
# PARA CLIENTES
for fila in resultados:
    # Convertir la fila a un diccionario
    fila_dict = dict(zip([column[0] for column in cursor.description], fila))

    # Convertir objetos Decimal a float antes de la serialización
    fila_dict = {key: float(value) if isinstance(value, Decimal) else value for key, value in fila_dict.items()}

    datos_a_enviar = {

    }

    # ENCABEZADOS CON LA API KEY PARA LA AUTORIZACION
    headers = {'Authorization': api_key}

    # REALIZAR LA SOLICITUD POST CON ENCABEZADOS
    respuesta = requests.post(url_contifico, json=datos_a_enviar, headers=headers)

    # VERIFICAR EL ESTADO DE LA RESPUESTA
    if respuesta.status_code == 200:
        print(respuesta.status_code)
    else:
        print(respuesta.status_code)
        print(respuesta.text)

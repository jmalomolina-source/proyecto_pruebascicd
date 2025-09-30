
import csv

import keyring

import sys

# Abre el fichero en modo de lectura ('r' de 'read')
# La sentencia 'with' se encarga de cerrarlo automáticamente
with open('../../entrada/datos.txt', 'r', encoding='utf-8') as archivo_txt:
    # Lee todas las líneas del fichero y las almacena en una lista
    lineas = archivo_txt.readlines()
    
# Ahora puedes trabajar con la lista de líneas fuera de la sentencia 'with'
print("Contenido del fichero XXXAAABBCCCDDDEEEE")
for linea in lineas:
    # La función .strip() elimina los espacios en blanco y saltos de línea al inicio y final
    print(linea.strip())
    
with open('../../entrada/empleados.csv', 'r', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv, delimiter=';')
    
    # Cada fila ahora es un diccionario
    for fila in lector:
        print(f"Nombre: {fila['nombre']}, Edad: {fila['edad']}")



datos = [
    ['nombre', 'edad', 'ciudad'],
    ['Ana', 25, 'Madrid'],
    ['Juan', 30, 'Barcelona']
]

estudiante = {
    "nombre": "Ana García",
    "edad": 22,
    "carrera": "Ingeniería Informática",
    "promedio": 8.7
}

with open('../../salida_tab2.csv', 'w', newline='', encoding='utf-8') as archivo_csv:

     escritor_csv = csv.writer(archivo_csv, delimiter=';')
     escritor_csv.writerows(estudiante)

     SERVICE_ID = "conexion.prueba" # Debe coincidir con el <TargetName> usado en cmdkey
     USUARIO = "jmalo"               # Debe coincidir con el <UserName> usado en cmdkey

     clave_recuperada = keyring.get_password(SERVICE_ID, USUARIO)
     print (clave_recuperada)

     print ("argumento:" + sys.argv[1])

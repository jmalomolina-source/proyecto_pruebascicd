import csv
import logging
import sys
import os
entorno = os.environ.get("ENTORNO","desa") 
print(entorno)
# 'level=logging.INFO' le dice a Python que muestre los mensajes INFO o superiores.
logging.basicConfig(level=logging.INFO, stream=sys.stdout) # Usamos sys.stdout para asegurar la salida a la consola


with open('datos.txt', 'r', encoding='utf-8') as archivo1:
# se puede indicar el directorio usando dir relativa partiendo de donde estas open('../entrada/datos.txt', ..
    # Lee todas las líneas del fichero y las almacena en una lista
    lineas1 = archivo1.readlines()
record_count_1 = sum(1 for row in lineas1)
print ("lineas fichero 1: " + str(record_count_1))

with open('empleados.csv', 'r', encoding='utf-8') as archivo2:
# se puede indicar el directorio usando dir relativa partiendo de donde estas open('../entrada/datos.txt', ..
    # Lee todas las líneas del fichero y las almacena en una lista
    lineas2 = archivo2.readlines()
record_count_2 = sum(1 for row in lineas2)
print ("lineas fichero 2: " + str(record_count_2))
if record_count_1 == record_count_2:
    logging.info("VERIFICACIÓN DE CALIDAD DE DATOS: El número de registros coincide.")
    exit(0)
else:
    logging.error("VERIFICACIÓN DE CALIDAD DE DATOS: El número de registros NO coincide.")
    exit(1)
import datetime
import os
import sys
if len(sys.argv) == 4:
#temp_c = input("Introduzca la temperatura en °C: ")
#humedad = input("Introduzca la humedad en %: ")
#llovio = input("Llovio recientemente, responda 'True' si llovio o 'False' si no llovio: ")
    temp_c = sys.argv[1]
    humedad = sys.argv[2]
    llovio = sys.argv[3]
    fecha_tiempo = datetime.datetime.now()
    fecha_hora = int(datetime.datetime.timestamp(fecha_tiempo))
    datos = str(f"{fecha_hora}, {temp_c}, {humedad}, {llovio}")
    print(fecha_tiempo, temp_c, humedad, llovio)
    print(datos)
    with open("clase09_ej2.csv", "a") as cl09:
        cl09.write(datos + "\n")
else:
    print("No introdujo la cantidad correcta de variables")
    print("Debe itroducir: 'temperatura', 'humedad', 'llovio': True o no llovio: False")



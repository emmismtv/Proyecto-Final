#INCIDENTES


import csv
from datetime import datetime

def registrar_incidente(filename):
    with open(filename, mode='w', newline='') as cvsfile:
        writer = csv.writer(cvsfile)
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        descripcion = input("Escriba el incidente:")
        gravedad= input("Escriba la gravedad (Alta, Media, Baja):")
        area = ["1", "2", "3", "4", "5"]
        nombrerep= input("Escriba su nombre por favor")
        writer.writerow([fecha_hora, descripcion, gravedad, area, nombrerep])
        print("Perfecto, el incidente ha sido registrado.")

registrar_incidente('c:/Users/bumbl/OneDrive/Escritorio/Algoritmos/incidentes.csv')


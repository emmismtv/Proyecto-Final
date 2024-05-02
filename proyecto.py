import csv
from datetime import datetime

def registrar_incidente(filename):
    with open(filename, mode='w', newline='') as cvsfile:
        writer = csv.writer(cvsfile)
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        descripcion = input("Escriba el incidente:")
        gravedad= input("Escriba la gravedad (Alta, Media, Baja):")
        area= ["Recursos humanos", "Auxiliares", "Administración"]
        writer.writerow([fecha_hora, descripcion, gravedad])
        print("Perfecto, el incidente ha sido registrado.")

registrar_incidente('incidentes.csv')
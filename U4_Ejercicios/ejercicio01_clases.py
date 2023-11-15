
import datetime

from dateutil.relativedelta import relativedelta


class Persona:
    def __init__(self, id, nombre, apellidos, fecha_nacimiento):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar(self):
        print(f"Nombre: {self.nombre} Apellidos: {self.apellidos}\n")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")

    def getEdad(self):
        hoy = datetime.date.today()
        edad = relativedelta(hoy, self.fecha_nacimiento).years
        return edad

    def __str__(self):
        return f"""Persona: {self.nombre} {self.apellidos} 
                ({self.id})-{self.getEdad()} años"""
                
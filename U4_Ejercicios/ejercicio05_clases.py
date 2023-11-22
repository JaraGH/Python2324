class Alojamiento:

    def __init__(self, id, nombre, categoria):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self) -> str:
        return f"{self.id} {self.nombre} {self.categoria}"   

class Hotel (Alojamiento):

    def __init__(self, id, nombre, categoria, numero_habitaciones):
        super().__init__(id, nombre, categoria)
        self.numero_habitaciones = numero_habitaciones

    def __str__(self) -> str:
        return super().__str__() + f" {self.numero_habitaciones}"


class CasaRural (Alojamiento):

    def __init__(self, id, nombre, categoria, chimenea, garaje, numero_camas):   
        super().__init__(id, nombre, categoria)
        self.chimenea = chimenea
        self.garaje = garaje
        self.numero_camas = numero_camas
    
    def __str__(self) -> str:
        return super().__str__() + f" {self.chimenea} {self.garaje} {self.numero_camas}"

####################################################################################

class Dao:

    alojamientos = []

    def insertar(self, alojamiento):
        self.alojamientos.append(alojamiento)

    def buscar (self, id):

        for a in self.alojamientos:
            if a.id==id:
                return a
        return None

    def alojamientosDelTipo(self, tipo):

        retorno = []
        for a in self.alojamientos:
            if tipo=="Hotel" and isinstance(a, Hotel):
                retorno.append(a)
            elif tipo=="CasaRural" and isinstance(a, CasaRural):
                retorno.append(a)
        return retorno
    
    # hacer uso del polimorfismo
    def mostrarTodos(self):
        for a in self.alojamientos:
            print(a)

####################################################################################










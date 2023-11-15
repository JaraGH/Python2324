class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def getValor(self):
        return self.valor
    
    def getSiguiente(self):
        return self.siguiente


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo = Elemento(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            inicio = self.cabeza
            while inicio.getSiguiente() is not None:
                inicio = inicio.getSiguiente()
            inicio.siguiente = nuevo

    def mostrar(self):
        inicio = self.cabeza
        while inicio is not None:
            print(inicio.getValor())
            inicio = inicio.getSiguiente()

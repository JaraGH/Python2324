class Empleado:
    def __init__(self, id, nombre, apellidos, salario, departamento):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.salario = salario
        self.departamento = departamento
    
    def __str__(self):
        return f"Empleado: {self.id} {self.nombre} {self.apellidos} {self.salario} {self.departamento}"


class GestionEmpleados:

    lista_empleados = []

    def __init__(self):
        pass

    def insertar(self, empleado):
        self.lista_empleados.append(empleado)
    
    def mostrar(self):
        for empleado in self.lista_empleados:
            print(empleado)
    
    def b_apellido(self, apellidos):
        for empleado in self.lista_empleados:
            if empleado.apellidos.lower() == apellidos.lower():
                return empleado
        return -1

    def b_id(self, id):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                return empleado
        return -1

    def buscar(self, id, apellidos):
        if apellidos is not None:
            return self.b_apellido(apellidos)
        elif id is not None:
            return self.b_id(id)
        else:
            return -1

    def eliminar(self, id):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                self.lista_empleados.remove(empleado)
                return True
        return False
    
    def actualizarSalario(self, idBuscado, nuevo_salario):
        e = self.buscar(id=idBuscado, apellidos=None)
        if e != -1:
            e.salario = nuevo_salario
            return True
        return False



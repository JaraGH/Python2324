from ejercicio03_clases import *


g = GestionEmpleados()

g.insertar(Empleado(1, "Juan", "García", 1000, "Informática"))
g.insertar(Empleado(2, "Ana", "Rosas", 2000, "Informática"))
g.insertar(Empleado(3, "Gema", "Losa", 1500, "Personal"))
g.insertar(Empleado(4, "Tomás", "Rosas", 2500, "Personal"))

# mostrar todos los empleados
# g.mostrar()

# buscar por id
e = g.buscar(id=1, apellidos=None)
print(e)

# buscar por apellidos
e = g.buscar(id=None, apellidos="Rosas")
print(e)

e = g.buscar(id=None, apellidos="Rosasrrrrrr")
print(e)

# eliminar por id
rtdo = g.eliminar(1)
print(rtdo)

# modificar salario
g.actualizarSalario(2, 9999)

# mostrar todos los empleados
g.mostrar()

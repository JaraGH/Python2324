from ejercicio05_clases import *

a = Arbol()

r = a.insert(None, 10)
r = a.insert(r, 5)
r = a.insert(r, 15)
r = a.insert(r, 25)
r = a.insert(r, 175)


a.inorder(r)

print(a.buscar(r, 12))
print(a.buscar(r, 12))



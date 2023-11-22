from ejercicio05_clases import *

dao = Dao()

dao.insertar(Hotel(1, "Hotel 1", "3 estrellas", 100))
dao.insertar(Hotel(2, "Hotel 2", "2 estrellas", 156))
dao.insertar(Hotel(3, "Hotel 3", "4 estrellas", 200))
dao.insertar(CasaRural(4, "Casa Rural 1", "2 espigas", True, False, 4))
dao.insertar(CasaRural(5, "Casa Rural 2", "3 espigas", False, True, 6))
dao.insertar(CasaRural(6, "Casa Rural 3", "1 espiga", True, True, 2))


# l = dao.alojamientosDelTipo("Hotel")
# for a in l:
#     print(a)

# hotel_buscado = dao.buscar(22)
# if hotel_buscado != None:
#     print(hotel_buscado)

dao.mostrarTodos()
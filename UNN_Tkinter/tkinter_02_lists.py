import tkinter as tk
from tkinter import messagebox

def cargarNumerosLista():
    for num in range(1,101):
        listbox.insert(tk.END, num)

def eliminarSeleccionado():
    listbox.delete(listbox.curselection())


# creación de la ventana principal
window = tk.Tk()
#título de la ventana
window.title('Listas')
#dimensiones de la ventana
window.geometry('400x200')

#añadir una lista
listbox = tk.Listbox(window)
listbox.pack()
cargarNumerosLista()

#añadir un botón
button = tk.Button(window, text='Eliminar seleccionado', command=eliminarSeleccionado)
button.pack()

#ejecuta el método Tkinter loop
#para escuchar eventos como clicks, keypresses, etc.
window.mainloop()


import tkinter as tk
from tkinter import messagebox

def saludar():
    message = "Hola " + text.get()
    messagebox.showinfo(message=message)

# creación de la ventana principal
window = tk.Tk()
#título de la ventana
window.title('Ejercicio 2')
#dimensiones de la ventana
window.geometry('400x200')

#añadir un label
label = tk.Label(window, text='Introduce tu nombre')
#este método coloca el label en la ventana
label.pack()

#añadir una entrada de texto
text = tk.Entry(window)
text.pack()

#añadir un botón
button = tk.Button(window, text='Haz click aquí', command=saludar)
button.pack()

#ejecuta el método Tkinter loop
#para escuchar eventos como clicks, keypresses, etc.
window.mainloop()


import tkinter as tk

# creación de la ventana principal
window = tk.Tk()
#título de la ventana
window.title('Ventana Hello World')
#dimensiones de la ventana
window.geometry('300x200')

#ejecuta el método Tkinter loop
#para escuchar eventos como clicks, keypresses, etc.
window.mainloop()
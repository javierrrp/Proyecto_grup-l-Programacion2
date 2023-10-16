import tkinter as tk
from tkinter import simpledialog, ttk
import customtkinter as ctk
nRes = [440, 330]
def crear_lista():
    lista = []
    for i in range(10):
        root = tk.Tk()
        root.withdraw()
        value = simpledialog.askinteger("Ingrese un numero:", "Numero:")
        root.destroy()
        lista.append(value)
    return lista
def ordenar(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
        label.config(text=f"Lista: {lista}")
        win.update()
        win.after(100) 
    return lista
lista_creada = crear_lista()
win = ctk.CTk()
win._set_appearance_mode('light')
win.title('Proyecto acumulativo')
win.iconbitmap('Logo.ico')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)
fuente = ctk.CTkFont(family='Times New Roman', size=12)
label = tk.Label(win, text=f"Lista: {lista_creada}")
label.pack()
botonordena = ttk.Button(text="ordena esta lista", command=lambda: ordenar(lista_creada))
botonordena.place(x=50, y=80)
win.mainloop()
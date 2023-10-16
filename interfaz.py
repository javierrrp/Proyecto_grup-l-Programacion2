import tkinter as tk
from tkinter import simpledialog
import customtkinter as ctk

nRes = [1200, 800]

def crear_lista():
    lista = []
    for i in range(10):
        root = tk.Tk()
        root.withdraw()
        value = simpledialog.askinteger("Ingrese un numero:", "Numero:")
        root.destroy()
        lista.append(value)
    return lista





lista_creada = crear_lista()

win = ctk.CTk()
win._set_appearance_mode('light')
win.title('Proyecto Transdiciplinario: Trabajo y Energia')
win.iconbitmap('Logo.ico')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)
fuente = ctk.CTkFont(family='Times New Roman', size=12)

label = tk.Label(win, text=f"Lista: {lista_creada}")
label.pack()

win.mainloop()

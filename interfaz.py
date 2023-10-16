import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import customtkinter as ctk
nRes = [440, 330]
def crear_lista():
    lista = []
    for i in range(10):
        root = tk.Tk()
        root.withdraw()
        try:
            value = simpledialog.askinteger("Ingrese un numero:", "Numero:")
            if value is not None:
                lista.append(value)
            else:
                messagebox.showerror("Error, debes ingresar un numero valido")
        except ValueError as erroe:
            messagebox.showerror("Error" f"{erroe}")
        root.destroy()
    return lista
def ordenar(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
        label.config(text=f"{lista}")
        win.update()
        win.after(100) 
    return lista


def change_color():
    win.config(background="black")
    if botoncolor["text"] == "Modo Oscuro":
        botoncolor["text"] = "Modo claro"
    else:
        botoncolor["text"] = "Modo Oscuro"
        win.config(background='white')

lista_creada = crear_lista()
win = ctk.CTk()
win._set_appearance_mode('light')
win.title('Proyecto acumulativo')
win.iconbitmap('Logo.ico')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)

fuente = ctk.CTkFont(family='Times New Roman', size=33)
label = tk.Label(win, font=fuente, text=f"{lista_creada}")
label.pack()
botonordena = ttk.Button(text="ordena esta lista", command=lambda: ordenar(lista_creada))
botonordena.place(x=50, y=80)
botonordena.pack()

botoncolor = ttk.Button(text="Modo Oscuro", command=change_color)
botoncolor.place(x=50, y=60)
botoncolor.pack()

win.mainloop()
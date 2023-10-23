#Javier Poblete y Matias Leal
#Programacion II

import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import customtkinter as ctk 
import time

nRes = [600, 400]

def crear_lista():

    lista = [] 
    while True:
        try:
            root = tk.Tk() 
            root.withdraw() 
            value = simpledialog.askstring("Ingrese un número:", "Número:") 
            root.destroy()
            if value is None:
                root.destroy()
            if value == "stop":
                break

            if value is not None:
                value = int(value)
                lista.append(value)

            else:
                messagebox.showerror("Error", "Debes ingresar un número válido")
        except ValueError: 
                messagebox.showerror("Error", "Debes ingresar un número válido")

    return lista 



def binary_search(lista, numero_buscado):
    izquierda, derecha = 0, len(lista) - 1
    primer_indice = -1  

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero_buscado:
            primer_indice = medio 
            derecha = medio - 1  
        elif lista[medio] < numero_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    if primer_indice != -1:
        return primer_indice 
    else:
        return -1 


def ordenar(lista, label): 
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            label.config(text=f"Ordenando: {lista}", font=("Times New Roman", 20))
            label.update()
            win.update()
            win.after(100)
            time.sleep(0.5)
            
            label.config(text=f"Lista ordenada: {lista}", font=("Times New Roman", 20))
            label.update()

def change_color():
    fondo = win.cget('background')
    if fondo == "black":
        win.config(background="white")
        botoncolor["text"] = "Modo Oscuro"
    else:
        win.config(background="black")
        botoncolor["text"] = "Modo Claro"

lista_creada = crear_lista()


win = ctk.CTk()
win._set_appearance_mode('light')
win.title('Proyecto acumulativo')
win.iconbitmap('Logo.ico')

win.geometry('600x400')

win.resizable(False, False)

fuente = ctk.CTkFont(family='Times New Roman', size=12)
label = tk.Label(win, text=f"Lista: {lista_creada}", font=("Times New Roman", 20))
label.pack()

botonordena = ttk.Button(win, text="Ordenar esta lista", command=lambda: ordenar(lista_creada, label))
botonordena.place(x=700, y=500)
botonordena.pack()

botoncolor = ttk.Button(win, text="Modo Oscuro", command=change_color)
botoncolor.place(x=700, y=500)
botoncolor.pack()
def buscar():
    try:
        numero_buscado_str = simpledialog.askstring("Buscar número", "Ingrese el número que desea buscar:")
        if numero_buscado_str is not None:
            numero_buscado = int(numero_buscado_str)
            lista_creada_ordenada = lista_creada[:]
            ordenar(lista_creada_ordenada, label)
            indice = binary_search(lista_creada_ordenada, numero_buscado)
            if indice != -1:
                messagebox.showinfo("Resultado", f"El número {numero_buscado} existe en la lista en la posición {indice}.")
            else:
                messagebox.showinfo("Resultado", f"El número {numero_buscado} no existe en la lista.")
        else:
            messagebox.showerror("Error", "Debes ingresar un número válido.")
            return None
    except ValueError: 
        messagebox.showerror("Error", "Debes ingresar un número válido")
        return


botonbuscar = ttk.Button(win, text="Buscar número", command=buscar)
botonbuscar.place(x=711100, y=60)
botonbuscar.pack()

win.mainloop()
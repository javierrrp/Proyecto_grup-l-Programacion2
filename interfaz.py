#Javier Poblete y Matias Leal
#Programacion II




import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import customtkinter as ctk

nRes = [600, 400]

def crear_lista():
    lista = [] #Crear lista vacia
    for i in range(10): #repetir 10 veces
        root = tk.Tk()
        root.withdraw()
        value = simpledialog.askinteger("Ingrese un numero:", "Numero:") #pedira 10 veces ingresar un numero
        if value is not None: #si no es un dato vacio, agrega el numero a la lista
            lista.append(value)
        else:
            messagebox.showerror("Error", "Debes ingresar un número válido") 
            root.destroy()
            return None  # Salir si el  usuario presiona "Cancelar"
        root.destroy()
    return lista #retorna la lista creada

def buscar_exponencial(lista, numero_buscado): 
    if lista[0] == numero_buscado: #si el primer elemento de la lista es igualito al numero buscado, devuelve 0
        return 0

    i = 1
    while i < len(lista) and lista[i] <= numero_buscado: #mientras i sea menor a la longitud de la lista y el elemento en posicion i de la lista es menor o igual al numero buscado, i se duplica en cada iteración, se avanza exponencialmente a través de la lista
        i *= 2

    return binary_search(lista, numero_buscado, i // 2, min(i, len(lista) - 1)) 

def binary_search(lista, numero_buscado, izquierda, derecha):
    # El siguiente bucle se ejecuta mientras el rango de búsqueda (izquierda a derecha) es válido.
    while izquierda <= derecha:
        # Calcula el punto medio entre los índices izquierda y derecha.
        medio = izquierda + (derecha - izquierda) // 2

        # revisa si el elemento en la posición media de la lista es igual al número buscado.
        if lista[medio] == numero_buscado:
            # si se encuentra una coincidencia, se devuelve el índice del elemento encontrado.
            return medio
        # si el elemento del medio es menor que el número buscado, limita la búsqueda a la mitad derecha de la lista.
        elif lista[medio] < numero_buscado:
            izquierda = medio + 1
        # si el elemento del medio es mayor que el número buscado, limita la búsqueda a la mitad izquierda de la lista.
        else:
            derecha = medio - 1

    # Si el ciclo termina y no se encontró el número, retorna -1 para indicar que no se encontró en la lista.
    return -1



def ordenar(lista, label): 
    #Ordenamiento por Insercion
    for i in range(1, len(lista)): 
        key = lista[i]
        j = i - 1 # usamos j para comparar con elementos anteriores.
        while j >= 0 and lista[j] > key:
            # Si el elemento en en indice j en lista es mayor que 'key', se mueve a la derecha.
            lista[j + 1] = lista[j]
            j -= 1
             #mostrar el proceso de ordenamiento en la interfaz gráfica.
            label.config(text=f"Ordenando: {lista}", font=("Times New Roman", 20))
            label.update()
            win.update()
            win.after(100)
            # Inserta key en la posición correcta dentro de la lista ordenada.
        lista[j + 1] = key
    label.config(text=f"Lista ordenada: {lista}", font=("Times New Roman", 20))
    label.update()

def change_color():
    current_bg_color = win.cget('background')
    if current_bg_color == "black":
        win.config(background="white")
        botoncolor["text"] = "Modo Oscuro"
    else:
        win.config(background="black")
        botoncolor["text"] = "Modo Claro"

#Lista creada mas arriba
lista_creada = crear_lista()
if lista_creada is None:
    exit()  

win = ctk.CTk()
win._set_appearance_mode('light')
win.title('Proyecto acumulativo')
win.iconbitmap('Logo.ico')

#resolucion
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
    numero_buscado = simpledialog.askinteger("Buscar número", "Ingrese el número que desea buscar:") #Pregunta el numero a buscar
    #si el numero buscado no es "none", reemplaza la lista ordenada por la creada
    if numero_buscado is not None:
        lista_creada_ordenada = lista_creada[:]
        #llamamos funcion para ordenar
        ordenar(lista_creada_ordenada, label)
        indice = buscar_exponencial(lista_creada_ordenada, numero_buscado)
        if indice != -1:
            messagebox.showinfo("Resultado", f"El número {numero_buscado} existe en la lista en la posición {indice}.")
        else:
            messagebox.showinfo("Resultado", f"El número {numero_buscado} no existe en la lista.")
    else:
        messagebox.showerror("Error", "Debes ingresar un número válido.")


botonbuscar = ttk.Button(win, text="Buscar número", command=buscar)
botonbuscar.place(x=711100, y=60)
botonbuscar.pack()

win.mainloop()
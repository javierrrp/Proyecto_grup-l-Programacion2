import tkinter as tk
from tkinter import simpledialog, ttk, messagebox

nRes = [600, 400]
modo_oscuro = False

def crear_lista():
    lista = []
    for i in range(2):
        root = tk.Tk()
        root.withdraw()
        value = simpledialog.askinteger("Ingrese un número:", "Número:")
        if value is not None:
            lista.append(value)
        else:
            messagebox.showerror("Error", "Debes ingresar un número válido")
            root.destroy()
            return None
        root.destroy()
    return lista

def buscar_exponencial(lista, numero_buscado):
    if lista[0] == numero_buscado:
        return 0

    i = 1
    while i < len(lista) and lista[i] <= numero_buscado:
        i *= 2

    return binary_search(lista, numero_buscado, i // 2, min(i, len(lista) - 1))

def binary_search(lista, numero_buscado, izquierda, derecha):
    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2
        if lista[medio] == numero_buscado:
            return medio
        elif lista[medio] < numero_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def ordenar(lista, label):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
            label.config(text=f"Ordenando: {lista}")
            win.update()
            win.after(100)
        lista[j + 1] = key
    label.config(text=f"Lista ordenada: {lista}")
    win.update()

def toggle_modo():
    global modo_oscuro
    if modo_oscuro:
        win.configure(bg="white")
        modo_oscuro = False
    else:
        win.configure(bg="black")
        modo_oscuro = True

def buscar():
    numero_buscado = simpledialog.askinteger("Buscar número", "Ingrese el número que desea buscar:")
    if numero_buscado is not None:
        lista_creada_ordenada = lista_creada[:]
        ordenar(lista_creada_ordenada, label)
        indice = buscar_exponencial(lista_creada_ordenada, numero_buscado)
        if indice != -1:
            messagebox.showinfo("Resultado", f"El número {numero_buscado} existe en la lista en la posición {indice}.")
        else:
            messagebox.showinfo("Resultado", f"El número {numero_buscado} no existe en la lista.")
    else:
        messagebox.showerror("Error", "Debes ingresar un número válido")

lista_creada = crear_lista()
if lista_creada is None:
    exit()
win = tk.Tk()
win.title('Proyecto acumulativo')

win.geometry('800x400')

win.configure(bg="white")

label = tk.Label(win, text=f"Lista: {lista_creada}", font=("Times New Roman", 16), fg="black")
label.pack(pady=10)

frame_botones = tk.Frame(win)
frame_botones.pack()

s = ttk.Style()
s.configure('ModoOscuro.TButton', background='black', foreground='white')
s.configure('ModoClaro.TButton', background='white', foreground='black')

botonordena = ttk.Button(frame_botones, text="Ordenar lista", command=lambda: ordenar(lista_creada, label), style='ModoClaro.TButton')
botonordena.grid(row=0, column=0, pady=20)

botonbuscar = ttk.Button(frame_botones, text="Buscar número", command=buscar, style='ModoClaro.TButton')
botonbuscar.grid(row=1, column=0, pady=20)

botoncolor = ttk.Button(frame_botones, text="Cambiar Modo", command=toggle_modo, style='ModoClaro.TButton')
botoncolor.grid(row=2, column=0, pady=20)

win.mainloop()

import tkinter as tk

def agregar_numero():
    numero = int(entry1.get())
    arreglo.append(numero)
    label_lista.config(text=str(arreglo))
    entry1.delete(0,tk.END)

def buscar_numero():
    numero = int(entry2.get())
    encontrado = False
    for i, num in enumerate(arreglo):
        if num == numero:
            encontrado = True
            indice = i
            break

    if encontrado:
        resultado.set(f"El número {numero} fue encontrado en el índice {indice}.")
    else:
        resultado.set(f"El número {numero} no fue encontrado en la lista.")
    entry2.delete(0,tk.END)

ventana = tk.Tk()
ventana.geometry("350x230")
ventana.title("Búsqueda Lineal - Marlon Varela")

label_lista = tk.Label(ventana, text= " ")
label_lista.pack()

label1 = tk.Label(ventana, text = "Ingrese numeros a la lista")
label1.pack()

entry1 = tk.Entry(ventana)
entry1.pack()

boton1 = tk.Button(ventana, text = "Agregar", command=agregar_numero)
boton1.pack()

labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

label2 = tk.Label(ventana, text="Ingrese un numero para buscar:")
label2.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

boton2 = tk.Button(ventana, text="Buscar", command=buscar_numero)
boton2.pack()

resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()

arreglo = []

ventana.mainloop()

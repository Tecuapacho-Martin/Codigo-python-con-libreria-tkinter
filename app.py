import tkinter as tk
def saludar():
 #holalala prueba shdhajdgw
 nombre = entrada.get()
 etiqueta_resultado.config(text=f"Hola {nombre}")
def edad():
  edad = entrada2.get() 
  etiqueta_res.config(text=f"Tu edad es {edad}")
ventana = tk.Tk()
ventana.title("Mi primera app grafica") #Modicamos el nombre
ventana.geometry("400x200") #Modificamos el tamaño a 400x200
# Aqui son todo la linea de codigo para ingresar el nombre
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:", bg = "lavender")# Agrege colores a los botones
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack()
boton = tk.Button(ventana, text="Mostrar saludo", command=saludar, bg = "lightcyan") #Cambiamos el mensaje del boton 
boton.pack()
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()
# Aqui son todo la linea de codigo para ingresar la edad
etiqueta2 = tk.Label(ventana, text="Ingresa tu edad", bg = "lavender")
etiqueta2.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()
boton2 = tk.Button(ventana, text="Tu edad es", command=edad, bg = "lightcyan")
boton2.pack()
etiqueta_res = tk.Label(ventana, text="")
etiqueta_res.pack()
etiqueta_autor = tk.Label(ventana, text="Martin Tecuapacho Diaz") # Agrege mi nombre a la ventana
etiqueta_autor.pack()
ventana.config(bg ="Light blue") # Cambiamos el color de la ventana
ventana.mainloop()


import tkinter as tk
import re

class Ciudad:
    def __init__(self, nombre, pais, poblacion, area):
        self.nombre = nombre
        self.pais = pais
        self.poblacion = poblacion
        self.area = area

class VentanaCiudad:
    def __init__(self, root):
        self.root = root
        self.root.title("Crear Ciudad")
        self.root.geometry("300x350")

        self.nombre_label = tk.Label(root, text="Nombre de la ciudad:")
        self.nombre_label.pack()

        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        self.nombre_validacion_label = tk.Label(root, text="")
        self.nombre_validacion_label.pack()

        self.pais_label = tk.Label(root, text="Pais de la ciudad:")
        self.pais_label.pack()

        self.pais_entry = tk.Entry(root)
        self.pais_entry.pack()

        self.pais_validacion_label = tk.Label(root, text="")
        self.pais_validacion_label.pack()

        self.poblacion_label = tk.Label(root, text="Poblacion de la ciudad:")
        self.poblacion_label.pack()

        self.poblacion_entry = tk.Entry(root)
        self.poblacion_entry.pack()

        self.poblacion_validacion_label = tk.Label(root, text="")
        self.poblacion_validacion_label.pack()

        self.area_label = tk.Label(root, text="Area de la ciudad:")
        self.area_label.pack()

        self.area_entry = tk.Entry(root)
        self.area_entry.pack()

        self.area_validacion_label = tk.Label(root, text="")
        self.area_validacion_label.pack()

        self.mostrar_button = tk.Button(root, text="Crear Ciudad", command=self.crear_ciudad)
        self.mostrar_button.pack()

        self.atributos_label = tk.Label(root, text="")
        self.atributos_label.pack()

        self.nombre_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.nombre_entry, self.nombre_validacion_label, "^[a-zA-Z ]*$", "Solo se permiten letras y espacios"))
        self.pais_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.pais_entry, self.pais_validacion_label, "^[a-zA-Z ]*$", "Solo se permiten letras y espacios"))
        self.poblacion_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.poblacion_entry, self.poblacion_validacion_label, "^[0-9]*$", "Solo se permiten números"))
        self.area_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.area_entry, self.area_validacion_label, "^[0-9]*$", "Solo se permiten números"))

    def validar_campo(self, campo, etiqueta, patron, mensaje_error):
        valor = campo.get()
        resultado = re.compile(patron).match(valor) is not None
        if not resultado:
            etiqueta.config(text=mensaje_error, fg="red")
        else:
            etiqueta.config(text="", fg="black")

    def crear_ciudad(self):
        nombre = self.nombre_entry.get()
        pais = self.pais_entry.get()
        poblacion = self.poblacion_entry.get()
        area = self.area_entry.get()

        if nombre and pais and poblacion and area:
            ciudad = Ciudad(nombre, pais, poblacion, area)

            atributos = f"Nombre: {ciudad.nombre}\nPais: {ciudad.pais}\nPoblacion: {ciudad.poblacion}\nArea: {ciudad.area}"

            self.atributos_label.config(text=atributos)
        else:
            self.atributos_label.config(text="Por favor, complete todos los campos", fg="red")

root = tk.Tk()
ventana = VentanaCiudad(root)
root.mainloop()
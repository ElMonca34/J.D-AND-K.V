import tkinter as tk
import re

class Carro:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

class VentanaCarro:
    def __init__(self, root):
        self.root = root
        self.root.title("Atributos de un Carro")
        self.root.geometry("300x300")

        self.marca_label = tk.Label(root, text="Marca:")
        self.marca_label.pack()

        self.marca_entry = tk.Entry(root)
        self.marca_entry.pack()

        self.marca_validacion_label = tk.Label(root, text="")
        self.marca_validacion_label.pack()

        self.modelo_label = tk.Label(root, text="Modelo:")
        self.modelo_label.pack()

        self.modelo_entry = tk.Entry(root)
        self.modelo_entry.pack()

        self.modelo_validacion_label = tk.Label(root, text="")
        self.modelo_validacion_label.pack()

        self.año_label = tk.Label(root, text="Año:")
        self.año_label.pack()

        self.año_entry = tk.Entry(root)
        self.año_entry.pack()

        self.año_validacion_label = tk.Label(root, text="")
        self.año_validacion_label.pack()

        self.color_label = tk.Label(root, text="Color:")
        self.color_label.pack()

        self.color_entry = tk.Entry(root)
        self.color_entry.pack()

        self.color_validacion_label = tk.Label(root, text="")
        self.color_validacion_label.pack()

        self.mostrar_button = tk.Button(root, text="Mostrar Atributos", command=self.mostrar_atributos)
        self.mostrar_button.pack()

        self.atributos_label = tk.Label(root, text="")
        self.atributos_label.pack()

        self.marca_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.marca_entry, self.marca_validacion_label, "^[a-zA-Z]*$", "Solo se permiten letras"))
        self.modelo_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.modelo_entry, self.modelo_validacion_label, "^[a-zA-Z0-9]*$", "Solo se permiten letras"))
        self.año_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.año_entry, self.año_validacion_label, "^[0-9]*$", "Solo se permiten números"))
        self.color_entry.bind("<KeyRelease>", lambda event: self.validar_campo(self.color_entry, self.color_validacion_label, "^[a-zA-Z]*$", "Solo se permiten letras"))

    def validar_campo(self, campo, etiqueta, patron, mensaje_error):
        valor = campo.get()
        resultado = re.compile(patron).match(valor) is not None
        if not resultado:
            etiqueta.config(text=mensaje_error)
        else:
            etiqueta.config(text="")

    def mostrar_atributos(self):
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        año = self.año_entry.get()
        color = self.color_entry.get()

        if marca and modelo and año and color:
            carro = Carro(marca, modelo, año, color)

            atributos = f"Marca: {carro.marca}\nModelo: {carro.modelo}\nAño: {carro.año}\nColor: {carro.color}"

            self.atributos_label.config(text=atributos)
        else:
            self.atributos_label.config(text="Por favor, complete todos los campos")

root = tk.Tk()
ventana = VentanaCarro(root)
root.mainloop()

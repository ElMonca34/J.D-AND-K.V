import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.carro import carro
from .tabla import Tabla

class Interfaz:
    def __init__(self):
        titulos = ['Marca', 'Modelo', 'Año', 'Color', 'Precio']
        columnas = ['id', 'marca', 'modelo', 'año', 'color', 'precio']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)

    def accion_guardar_boton(self, id, marca, modelo, año, color, precio):
        if id == '':
            self.comunicacion.guardar(marca, modelo, año, color, precio)
        else:
            self.comunicacion.actualizar(id, marca, modelo, año, color, precio)

    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            labelConsulta.config(
                text=f"{resultado.get('marca', '')} {resultado.get('modelo', '')} {resultado.get('año', '')} {resultado.get('color', '')} {resultado.get('precio', '')}"
            )

    def accion_consultar_todo(self, marca, modelo, año, color, precio):
        resultado = self.comunicacion.consultar_todo(marca, modelo, año, color, precio)
        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'), elemento.get('marca'), elemento.get('modelo'),
                elemento.get('año'), elemento.get('color'), elemento.get('precio')
            ))
        self.tabla.refrescar(data)

    def mostrar_interfaz(self):
        usuario = carro(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)
        labelMarca = tk.Label(self.ventanaPrincipal, text="Marca")
        entryMarca = tk.Entry(self.ventanaPrincipal, textvariable=usuario.marca)
        labelModelo = tk.Label(self.ventanaPrincipal, text="Modelo")
        entryModelo = tk.Entry(self.ventanaPrincipal, textvariable=usuario.modelo)
        labelAño = tk.Label(self.ventanaPrincipal, text="Año")
        entryAño = tk.Entry(self.ventanaPrincipal, textvariable=usuario.año)
        labelColor = tk.Label(self.ventanaPrincipal, text="Color")
        entryColor = tk.Entry(self.ventanaPrincipal, textvariable=usuario.color)
        labelPrecio = tk.Label(self.ventanaPrincipal, text="Precio")
        entryPrecio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.precio)
        labelConsulta = tk.Label(self.ventanaPrincipal, text="Consulta")

        boton_guardar = tk.Button(self.ventanaPrincipal, text="Guardar", command=lambda: self.accion_guardar_boton(
            entryId.get(), entryMarca.get(), entryModelo.get(), entryAño.get(), entryColor.get(), entryPrecio.get()
        ))

        boton_consultar_1 = tk.Button(self.ventanaPrincipal, text="Consultar 1", command=lambda: self.accion_consultar_boton(
            labelConsulta, entryId.get()
        ))

        boton_consultar_todos = tk.Button(self.ventanaPrincipal, text="Consultar todos", command=lambda: self.accion_consultar_todo(
            entryMarca.get(), entryModelo.get(), entryAño.get(), entryColor.get(), entryPrecio.get()
        ))

        self.ventanaPrincipal.title("Gestión de Carros")
        self.ventanaPrincipal.geometry("1000x600")

        for widget in [
            labelId, entryId, labelMarca, entryMarca, labelModelo, entryModelo,
            labelAño, entryAño, labelColor, entryColor, labelPrecio, entryPrecio,
            boton_guardar, boton_consultar_1, boton_consultar_todos, labelConsulta
        ]:
            widget.pack()

        self.tabla.tabla.pack()

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                entryMarca.delete(0, tk.END)
                entryMarca.insert(0, str(valores[1]))
                entryModelo.delete(0, tk.END)
                entryModelo.insert(0, str(valores[2]))
                entryAño.delete(0, tk.END)
                entryAño.insert(0, str(valores[3]))
                entryColor.delete(0, tk.END)
                entryColor.insert(0, str(valores[4]))
                entryPrecio.delete(0, tk.END)
                entryPrecio.insert(0, str(valores[5]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()


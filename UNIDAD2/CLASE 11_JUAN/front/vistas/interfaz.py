import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.ciudad import ciudad
from .tabla import Tabla

class Interfaz:
    def __init__(self):
        titulos = ['Ciudad', 'Población', 'Área', 'País']
        columnas = ['id', 'ciudad', 'poblacion', 'area', 'pais']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)

    def accion_guardar_boton(self, id, ciudad, poblacion, area, pais):
        if id == '':
            self.comunicacion.guardar(ciudad, poblacion, area, pais)
        else:
            self.comunicacion.actualizar(id, ciudad, poblacion, area, pais)

    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            labelConsulta.config(
                text=f"{resultado.get('ciudad', '')} {resultado.get('poblacion', '')} {resultado.get('area', '')} {resultado.get('pais', '')}"
            )

    def accion_consultar_todo(self, ciudad, poblacion, area, pais):
        resultado = self.comunicacion.consultar_todo(ciudad, poblacion, area, pais)
        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'), elemento.get('ciudad'), elemento.get('poblacion'),
                elemento.get('area'), elemento.get('pais')
            ))
        self.tabla.refrescar(data)

    def mostrar_interfaz(self):
        usuario = ciudad(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)
        labelCiudad = tk.Label(self.ventanaPrincipal, text="Ciudad")
        entryCiudad = tk.Entry(self.ventanaPrincipal, textvariable=usuario.ciudad)
        labelPoblacion = tk.Label(self.ventanaPrincipal, text="Población")
        entryPoblacion = tk.Entry(self.ventanaPrincipal, textvariable=usuario.poblacion)
        labelArea = tk.Label(self.ventanaPrincipal, text="Área")
        entryArea = tk.Entry(self.ventanaPrincipal, textvariable=usuario.area)
        labelPais = tk.Label(self.ventanaPrincipal, text="País")
        entryPais = tk.Entry(self.ventanaPrincipal, textvariable=usuario.pais)
        labelConsulta = tk.Label(self.ventanaPrincipal, text="Consulta")

        boton_guardar = tk.Button(self.ventanaPrincipal, text="Guardar", command=lambda: self.accion_guardar_boton(
            entryId.get(), entryCiudad.get(), entryPoblacion.get(), entryArea.get(), entryPais.get()
        ))

        boton_consultar_1 = tk.Button(self.ventanaPrincipal, text="Consultar 1", command=lambda: self.accion_consultar_boton(
            labelConsulta, entryId.get()
        ))

        boton_consultar_todos = tk.Button(self.ventanaPrincipal, text="Consultar todos", command=lambda: self.accion_consultar_todo(
            entryCiudad.get(), entryPoblacion.get(), entryArea.get(), entryPais.get()
        ))

        self.ventanaPrincipal.title("Gestión de Ciudades")
        self.ventanaPrincipal.geometry("1000x600")

        for widget in [
            labelId, entryId, labelCiudad, entryCiudad, labelPoblacion, entryPoblacion,
            labelArea, entryArea, labelPais, entryPais,
            boton_guardar, boton_consultar_1, boton_consultar_todos, labelConsulta
        ]:
            widget.pack()

        self.tabla.tabla.pack()

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                entryCiudad.delete(0, tk.END)
                entryCiudad.insert(0, str(valores[1]))
                entryPoblacion.delete(0, tk.END)
                entryPoblacion.insert(0, str(valores[2]))
                entryArea.delete(0, tk.END)
                entryArea.insert(0, str(valores[3]))
                entryPais.delete(0, tk.END)
                entryPais.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()
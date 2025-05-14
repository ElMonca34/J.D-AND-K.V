import tkinter as tk
from tkinter import ttk

class Tabla:
    def __init__(self, master, titulos, columnas, data):
        self.tabla = ttk.Treeview(master, columns=columnas, show='headings')

        for col, title in zip(columnas, titulos):
            self.tabla.heading(col, text=title)
            self.tabla.column(col, width=100)

        self.refrescar(data)

    def refrescar(self, data):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for fila in data:
            self.tabla.insert('', tk.END, values=fila)

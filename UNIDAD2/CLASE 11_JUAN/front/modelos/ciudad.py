import tkinter as tk

class ciudad:
    def __init__(self, master):
        self.id = tk.StringVar(master)
        self.ciudad = tk.StringVar(master)
        self.poblacion = tk.StringVar(master)
        self.area = tk.StringVar(master)
        self.pais = tk.StringVar(master)
        self.pais.set('')
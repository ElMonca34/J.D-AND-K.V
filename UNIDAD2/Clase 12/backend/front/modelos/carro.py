import tkinter as tk

class carro:
    def __init__(self, master):
        self.id = tk.StringVar(master)
        self.marca = tk.StringVar(master)
        self.modelo = tk.StringVar(master)
        self.año = tk.StringVar(master)
        self.color = tk.StringVar(master)
        self.precio = tk.StringVar(master)
        self.precio.set('0')

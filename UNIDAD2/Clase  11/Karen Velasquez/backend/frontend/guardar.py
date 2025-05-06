import tkinter as tk
from tkinter import messagebox
import requests

# URL de la API de Django
API_URL = 'http://localhost:8000/api/carro/'

def buscar():
    carro_id = entry_id.get()
    if carro_id:
        response = requests.get(API_URL + carro_id + "/")
        if response.status_code == 200:
            data = response.json()
            entry_marca.delete(0, tk.END)
            entry_marca.insert(0, data['marca'])
            entry_modelo.delete(0, tk.END)
            entry_modelo.insert(0, data['modelo'])
            entry_año.delete(0, tk.END)
            entry_año.insert(0, data['año'])
            entry_color.delete(0, tk.END)
            entry_color.insert(0, data['color'])
            entry_precio.delete(0, tk.END)
            entry_precio.insert(0, data['precio'])
        else:
            messagebox.showerror("Error", "Carro no encontrado")

def guardar():
    data = {
        "marca": entry_marca.get(),
        "modelo": entry_modelo.get(),
        "año": int(entry_año.get()),
        "color": entry_color.get(),
        "precio": float(entry_precio.get())
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        messagebox.showinfo("Éxito", "Carro guardado")
    limpiar_campos()

def actualizar():
    carro_id = entry_id.get()
    if carro_id:
        data = {
            "marca": entry_marca.get(),
            "modelo": entry_modelo.get(),
            "año": int(entry_año.get()),
            "color": entry_color.get(),
            "precio": float(entry_precio.get())
        }
        response = requests.put(API_URL + carro_id + "/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Carro actualizado")
    limpiar_campos()

def eliminar():
    carro_id = entry_id.get()
    if carro_id:
        response = requests.delete(API_URL + carro_id + "/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Carro eliminado")
    limpiar_campos()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_marca.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_año.delete(0, tk.END)
    entry_color.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# Configuración de la ventana Tkinter
root = tk.Tk()
root.title("Gestión de Carros")

tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)
tk.Button(root, text="Buscar", command=buscar).grid(row=0, column=2)

tk.Label(root, text="Marca").grid(row=1, column=0)
entry_marca = tk.Entry(root)
entry_marca.grid(row=1, column=1)

tk.Label(root, text="Modelo").grid(row=2, column=0)
entry_modelo = tk.Entry(root)
entry_modelo.grid(row=2, column=1)

tk.Label(root, text="Año").grid(row=3, column=0)
entry_año = tk.Entry(root)
entry_año.grid(row=3, column=1)

tk.Label(root, text="Color").grid(row=4, column=0)
entry_color = tk.Entry(root)
entry_color.grid(row=4, column=1)

tk.Label(root, text="Precio").grid(row=5, column=0)
entry_precio = tk.Entry(root)
entry_precio.grid(row=5, column=1)

tk.Button(root, text="Guardar", command=guardar).grid(row=6, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=6, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=6, column=2)

root.mainloop()

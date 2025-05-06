import tkinter as tk
from tkinter import messagebox
import requests 

API_URL = 'http://localhost:8000/api/ciudad/'

def buscar():
    ciudad_id = entry_id.get()
    if ciudad_id:
        response = requests.get(API_URL + ciudad_id + "/")
        if response.status_code == 200:
            data = response.json()
            entry_ciudad.delete(0, tk.END)
            entry_ciudad.insert(0, data['ciudad'])
            entry_poblacion.delete(0, tk.END)
            entry_poblacion.insert(0, data['poblacion'])
            entry_area.delete(0, tk.END)
            entry_area.insert(0, data['area'])
            entry_pais.delete(0, tk.END)
            entry_pais.insert(0, data['pais'])
        else:
            messagebox.showerror("Error", "Ciudad no encontrada")

def guardar():
    data = {
        "ciudad": entry_ciudad.get(),
        "poblacion": int(entry_poblacion.get()),
        "area": float(entry_area.get()),
        "pais": entry_pais.get()
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        messagebox.showinfo("Éxito", "Ciudad guardada")
    limpiar_campos()

def actualizar():
    ciudad_id = entry_id.get()
    if ciudad_id:
        data = {
            "ciudad": entry_ciudad.get(),
            "poblacion": int(entry_poblacion.get()),
            "area": float(entry_area.get()),
            "pais": entry_pais.get()
        }
        response = requests.put(API_URL + ciudad_id + "/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Ciudad actualizada")
    limpiar_campos()

def eliminar():
    ciudad_id = entry_id.get()
    if ciudad_id:
        response = requests.delete(API_URL + ciudad_id + "/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Ciudad eliminada")
    limpiar_campos()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_poblacion.delete(0, tk.END)
    entry_area.delete(0, tk.END)
    entry_pais.delete(0, tk.END)

# Configuración de la ventana Tkinter
root = tk.Tk()
root.title("Gestión de Ciudades")

tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)
tk.Button(root, text="Buscar", command=buscar).grid(row=0, column=2)

tk.Label(root, text="Ciudad").grid(row=1, column=0)
entry_ciudad = tk.Entry(root)
entry_ciudad.grid(row=1, column=1)

tk.Label(root, text="Población").grid(row=2, column=0)
entry_poblacion = tk.Entry(root)
entry_poblacion.grid(row=2, column=1)

tk.Label(root, text="Área (km²)").grid(row=3, column=0)
entry_area = tk.Entry(root)
entry_area.grid(row=3, column=1)

tk.Label(root, text="País").grid(row=4, column=0)
entry_pais = tk.Entry(root)
entry_pais.grid(row=4, column=1)

tk.Button(root, text="Guardar", command=guardar).grid(row=5, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=5, column=2)

root.mainloop()
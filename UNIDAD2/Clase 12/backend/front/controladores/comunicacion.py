import requests

class Comunicacion:

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/carro/'
        self.ventanaPrincipal = ventanaPrincipal

    def guardar(self, marca, modelo, año, color, precio):
        try:
            data = {
                'marca': marca,
                'modelo': modelo,
                'año': int(año),
                'color': color,
                'precio': float(precio)
            }
            resultado = requests.post(self.url, json=data)
            return resultado
        except Exception as e:
            print("Error al guardar:", e)

    def actualizar(self, id, marca, modelo, año, color, precio):
        try:
            data = {
                'marca': marca,
                'modelo': modelo,
                'año': int(año),
                'color': color,
                'precio': float(precio)
            }
            resultado = requests.put(self.url + str(id) + '/', json=data)
            return resultado
        except Exception as e:
            print("Error al actualizar:", e)

    def consultar(self, id):
        try:
            resultado = requests.get(self.url + str(id) + '/')
            return resultado.json()
        except Exception as e:
            print("Error al consultar:", e)
            return {}

    def consultar_todo(self, marca, modelo, año, color, precio):
        url = self.url + "?"
        if marca != '':
            url += f"marca={marca}&"
        if modelo != '':
            url += f"modelo={modelo}&"
        if año != '':
            url += f"año={año}&"
        if color != '':
            url += f"color={color}&"
        if precio != '':
            url += f"precio={precio}&"
        try:
            resultado = requests.get(url)
            return resultado.json()
        except Exception as e:
            print("Error al consultar todos:", e)
            return []

    def eliminar(self, id):
        try:
            resultado = requests.delete(self.url + str(id) + '/')
            return resultado.status_code
        except Exception as e:
            print("Error al eliminar:", e)
            return None

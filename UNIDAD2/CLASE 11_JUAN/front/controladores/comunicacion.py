import requests

class Comunicacion:
    def __init__(self, ventanaPrincipal):
        self.url ='http://127.0.0.1:8000/api/ciudad/'
        self.ventanaPrincipal = ventanaPrincipal

    def guardar(self, ciudad, poblacion, area, pais):
        try:
            data = {
                'ciudad': ciudad,
                'poblacion': int(poblacion),
                'area': float(area),
                'pais': pais
            }
            resultado = requests.post(self.url, json=data)
            return resultado
        except Exception as e:
            print("Error al guardar:", e)

    def actualizar(self, id, ciudad, poblacion, area, pais):
        try:
            data = {
                'ciudad': ciudad,
                'poblacion': int(poblacion),
                'area': float(area),
                'pais': pais
            }
            resultado = requests.put(self.url + str(id) + '/', json=data)
            return resultado
        except Exception as e:
            print("Error al actualizar:", e)

    def consultar(self, id):
        try:
            resultado = requests.get(f"{self.url}{id}/")
            if resultado.status_code == 200:
                return resultado.json()
            else:
                print("Error al consultar - Código:", resultado.status_code)
                return {}
        except Exception as e:
            print("Error al consultar:", e)
            return {}

    def consultar_todo(self, ciudad, poblacion, area, pais):
        url = self.url + "?"
        if ciudad != '':
            url += f"ciudad={ciudad}&"
        if poblacion != '':
            url += f"poblacion={poblacion}&"
        if area != '':
            url += f"area={area}&"
        if pais != '':
            url += f"pais={pais}&"
        try:
            resultado = requests.get(url)
            if resultado.status_code == 200 and resultado.content:
                return resultado.json()
            else:
                print("Error al consultar todos - Código:", resultado.status_code)
                return []
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
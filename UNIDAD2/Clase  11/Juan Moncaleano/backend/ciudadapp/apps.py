from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_ciudad', methods=['POST'])
def agregar_ciudad():
    ciudad_data = {
        "ciudad": request.form['ciudad'],
        "poblacion": request.form['poblacion'],
        "area": request.form['area'],
        "pais": request.form['pais']
    }

    url = 'http://localhost:8000/api/ciudad/'
    response = requests.post(url, json=ciudad_data)

    if response.status_code == 201:
        return jsonify({"message": "ciudad creado con éxito!"}), 201
    else:
        return jsonify({"error": "Error al crear la ciudad"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

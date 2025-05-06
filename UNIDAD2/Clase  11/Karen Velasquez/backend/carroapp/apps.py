from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_carro', methods=['POST'])
def agregar_carro():
    carro_data = {
        "marca": request.form['marca'],
        "modelo": request.form['modelo'],
        "año": int(request.form['año']),
        "color": request.form['color'],
        "precio": float(request.form['precio'])
    }

    url = 'http://localhost:8000/api/cars/'
    response = requests.post(url, json=carro_data)

    if response.status_code == 201:
        return jsonify({"message": "Carro creado con éxito!"}), 201
    else:
        return jsonify({"error": "Error al crear el carro"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

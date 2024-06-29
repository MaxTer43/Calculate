from flask import Flask, request, jsonify
from scipy.integrate import quad
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# agrega soporte CORS para todos los endpoints, todos los origenes
CORS(app)

@app.route("/calculate", methods=['POST'])
def calculate_volume():
    data = request.get_json()
    a = float(data['start'])
    b = float(data['end'])
    area_function = lambda x: eval(data['area'])  # Convertir la función A(x) a una función evaluable
    volume, error = quad(area_function, a, b)
    return jsonify({'volume': round(volume, 2)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
import numpy as np
from scipy.integrate import quad
from starlette.middleware.cors import CORSMiddleware
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)


def area_function(x):
    # Aquí debes convertir la función A(x) recibida en una función evaluable
    return eval(request.json['area'])


@app.route('/calculate', methods=['POST'])
def calculate_volume():
    data = request.json
    a = float(data['start'])
    b = float(data['end'])
    area_function = lambda x: eval(data['area'])  # Convertir la función A(x) a una función evaluable
    volume, error = quad(area_function, a, b)
    return jsonify({'volume': round(volume, 2)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

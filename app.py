from flask import Flask, request, jsonify
import numpy as np
from scipy.integrate import quad

app = Flask(__name__)

def area_function(x):
    # Aquí debes convertir la función A(x) recibida en una función evaluable
    return eval(request.json['area'])

@app.route('/calculate', methods=['POST'])
def calculate_volume():
    data = request.json
    a = float(data['start'])
    b = float(data['end'])
    volume, error = quad(area_function, a, b)
    return jsonify({'volume': volume})

if __name__ == '__main__':
    app.run(debug=True)

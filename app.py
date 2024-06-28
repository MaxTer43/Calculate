from flask import Flask, request, jsonify
from scipy.integrate import quad
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/calculate")
def calculate_volume():
    data = request.json
    a = float(data['start'])
    b = float(data['end'])
    area_function = lambda x: eval(data['area'])  # Convertir la función A(x) a una función evaluable
    volume, error = quad(area_function, a, b)
    response = jsonify({'volume': round(volume, 2)})
    return response


def area_function(x):
    # Aquí debes convertir la función A(x) recibida en una función evaluable
    return eval(request.json['area'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

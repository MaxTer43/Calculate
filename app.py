from flask import Flask, request, jsonify
from scipy.integrate import quad
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=['POST'])
@cross_origin()
def calculate_volume():
    data = request.get_json()
    a = float(data['start'])
    b = float(data['end'])
    area_function = lambda x: eval(data['area'])  # Convertir la función A(x) a una función evaluable
    volume, error = quad(area_function, a, b)
    response = jsonify({'volume': round(volume, 2)})
    return response, 200, {'Access-Control-Allow-Origin':'*',
                                'Access-Control-Allow-Methods':'POST',
                                'Access-Control-Allow-Headers':'content-type'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

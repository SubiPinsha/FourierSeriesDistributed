from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import sympy as sp

app = Flask(__name__)
CORS(app)

@app.route('/calculate_b_n', methods=['POST'])
def calculate_b_n():
    data = request.json
    function = data['function']
    T = float(data['T'])
    n_terms = int(data['n_terms'])

    x = sp.Symbol('x')
    f = sp.sympify(function)

    b_n_values = {}

    for n in range(1, n_terms + 1):
        b_n = (2 / T) * sp.integrate(f * sp.sin((2 * np.pi * n * x) / T), (x, -T/2, T/2))
        b_n_values[f"b_{n}"] = float(b_n)

    return jsonify(b_n_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

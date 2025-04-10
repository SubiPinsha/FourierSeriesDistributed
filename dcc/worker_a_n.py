from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import sympy as sp

app = Flask(__name__)
CORS(app)

@app.route('/calculate_a_n', methods=['POST'])
def calculate_a_n():
    data = request.json
    function = data['function']
    T = float(data['T'])
    n_terms = int(data['n_terms'])

    x = sp.Symbol('x')
    f = sp.sympify(function)

    a_0 = (2 / T) * sp.integrate(f, (x, -T/2, T/2))
    a_n_values = {"a_0": float(a_0)}

    for n in range(1, n_terms + 1):
        a_n = (2 / T) * sp.integrate(f * sp.cos((2 * np.pi * n * x) / T), (x, -T/2, T/2))
        a_n_values[f"a_{n}"] = float(a_n)

    return jsonify(a_n_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

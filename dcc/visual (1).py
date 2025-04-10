from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to plot Fourier series graph
def plot_fourier_series(a_n, b_n, T, n_terms):
    # Create the x values
    x = np.linspace(-T/2, T/2, 1000)
    
    # Fourier series summation
    f_approx = np.zeros_like(x)
    for n in range(1, n_terms + 1):
        f_approx += a_n.get(f'a_{n}', 0) * np.cos(2 * np.pi * n * x / T) + b_n.get(f'b_{n}', 0) * np.sin(2 * np.pi * n * x / T)
    
    # Create plot
    fig, ax = plt.subplots()
    ax.plot(x, f_approx, label="Fourier Series Approximation")
    ax.set_title(f"Fourier Series Approximation with {n_terms} Terms")
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Save the figure as an image in memory
    img = io.BytesIO()
    FigureCanvas(fig).print_png(img)
    img.seek(0)
    
    # Encode the image to send back as a response
    img_b64 = base64.b64encode(img.getvalue()).decode('utf-8')
    return img_b64

@app.route('/plot_graph', methods=['POST'])
def plot_graph():
    data = request.json
    
    a_n = data.get('a_n', {})
    b_n = data.get('b_n', {})
    T = data.get('period', 1)
    n_terms = data.get('n_terms', 1)
    
    # Generate the Fourier Series graph
    graph_image = plot_fourier_series(a_n, b_n, T, n_terms)
    
    return jsonify({"graph_image": graph_image})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)  # Different port for visualization server

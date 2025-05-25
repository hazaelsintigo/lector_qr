from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_qr', methods=['POST'])
def procesar_qr():
    data = request.json.get('data')
    print(f"[QR RECIBIDO] {data}")
    return jsonify({'mensaje': 'QR procesado con éxito', 'contenido': data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

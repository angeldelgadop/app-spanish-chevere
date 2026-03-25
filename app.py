from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/corregir', methods=['POST'])
def corregir():
    datos = request.json
    texto_alumno = datos.get('texto')
    # Por ahora, simulamos la respuesta de la IA
    respuesta = f"¡Excelente intento! Tu frase '{texto_alumno}' es muy clara. En Spanish Chévere te sugerimos practicar los acentos."
    return jsonify({"feedback": respuesta})

if __name__ == "__main__":
    app.run()

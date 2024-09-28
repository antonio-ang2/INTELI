from flask import Flask, request, jsonify
import numpy as np
import cv2
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define o diretório onde as imagens serão salvas
SAVE_DIR = "detected_faces"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Rota principal
@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao Pond2!"})

# Função para processar a imagem e detectar faces
@app.route('/upload', methods=['POST'])
def process_image():
    # Verificar se o arquivo foi enviado
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo foi enviado"}), 400

    file = request.files['file']

    # Verificar se o tipo de arquivo é JPEG
    if file.content_type != 'image/jpeg':
        return jsonify({"error": "Somente arquivos JPEG são aceitos"}), 400

    # Ler o arquivo de imagem em bytes
    image_bytes = file.read()
    image_np = np.frombuffer(image_bytes, np.uint8)

    # Decodificar a imagem usando OpenCV
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    if img is None:
        return jsonify({"error": "Falha ao processar a imagem"}), 400

    # Carregar o classificador de face do OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar faces na imagem
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Desenhar retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Se houver faces detectadas, salvar a imagem processada
    if len(faces) > 0:
        # Gerar um nome de arquivo único baseado no timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = secure_filename(f"face_detected_{timestamp}.jpg")
        file_path = os.path.join(SAVE_DIR, filename)

        # Salvar a imagem processada com as bounding boxes
        cv2.imwrite(file_path, img)
    else:
        file_path = None

    # Retornar a quantidade de faces detectadas e o caminho do arquivo salvo
    return jsonify({
        "message": "Imagem processada com sucesso",
        "faces_detected": len(faces),
        "saved_image_path": file_path
    })

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

from fastapi import FastAPI, File, UploadFile
import numpy as np
import cv2
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/process_image")
async def process_image(file: UploadFile = File(...)):
    # Verificar se o tipo de arquivo é imagem JPEG
    if file.content_type != "image/jpeg":
        return {"error": "Somente arquivos JPEG são aceitos"}
    
    # Ler o arquivo de imagem
    image_bytes = await file.read()
    image_np = np.frombuffer(image_bytes, np.uint8)
    
    # Decodificar a imagem usando OpenCV
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"error": "Falha ao processar a imagem"}

    # Carregar o classificador de face do OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar as faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Desenhar retângulos ao redor das faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Codificar a imagem de volta para JPEG
    _, img_encoded = cv2.imencode('.jpg', img)

    # Retornar a quantidade de faces detectadas e o tamanho da imagem
    return {
        "message": "Imagem processada com sucesso",
        "faces_detected": len(faces)
    }

# Para rodar o servidor, use: uvicorn main:app --reload
import paho.mqtt.client as mqtt
import time
import json
import random
from faker import Faker


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")


# Conecte ao broker
client.connect("localhost", 1891, 60)

# Função para gerar uma medição aleatória
def generate_sensor_data():
    fake = Faker()
    sensor_outputs = {
        "CO_ppm": fake.pyfloat(min_value=1, max_value=1000, right_digits=2),
        "": fake.pyfloat(min_value=0.05, max_value=10, right_digits=2),
        "NH3_ppm": fake.pyfloat(min_value=1, max_value=300, right_digits=2),
    }
    return sensor_outputs


# Loop para publicar mensagens continuamente
try:
    while True:
        data = generate_sensor_data()
        message = json.dumps(data) # Converte a medição para o formato JSON
        client.publish("test/topic", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")


client.disconnect()

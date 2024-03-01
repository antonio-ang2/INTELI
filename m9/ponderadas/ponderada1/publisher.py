import paho.mqtt.client as mqtt
import time
import json
import random
from faker import Faker

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

client.connect("localhost", 1891, 60)

def generate_data():
    fake = Faker()
    sensor_register = {
        "CO_ppm": fake.pyfloat(min_value=1, max_value=1000, right_digits=2), # Monóxido de carbono
        "NH3_ppm": fake.pyfloat(min_value=1, max_value=300, right_digits=2), # Amonia
    }
    return sensor_register


try:
    while True:
        data = generate_data()
        message = json.dumps(data)
        client.publish("test/topic", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")


client.disconnect()

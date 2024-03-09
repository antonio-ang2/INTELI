import paho.mqtt.client as mqtt
import time
import json
from faker import Faker

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

client.connect("localhost", 1891, 60)

def generate_data():
    fake = Faker()
    sensor_register = {
        "CO_ppm": fake.pyfloat(min_value=1, max_value=1000, right_digits=2),
        "NH3_ppm": fake.pyfloat(min_value=1, max_value=300, right_digits=2),
        "NO2_ppm": fake.pyfloat(min_value=0.05, max_value=10, right_digits=2),
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

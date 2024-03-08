import paho.mqtt.client as mqtt
import time
import json
import random
from faker import Faker

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

client.connect("localhost", 1891, 60)

tipo = ['freezer', 'geladeira']
loja = [1, 2, 3, 4, 5, 6]
def SensorData():
    fake = Faker()
    sensor_register = {
        "Loja": random.choice(loja),
        "tipo": random.choice(tipo),
        "temperatura": fake.pyfloat(min_value=-25, max_value=25, right_digits=2),
        "hora": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return sensor_register


try:
    while True:
        data = SensorData()
        message = json.dumps(data)
        client.publish("test/topic", message)
        print(data['temperatura'])
        if -15> float(data['temperatura']) >-25 and data['tipo'] == 'freezer':
            print("Alerta, a temperatura no freezer está muito alta")
        if 2> float(data['temperatura']) >10 and data['tipo'] == 'geladeira':
            print("Alerta, a temperatura na geladeira está muito alta")
        print(f"Publicado: {message}")


        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")


client.disconnect()

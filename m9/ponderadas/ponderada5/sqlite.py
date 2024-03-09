import sqlite3
import paho.mqtt.client as mqtt
import json

# Conectar ao banco de dados SQLite
con = sqlite3.connect("db.db")
cur = con.cursor()

# Criar a tabela se ainda não existir
cur.execute("CREATE TABLE IF NOT EXISTS CO2(value REAL, timestamp TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS NH3(value REAL, timestamp TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS NO2(value REAL, timestamp TEXT)")


# Função de callback para processar as mensagens recebidas
def on_message(client, userdata, message):
    try:
        # Decodificar a mensagem JSON
        data = json.loads(message.payload.decode("utf-8"))
        
        # Extrair o valor CO_ppm e o timestamp da mensagem
        co_ppm = data.get("CO_ppm") 
        nh3_ppm = data.get("NH3_ppm")
        no2_ppm = data.get("NO2_ppm")
        timestamp = message.timestamp
        
        # Inserir os dados no banco de dados
        cur.execute("INSERT INTO CO2 (value, timestamp) VALUES (?, ?)", (co_ppm, timestamp))
        cur.execute("INSERT INTO NH3 (value, timestamp) VALUES (?, ?)", (nh3_ppm, timestamp))
        cur.execute("INSERT INTO NO2 (value, timestamp) VALUES (?, ?)", (no2_ppm, timestamp))
        
        con.commit()
        
        print(f"Dados inseridos no banco de dados: CO_ppm = {co_ppm}, NH3_ppm = {nh3_ppm}, NO2_ppm = {no2_ppm},timestamp = {timestamp}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

# Configurar o cliente MQTT
client = mqtt.Client()
client.on_message = on_message

# Conectar ao broker MQTT e subscrever ao tópico
client.connect("localhost", 1883, 60)
client.subscribe("test/topic")

# Loop de recebimento de mensagens
client.loop_forever()

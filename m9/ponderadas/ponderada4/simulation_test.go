package main

import (
	"encoding/json"
	MQTT "github.com/eclipse/paho.mqtt.golang"
	godotenv "github.com/joho/godotenv"
	"testing"
	"time"
	"fmt"
	"os"
)

func TestConection(t *testing.T) {
	err := godotenv.Load(".env")
	if err != nil {
		fmt.Printf("Error loading .env file: %s", err)
	}
	var broker = os.Getenv("BROKER_ADDR")
	var port = 8883
	opts := MQTT.NewClientOptions().AddBroker(fmt.Sprintf("tls://%s:%d", broker, port))
	opts.SetClientID("test-client")
	opts.SetUsername(os.Getenv("HIVE_USER"))
	opts.SetPassword(os.Getenv("HIVE_PSWD"))

	client := MQTT.NewClient(opts)

	if token := client.Connect(); token.Wait() && token.Error() != nil {
		t.Errorf("Error in connection with broker MQTT: %v", token.Error())
	} else {
		t.Log("Conection with broker MQTT successful")
	}

}

// Testa validação dos dados
func TestValidationData(t *testing.T) {
	msg := MsgSender()

	// Verifique se todos os campos esperados estão presentes nos dados gerados
	expectedFields := []string{"NH3_ppm", "CO_ppm", "NO2_ppm"}
	for _, field := range expectedFields {
		if _, ok := msg[field]; !ok {
			t.Errorf("field expected: %s", field)
			return
		}
	}
	t.Log("Data validation successful.")
}

func TestPublishMessages(t *testing.T) {
	err := godotenv.Load(".env")
	if err != nil {
		fmt.Printf("Error loading .env file: %s", err)
	}
	var broker = os.Getenv("BROKER_ADDR")
	var port = 8883
	opts := MQTT.NewClientOptions().AddBroker(fmt.Sprintf("tls://%s:%d", broker, port))
	opts.SetClientID("test-client")
	opts.SetUsername(os.Getenv("HIVE_USER"))
	opts.SetPassword(os.Getenv("HIVE_PSWD"))


	client := MQTT.NewClient(opts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		t.Fatalf("Failed to connect MQTT broker: %v", token.Error())
	}

	received := make(chan bool)
	token := client.Subscribe("/pond4", 1, func(client MQTT.Client, msg MQTT.Message) {
		var data map[string]int
		if err := json.Unmarshal(msg.Payload(), &data); err != nil {
			t.Errorf("Erro ao decodificar a mensagem JSON: %v", err)
			return
		}

		expectedFields := []string{"NH3_ppm", "CO_ppm", "NO2_ppm"}
		for _, field := range expectedFields {
			if _, ok := data[field]; !ok {
				t.Errorf("Field %s expected but not received", field)
				return
			}
		}

		received <- true
	})
	if token.Wait() && token.Error() != nil {
		t.Fatalf("Failed to subscribe MQTT topic: %v", token.Error())
	}

	msg := MsgSender()
	jsonData, err := json.Marshal(msg)
	if err != nil {
		t.Fatalf("Error to convert to JSON: %v", err)
	}

	data := string(jsonData)
	token = client.Publish("/pond4", 0, false, data)
	if token.Wait() && token.Error() != nil {
		t.Fatalf("Failed to post MQTT message: %v", token.Error())
	}


	select {
	case <-received:
		t.Log("Message received successfull.")
	case <-time.After(5 * time.Second):

		t.Fatalf("Timeout: Any message was received after 5 sec.")
	}
}

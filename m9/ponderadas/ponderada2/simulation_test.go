package main

import (
	"encoding/json"
	"testing"
	"time"

	MQTT "github.com/eclipse/paho.mqtt.golang"
)

func TestConnectToBroker(t *testing.T) {
	opts := MQTT.NewClientOptions().AddBroker("tcp://localhost:1891")
	opts.SetClientID("test-client")

	client := MQTT.NewClient(opts)

	if token := client.Connect(); token.Wait() && token.Error() != nil {
		t.Errorf("Failed to connect to MQTT broker: %v", token.Error())
	} else {
		defer client.Disconnect(250)
		t.Log("Successfully connected to MQTT broker")
	}
}

func TestSensorDataValidation(t *testing.T) {
	msg := SensorData()

	expectedFields := []string{"NH3_ppm", "CO_ppm", "NO2_ppm"}
	for _, field := range expectedFields {
		if _, ok := msg[field]; !ok {
			t.Errorf("Expected field %s not found in sensor data", field)
		}
	}
	t.Log("Sensor data validation successful")
}

func TestMessageProcessing(t *testing.T) {
	opts := MQTT.NewClientOptions().AddBroker("tcp://localhost:1891")
	opts.SetClientID("test-client")

	client := MQTT.NewClient(opts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		t.Fatalf("Failed to connect to MQTT broker: %v", token.Error())
	}
	defer client.Disconnect(250)

	received := make(chan bool)
	token := client.Subscribe("/pond-2", 1, func(client MQTT.Client, msg MQTT.Message) {
		var data map[string]int
		if err := json.Unmarshal(msg.Payload(), &data); err != nil {
			t.Errorf("Error validating message: %v", err)
			return
		}

		expectedFields := []string{"NH3_ppm", "CO_ppm", "NO2_ppm"}
		for _, field := range expectedFields {
			if _, ok := data[field]; !ok {
				t.Errorf("Expected field %s not found in received message", field)
				return
			}
		}

		received <- true
	})
	if token.Wait() && token.Error() != nil {
		t.Fatalf("Failed to subscribe to MQTT topic: %v", token.Error())
	}

	msg := SensorData()
	jsonData, err := json.Marshal(msg)
	if err != nil {
		t.Fatalf("Error converting sensor data to JSON: %v", err)
	}

	data := string(jsonData)
	token = client.Publish("/pond-2", 0, false, data)
	if token.Wait() && token.Error() != nil {
		t.Fatalf("Failed to publish message: %v", token.Error())
	}

	select {
	case <-received:
		t.Log("Message received and processed successfully")
	case <-time.After(5 * time.Second):
		t.Error("Timed out waiting for message processing")
	}
}

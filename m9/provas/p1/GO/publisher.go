package main

import (
	"encoding/json"
	"flag"
	"log"
	"math/rand"
	"os"
	"os/signal"
	"syscall"
	"time"


	MQTT "github.com/eclipse/paho.mqtt.golang"
)


const (
	defaultBrokerURL = "tcp://localhost:1883"
	defaultClientID  = "publisher"
	topic            = "/pratica_p1"
)

 


func SensorData() map[string]int {
	data := map[string]int{
		
		"NH3_ppm": 
		"CO_ppm":  rand.Intn(1000),
		"NO2_ppm": rand.Intn(30),
	}
	return data
}

func Connect(brokerURL, clientID string) MQTT.Client {
	opts := MQTT.NewClientOptions().AddBroker(brokerURL)
	opts.SetClientID(clientID)

	client := MQTT.NewClient(opts)

	if token := client.Connect(); token.Wait() && token.Error() != nil {
		log.Fatalf("Error connecting to broker: %v", token.Error())
	}

	return client
}

func Publish(client MQTT.Client) {
	for {
		data := SensorData()
		jsonData, err := json.Marshal(data)
		if err != nil {
			log.Printf("Error converting data to JSON: %v", err)
			continue
		}

		msg := time.Now().Format(time.RFC3339) + " " + string(jsonData)

		token := client.Publish(topic, 1, false, msg)
		token.Wait()

		log.Printf("[PUBLISHER] %s", msg)
		time.Sleep(2 * time.Second)
	}
}

func main() {
	brokerURL := flag.String("broker", defaultBrokerURL, "MQTT broker URL")
	clientID := flag.String("clientID", defaultClientID, "Client ID")
	flag.Parse()

	client := Connect(*brokerURL, *clientID)
	defer client.Disconnect(250)

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)

	go Publish(client)

	<-quit
	log.Println("Exiting...")
}
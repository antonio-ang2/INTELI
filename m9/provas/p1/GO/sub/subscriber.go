package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	MQTT "github.com/eclipse/paho.mqtt.golang"
)

var (
	brokerURL  = flag.String("broker", "tcp://localhost:1883", "MQTT broker URL")
	clientID   = flag.String("clientID", "subscriber", "Client ID")
	topic      = "/pratica_p1"
	qos        = 1
	messagePubHandler MQTT.MessageHandler = func(client MQTT.Client, msg MQTT.Message) {
		fmt.Printf("Received: %s from: %s\n", msg.Payload(), msg.Topic())
	}
)

func Connect(brokerURL, clientID string) MQTT.Client {
	opts := MQTT.NewClientOptions().AddBroker(brokerURL)
	opts.SetClientID(clientID)
	opts.SetDefaultPublishHandler(messagePubHandler)

	client := MQTT.NewClient(opts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		log.Fatalf("Error connecting to broker: %v", token.Error())
	}
	return client
}

func Subscribe(client MQTT.Client, topic string, qos byte) {
	if token := client.Subscribe(topic, qos, nil); token.Wait() && token.Error() != nil {
		log.Fatalf("Error subscribing to topic %s: %v", topic, token.Error())
	}
}

func main() {
	flag.Parse()

	client := Connect(*brokerURL, *clientID)
	defer client.Disconnect(250)

	Subscribe(client, topic, byte(qos))

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)

	<-quit
	log.Println("Exiting...")
}

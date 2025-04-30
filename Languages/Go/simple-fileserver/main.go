package main

import (
	"fmt"
	"log"
	"net"
)

func handleRequest(connection net.Conn) {
	defer connection.Close()

	// Read incomming request
	requestBuffer := make([]byte, 4096)

	_, err := connection.Read(requestBuffer)

	if err != nil {
		log.Fatalf("Failed with error: %v", err)
	}

	// request := parseRequest(requestBuffer)

	// fmt.Printf("Request recieved: \n%v", request)

	// Generate Response

	// response := generateResponse(request)
	// fmt.Printf("Response Generated: \n%v", response)

	// connection.Write([]byte(response.String()))
}

func main() {
	// Primary entrypoint
	listener, err := net.Listen("tcp", ":8118")
	fmt.Printf("Listening on %v\n\n", listener.Addr())

	if err != nil {
		log.Fatalf("Failed with error: %v", err)
	}

	defer listener.Close() // Ensure socket closes properly

	for {
		connection, err := listener.Accept()
		if err != nil {
			log.Printf("Error: %v", err)
		}
		go handleRequest(connection)
	}

}

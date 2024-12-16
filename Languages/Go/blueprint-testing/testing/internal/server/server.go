package server

import (
	"github.com/gofiber/fiber/v2"

	"testing/internal/database"
)

type FiberServer struct {
	*fiber.App

	db database.Service
}

func New() *FiberServer {
	server := &FiberServer{
		App: fiber.New(fiber.Config{
			ServerHeader: "testing",
			AppName:      "testing",
		}),

		db: database.New(),
	}

	return server
}

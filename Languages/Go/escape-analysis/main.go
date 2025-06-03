package main

type System struct {
	label    string
	owner    string
	hostname string
}

func InitializeSystemDefaults() System {
	return System{
		label:    "System-Service",
		owner:    "John Doe",
		hostname: "localhost",
	}
}

func main() {
	v := InitializeSystemDefaults()
	_ = v
}

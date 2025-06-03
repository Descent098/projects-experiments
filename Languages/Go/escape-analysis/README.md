# Escape Analysis

Escape Analysis is a method for determining if values in your code are allocated on the stack or the heap.

`go run -gcflags '-m -l' <file>.go`

## Test Case

I wanted to see what's the best option for initializing a struct with default values, and keeping it on the heap. Here is the struct I'm testing with:

```go 
type System struct {
	label    string
	owner    string
	hostname string
}
```


### Case 1

```go
func (sys *System) InitializeDefaults() {
	sys.label = "System-Service"
	sys.owner = "John Doe"
	sys.hostname = "localhost"
}

func main() {
	v := System{}
	v.InitializeDefaults()
	fmt.Println(v)
}
```

```bash
go run -gcflags "-m -l" main.go
# command-line-arguments
./main.go:11:7: sys does not escape
./main.go:21:13: ... argument does not escape
./main.go:21:14: v escapes to heap
{System-Service John Doe localhost}
```

### Case 2

```go
func InitializeDefaults() System {
	return System{
		label:    "System-Service",
		owner:    "John Doe",
		hostname: "localhost",
	}
}

func main() {
	v := InitializeDefaults()
	fmt.Println(v)
}
```

```bash
go run -gcflags "-m -l" main.go
# command-line-arguments
./main.go:25:13: ... argument does not escape
./main.go:25:14: v escapes to heap
{System-Service John Doe localhost}
```

### Case 3


```go
func InitializeDefaults() *System {
	return &System{
		label:    "System-Service",
		owner:    "John Doe",
		hostname: "localhost",
	}
}

func main() {
	v := InitializeDefaults()
	fmt.Println(v)
}
```

```bash
go run -gcflags "-m -l" main.go
# command-line-arguments
./main.go:16:9: &System{...} escapes to heap
./main.go:25:13: ... argument does not escape
&{System-Service John Doe localhost}
```

### Case 4

```go
func (sys System) InitializeDefaults() System {
	return System{
		label:    "System-Service",
		owner:    "John Doe",
		hostname: "localhost",
	}
}

func main() {
	v := System{}.InitializeDefaults()
	fmt.Println(v)
}
```

```bash
go run -gcflags "-m -l" main.go
# command-line-arguments
./main.go:11:7: sys does not escape
./main.go:22:13: ... argument does not escape
./main.go:22:14: v escapes to heap
{System-Service John Doe localhost}
```

### Case 5

After a bunch of testing I realized it was the call to `fmt.Println()` that was causing the escape, so this code does not escape:

```go
func (sys System) InitializeDefaults() System {

	return System{
		label:    "System-Service",
		owner:    "John Doe",
		hostname: "localhost",
	}
}

func main() {
	v := System{}.InitializeDefaults()
	_ = v
}
```

```bash
go run -gcflags "-m -l" main.go
# command-line-arguments
./main.go:9:7: sys does not escape
```

### Case 6

```go
func (sys *System) InitializeDefaults() {
	sys.label = "System-Service"
	sys.owner = "John Doe"
	sys.hostname = "localhost"
}

func main() {
	v := System{}
	v.InitializeDefaults()
	_ = v
}
```


```bash
go run -gcflags "-m -l" main.go
# command-line-arguments
./main.go:9:7: sys does not escape
```


## References

- https://medium.com/eureka-engineering/understanding-allocations-in-go-stack-heap-memory-9a2631b5035d
- https://stackoverflow.com/questions/72245044/initializing-objects-in-golang-heap-stack-does-that-concept-exist
- https://stackoverflow.com/questions/22088754/using-new-vs-when-initializing-a-struct-in-go/22089544#22089544

# Golang Testing

Some testing (hah) of the golang builtin [testing package](https://pkg.go.dev/testing).

## Testing Types

Go packages tests
- [`*testing.T`](https://pkg.go.dev/testing#T): For regular testing
  - Prefix functions with `Test_<testname>`
- [`*testing.F`](https://pkg.go.dev/testing#F): For fuzzing
  - Prefix functions with `Fuzz_<testname>`
  - Pass `-fuzz <testname>` to make it run
- [`*testing.B`](https://pkg.go.dev/testing#B): For benchmarks
  - Prefix functions with `Benchmark_<testname>`
  - Pass `-bench` to make benchmarks run
  - Pass `-cpu` to run in parallel (i.e. using [`b.RunParallel()`](https://pkg.go.dev/testing#hdr-Fuzzing:~:text=func%20BenchmarkTemplateParallel(b%20*testing.B)%20%7B%0A%20%20%20%20templ%20%3A%3D%20template.Must(template.New(%22test%22).Parse(%22Hello%2C%20%7B%7B.%7D%7D!%22))%0A%20%20%20%20b.RunParallel(func(pb%20*testing.PB)%20%7B%0A%20%20%20%20%20%20%20%20var%20buf%20bytes.Buffer%0A%20%20%20%20%20%20%20%20for%20pb.Next()%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20buf.Reset()%0A%20%20%20%20%20%20%20%20%20%20%20%20templ.Execute(%26buf%2C%20%22World%22)%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D)%0A%7D))

Essentially the types become a `stdout`, `stderr` replacement, as well as modifying the runtime based on what's passed. For each you need certail flags to be passed

package api

import "testing"

func Benchmark_slowFunc(benchmarkState *testing.B) {
	benchmarkState.RunParallel(func(parallelBenchmarkState *testing.PB) {
		for parallelBenchmarkState.Next() {
			slowFunc()
		}
	})
}

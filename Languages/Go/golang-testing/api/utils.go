package api

import (
	"fmt"
	"math/rand"
	"os"
	"text/tabwriter"
	"time"
)

func slowFunc() {
	// From https://pkg.go.dev/math/rand#example-package-Rand
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	w := tabwriter.NewWriter(os.Stdout, 1, 1, 1, ' ', 0)
	defer w.Flush()
	show := func(name string, v1, v2, v3 any) {
		fmt.Fprintf(w, "%s\t%v\t%v\t%v\n", name, v1, v2, v3)
	}
	sleepTime := time.Duration(r.Intn(15)) * time.Second
	time.Sleep(sleepTime)
	// Float32 and Float64 values are in [0, 1).
	show("Float32", r.Float32(), r.Float32(), r.Float32())
	show("Float64", r.Float64(), r.Float64(), r.Float64())
}

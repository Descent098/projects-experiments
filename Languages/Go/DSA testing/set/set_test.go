package set_test

import (
	"dsa/set"
	"testing"
)

func TestBasics(t *testing.T) {
	a := make(set.Set[string])
	b := make(set.Set[int])
	c := make(set.Set[float32])

	a.Add("kieran")
	b.Add(1)
	c.Add(1.5)

	if !a.Contains("kieran") {
		t.Fatalf("Kieran not in set")
	}
	if a.Contains("Wali") {
		t.Fatalf("Wali in set when not added")
	}
	if !b.Contains(1) {
		t.Fatalf("1 not in set")
	}
	if b.Contains(5) {
		t.Fatalf("5 in set when it wasn't added")
	}
	if !c.Contains(1.5) {
		t.Fatalf("1.5 not in set")
	}
	if c.Contains(3.5) {
		t.Fatalf("3.5 in set when it was not added")
	}

}

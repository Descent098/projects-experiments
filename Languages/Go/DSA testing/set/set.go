// Implementing a set without any memory allocations.
// Because empty structs point to zerobase, they are free to use without memory being instantiated
//
// SEE: https://leapcell.io/blog/infinite-uses-of-go-empty-struct
package set

// The set allows for any type of comparable to be mapped to a struct (or zerobase)
type Set[k comparable] map[k]struct{}

// Allows you to add a value to a struct
func (s Set[k]) Add(value k) {
	s[value] = struct{}{}
}

func (s Set[K]) Remove(val K) {
	delete(s, val)
}

func (s Set[k]) Contains(value k) bool {
	_, ok := s[value] // False when nil, True when empty
	return ok
}

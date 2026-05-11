package formats

type whitespaceoptions rune

const (
	// blanks whitespaceoptions = rune("") // TODO: How to implement this?
	commentIndicator                   = '#'
	TABS             whitespaceoptions = '\t'
	CR               whitespaceoptions = '\r'
	LF               whitespaceoptions = '\n'
)

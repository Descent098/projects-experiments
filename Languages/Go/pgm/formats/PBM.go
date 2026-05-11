package formats

const (
	pbmMagicNumber      = "P4"
	plainPBMMagicNumber = "P1"
)

type PBMFile struct {
	MaxVal uint16 // TODO: must be greater than 0
	Plain  bool
}

// `
// <magicNumber>

// <width> <height>
// <content>
// `

func (instance *PBMFile) WriteFile(path string) error {

	return nil
}

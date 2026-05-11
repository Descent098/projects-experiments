package formats

const pgmMagicNumber = "P5"

type PGMFile struct {
	MaxVal uint16 // TODO: must be greater than 0

}

func (instance *PGMFile) WriteFile(path string) error {

	return nil
}

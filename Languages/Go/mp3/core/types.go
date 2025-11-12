package core

type MIMEType = string  // A valid MIME Type as a string (i.e. "image/png" )
type Base64Str = string // A base64 encoded string (data URI) of an image in the format "data:<MIME TYPE>;base64,<DATA>"

type Album struct {
	Name   string    `json:"name"`
	Cover  Base64Str `json:"image"` // Base64 encoded data URI of the album image
	Year   int       `json:"year"`
	Tracks []Song    `json:"tracks"`
	Artist string    `json:"artist"`
}

type Song struct {
	Title       string `json:"title"`
	Album       Album  `json:"album"`
	Artist      string `json:"artist"`
	TrackNumber int    `json:"trackNumber"`
	Filename    string `json:"filename"`
}

type MusicProvider interface {
	GetAlbums() []Album
	GetSongs() []Song
	Search(query string) []Song
	Connect() error // Ensure a connection can be established to the Provider
}

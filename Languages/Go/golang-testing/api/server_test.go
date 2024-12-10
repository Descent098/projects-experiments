package api

import (
	"fmt"
	"net/http"
	"net/url"
	"reflect"
	"testing"
)

func Fuzz_contact(testingState *testing.F) {
	for _, seed := range []string{"kieran", "adam", "^&*%#&*^"} {
		testingState.Add(seed)
	}
	testingState.Fuzz(func(t *testing.T, provided_name string) {
		t.Run(fmt.Sprintf("Fuzzy testing %s", provided_name),
			func(t *testing.T) {
				url, err := url.Parse(fmt.Sprintf("https://example.com/contact?name=%s", provided_name))
				if err != nil {
					t.Errorf("Unable to parse URL")
				}
				contact(nil, &http.Request{URL: url})
			},
		)

	})
}

func Test_contact(testingState *testing.T) {
	url, err := url.Parse("https://example.com/contact?name=kieran")
	if err != nil {
		testingState.Errorf("Unable to parse URL")
	}
	type args struct {
		writer  http.ResponseWriter
		request *http.Request
	}
	tests := []struct {
		name string
		args args
	}{
		{name: "INIT", args: args{writer: nil, request: &http.Request{URL: url}}},
	}
	for _, tt := range tests {
		testingState.Run(tt.name, func(t *testing.T) {
			contact(tt.args.writer, tt.args.request)
		})
	}
}

func Fuzz_weather(testingState *testing.F) {
	for _, seed := range []string{"/edmonton", "/Amsterdam"} {
		testingState.Add(seed)
	}
	testingState.Fuzz(func(subtestState *testing.T, provided_city string) {
		subtestState.Run(fmt.Sprintf("Fuzzy testing %s", provided_city),
			func(t *testing.T) {
				url, err := url.Parse(fmt.Sprintf("https://example.com/weather/%s", provided_city))
				if err != nil {
					t.Errorf("Unable to parse URL")
				}
				weather(nil, &http.Request{URL: url})
			},
		)

	})
}

func Test_weather(testingState *testing.T) {
	url, err := url.Parse("https://example.com/weather/calgary")
	if err != nil {
		testingState.Errorf("Unable to parse URL")
	}
	type args struct {
		writer  http.ResponseWriter
		request *http.Request
	}
	tests := []struct {
		name string
		args args
	}{
		{name: "INIT", args: args{writer: nil, request: &http.Request{URL: url}}},
	}
	for _, tt := range tests {
		testingState.Run(tt.name, func(t *testing.T) {
			weather(tt.args.writer, tt.args.request)
		})
	}
}

func TestSetupServer(testingState *testing.T) {

	tests := []struct {
		name string
		want *http.ServeMux
	}{
		// Always fails because the initial
		{name: "init", want: &http.ServeMux{}},
	}
	for _, tt := range tests {
		testingState.Run(tt.name, func(t *testing.T) {
			if got := SetupServer(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("SetupServer() = %v, want %v", got, tt.want)
			}
		})
	}
}

# Running

<details><summary>Linux/Mac</summary>

`go build -buildmode=c-shared -o lib.so lib.go && python3 testing.py`

</details>

<details><summary>Windows</summary>

`go build -buildmode=c-shared -o lib.dll lib.go`

`python testing.py`


</details>


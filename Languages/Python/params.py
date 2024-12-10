from flask import Flask, request

app = Flask(__name__)

# Query params
@app.route("/contact")
def contact():
	request_params = request.args
	name = request_params.get("name")
	age = request_params.get("age")

# Path params
@app.route("/weather/<city>")
def weather(city):
	return f"<h1>Your city is {city}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
app = Flask(__name__)

user = {"name": "Kieran",
        "age": 24}

@app.route('/')
def hello():
    return render_template("index.jinja", user=user)

@app.route('/post')
def sadkjfgh():
    return '<h1>This is a post</h1>'

@app.route('/weather/<city>')
def print_weather(city):
    return render_template("weather.jinja", city=city)

@app.route('/form_submit', methods=['POST'])
def method_name():
    if request.form:
        print(request.form)
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)


@app.route('/admin/')
def q():
    return 'pyth admin'

@app.route('/admin/login')
def z():
    return 'pyth admin login'

@app.route('/')
def hello():
    return 'pyth World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5787)
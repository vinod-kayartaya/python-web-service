# this is the entirypoint for the project

from flask import Flask

app = Flask()

@app.route('/')
def index():
    return '<h1>Hello, world</h1>'


@app.route('/hello')
def hello():
    return '<h1>Hello</h1>';


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask
from py.webapp import app as web_app
from py.middlewareService import app as api_app
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, this is the root!"

if __name__ == '__main__':
    serve(
        {
            '/': app,
            '/web': web_app,
            '/api': api_app
        },
        port=8080
    )

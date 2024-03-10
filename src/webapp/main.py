from flask import Flask
from py.webapp import app as web_app
from py.middlewareService import app as api_app

if __name__ == '__main__':
    # Start the web application
    web_app.run(debug=True, port=8080)

    # Start the API service
    # Note: This code will only execute after the web application has stopped
    api_app.run(debug=True, port=8080)

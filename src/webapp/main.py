from flask import Flask
from py.webapp import app as web_app  # Adjust the import path
from py.middlewareService import app as api_app  # Adjust the import path
import threading

if __name__ == '__main__':
    # Start the web application
    web_thread = threading.Thread(target=web_app.run, kwargs={'debug': True, 'port': 8080, 'use_reloader': False})
    web_thread.daemon = True  # Set the thread as a daemon
    web_thread.start()

    # Start the API service
    api_app.run(debug=True, port=8080)

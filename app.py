from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # We include the hostname to prove it's running inside a container
    hostname = socket.gethostname()
    return f"<h1>Hello from Docker!</h1><p>Running on host: {hostname}</p><p>System: {os.uname().sysname}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import os
import socket

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # hostname = socket.gethostbyaddr(request.remote_addr)
    hostname = socket.gethostname()
    # print(hostname)
    # print(request.remote_addr)
    # return request.remote_addr
    #return 'Hello World!'
    return hostname

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
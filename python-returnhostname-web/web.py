import os
import sys
import requests
import socket
from flask import Flask
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

@app.route('/')
def index():
    webapiHostName = get_webapi_hostname()
    hostName = get_hostname()

    return 'My hostname... "{0}" Webapi hostname:... "{1}"'.format(hostName, webapiHostName)

def get_hostname():
    return socket.gethostname();

def get_webapi_hostname():
    # the web container MUST be run with --link <appName>:helloapp
    # link_alias = 'helloapp'

    # Load the environment variables from the .env file.  
    # They will be overwritten if environment vars are set
    load_dotenv(find_dotenv())
    url = os.environ.get("APPURL")

    # Request data from the app container
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
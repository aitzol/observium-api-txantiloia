import json
import telegram
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def notifikazioa():
    data = json.loads(request.data)

    return "", 204
 
app.run(host='0.0.0.0')
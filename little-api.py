import os
import urllib, json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/objects/<object_id>')
def show_object(object_id):

    path = id2path(object_id)

    url = 'https://rawgit.com/cooperhewitt/collection/master/objects/' + path + '/' + object_id + '.json'
    response = urllib.urlopen(url)

    data = response.read()

    return data    

def id2path(id):

    tmp = str(id)

    parts = []

    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]
        
    if len(tmp):
        parts.append(tmp)
    
    return os.path.join(*parts)

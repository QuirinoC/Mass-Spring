'''
export FLASK_APP=server.py
flask run
'''

from flask import Flask, jsonify, make_response, request, render_template, Response
from LU import LU
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET',"POST"])
def root():
    req       = request.json
    res       = {}
    if (req == None): req = request.form 
    #if 'm' in req and 'b' in req:
    #    return ""
    try:
        m = req['m']
        b = req['b']
        result = LU(m,b)
    except:
        result = {"err":"Invalid request"}

    return jsonify(result)

app.run(host="0.0.0.0", port= os.getenv("PORT", "5000"))
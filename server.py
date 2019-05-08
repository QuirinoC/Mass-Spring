'''
export FLASK_APP=server.py
flask run
'''

from flask import Flask, jsonify, make_response, request, render_template, Response
from LU import LU
app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def root():
    req       = request.json
    res       = {}
    if (req == None): req = request.form
    m = req['m']
    b = req['b']
    result = LU(m,b)
    return jsonify(result)

    
import os
import signal
from flask import Flask, url_for, render_template

from flask import jsonify
import requests
import simplejson
import json
from flask import jsonify
#from buzz import generator
from  patientSimBin import patient
import logging

import random

app = Flask(__name__)
app.debug = False

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def info():
    page = '<html><body><h1>'
    page += "PatientSim Version 1 : Contact - sgyoung@us.ibm.com"
    page += '</h1></body></html>'

    return page

@app.route("/api/getPatientData/<patientName>")
def getPatientData(patientName):

    heartrate = random.randint(60,150)

    data = {}
    data['name'] = patientName
    data['heartrate'] = heartrate
    data['ecgData'] = patient.ecg(heartrate).tolist()

    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

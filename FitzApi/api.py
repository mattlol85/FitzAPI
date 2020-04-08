import flask
from flask import request, jsonify
import os
import sys
from datetime import time
from datetime import datetime
import sqlite3
from sqlite3 import Error

import random
import math

app = flask.Flask(__name__)
app.config[ "DEBUG" ] = True

conn = sqlite3.connect('testDb.db')
# Create Brothers table
#c.execute('''CREATE TABLE BROTHERS ([generated_id] INTEGER PRIMARY KEY, [Client_Name] text,[Country_ID] integer, [Date] date)''')
conn.commit()
@app.route('/', methods=['GET'])
def home():
    return "<h1>Fitz API TESTING</h1><p>FITZ API test. Is this thing on??.</p>"



# Test Data
Brothers = [
   { 'id': 0,
    'name': 'Matthew',
    "age": 22},
    { 'id': 1,
    'name': 'Joey',
    "age": 20}
]
# All Brothers
@app.route('/api/v1/resources/brothers/all', methods=['GET'])
def api_all():
    return jsonify(Brothers)

#Brother by ID
@app.route('/api/v1/resources/brothers', methods=['GET'])
def api_id():
    # Check if an ID was given as part of the URL
    # If ID is provided, assign it a variable.
    # If no ID is provided, display an error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No ID field profided. Please specify an id."
    
    results = []

    # Loop through the data and match the ID
    # All ID's are unique, other fields not so much

    for brother in Brothers:
        if brother['id'] == id:
            results.append(brother)

    # Pretty print with Jsonify
    return jsonify(results)


# Add New Brother
@app.route('/api/v1/resources/brothers', methods=['POST'])
def api_new_brother():
    conn = sqlite3.connect('testDb.db')
    c = conn.cursor()
    print(str(request.get_json()))
    name = request.get_json('name')
    age = request.get_json('age')
    #randNum  = math.ceil(float(random.randint(3, 9999)))
    c.execute("INSERT INTO Brothers VALUES (?,?,?)", (3,name, age))
    c.commit()
    conn.close()

# Return current time according to this computer
@app.route('/api/v1/resources/time', methods=['GET'])
def api_time():
    return {'time' : datetime.now()}




## Database Interaction Methods

def connect_toDB():
    print()

app.run()
from flask import Flask, request,jsonify

from common.db import Database
import json
app = Flask(__name__)

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/main', methods=['POST', 'GET'])
def home():
    # data=request.get_json()
    name = request.form['name']
    temp = request.form['temp']

    Database.insert(collection='sensors',data={'name':name, 'temp':temp})
    #display_data(name)

    l=Database.find(collection='sensors', query='all')
    d=[]
    for item in l:
        d.append({'name':item['name'],'temp':item['temp']} )
    return jsonify(d=d)

@app.route('/graph', methods=[ 'GET'])
def send_graph_data():


    l=Database.find(collection='sensors', query='all')
    d=[]
    for item in l:
        d.append({'name':item['name'],'temp':item['temp']} )
    return jsonify(d=d)



def display_data(name):
    print(Database.DATABASE['sensors'].find({'name': name}))

if __name__ == '__main__':
    app.run(port=5002, debug=True)

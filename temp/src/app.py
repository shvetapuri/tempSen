from flask import Flask, render_template, request

import requests
import json

app = Flask(__name__)


@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def send_results():


    #name= request.form.get("name")
    #temp= request.form['temp']
    data = request.get_json(force=True)

    r = requests.post("http://127.0.0.1:5002/main", data)

    #print(name, temp);

    #r = requests.post("http://127.0.0.1:5002/main", data={'name':name})

    #data = request.get_json()
    #print('here is',data)
    # print ("hi", r.headers['Content-Type'])


    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

import requests
from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html')

@app.route('/about')
def about():    
    return render_template('about.html')

@app.route('/transportasi', methods=['GET'])
def transportasi():
    asalkota = request.args.get('asal')
    tujuankota = request.args.get('tujuan')
    
    kota = requests.get('https://tst-adit.herokuapp.com/kota/' + asalkota)
    transport = requests.get('https://tstfarabi.herokuapp.com/' + asalkota + '/' + tujuankota)

    data = json.loads(kota.text)
    dataa = json.loads(transport.text)

    return render_template('transportasi.html', dataa = dataa, data = data)
# city = requests.get('http://localhost:5010/kota/' + 'bandung').json()
    # transport = requests.get('http://localhost:5020/sekalitrip/' + 'jakarta' + '/' + 'bandung').json()
    # data = []
    # data.append(city)
    # data.append(transport)

if __name__ == '__main__':
	app.run(debug = True)
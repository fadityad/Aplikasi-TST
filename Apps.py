import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # city = requests.get('http://localhost:5010/kota/' + 'bandung').json()
    # transport = requests.get('http://localhost:5020/sekalitrip/' + 'jakarta' + '/' + 'bandung').json()
    # data = []
    # data.append(city)
    # data.append(transport)
    # return render_template('home.html', data = data)

@app.route('/kota/<city>', methods=['GET'])
def kota(city):
    kota = requests.get('http://localhost:5010/kota/' + city)
    data = []
    data.append(kota)
    return render_template('page.html', data = data)

@app.route('/<asal>/<tujuan>')
def info_transport(asal, tujuan):
    transport = requests.get('http://localhost:5020/sekalitrip/' + asal + '/' + tujuan)
    return transport

if __name__ == '__main__':
	app.run(debug = True)
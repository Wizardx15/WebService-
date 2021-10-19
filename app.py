from flask import Flask, render_template, url_for, redirect, request
import requests
import json
from werkzeug.utils import html
from monad import *
# memanggil library flask tersebut agar dikenali sistem
app = Flask(__name__, template_folder='templates')
#app nama file

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/wsgi")
#link/url utama saat pertama akses
def wsgi():
    return render_template('wsgi.html')

@app.route("/nasional")
def nasional():
        data = requests.get('https://api.kawalcorona.com/indonesia/')
        covid = data.json()
        return render_template('index.html', covid=covid)

@app.route("/Prov")
def prov():
    data1 = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    prov = data1.json()
    return render_template('Prov.html', len=len(prov), prov=prov)
@app.route("/rs")
def rs():
    data2 = requests.get('https://dekontaminasi.com/api/id/covid19/hospitals')
    rs = data2.json()
    return render_template('RS.html', len=len(rs), rs=rs)

@app.route('/monad', methods=['POST','GET'])
def monad():
    if request.method=='POST':
        bil1=request.form['bil1']
        bil2=request.form['bil2']
        pilihan=request.form['pilihan']
        if pilihan=='penjumlahan':
            opsi=penjumlahan(int(bil1), int(bil2))
        elif pilihan == 'pengurangan':
            opsi=pengurangan(int(bil1),int(bil2))
        elif pilihan == 'perkalian':
            opsi=perkalian(int(bil1),int(bil2))
        elif pilihan == 'pembagian':
            opsi=pembagian(int(bil1),int(bil2))
        elif pilihan == 'add_1':
            opsi=add_1(int(bil1))
        elif pilihan == 'mul_3':
            opsi=mul_3(int(bil1))
        return render_template('monad.html', opsi=opsi)
    else:
        return render_template('monad.html')


if __name__=="__main__":
    app.run(debug=True)
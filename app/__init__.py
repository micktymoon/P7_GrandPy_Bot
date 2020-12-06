from flask import Flask
from flask import render_template, request, json
from app.parser.parser import parser, recup_latlong

app = Flask(__name__)

# from app import routes


@app.route('/accueil')
def accueil():
    return render_template('accueil.html', title='Accueil')


@app.route('/getCoords')
def get_coords():
    return render_template('coord.html')


@app.route('/Coord', methods=['POST'])
def coord():
    quest = request.form['question']
    lieu = parser(quest)
    lat_lng = recup_latlong(lieu)
    return lat_lng



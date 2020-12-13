from flask import Flask
from flask import render_template, request
from app.parser.parser import parser
from app.maps.maps_api import recup_latlong
from app.wikipedia.wiki_api import get_pageid, get_history
import json
app = Flask(__name__)


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
    lat = json.dumps(lat_lng['lat'])
    lng = json.dumps(lat_lng['lng'])
    page_id = get_pageid(lat, lng)
    history = get_history(page_id)
    return {'location': lat_lng, 'history': history}


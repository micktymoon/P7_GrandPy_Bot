#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template, request
from app.parser.parser import parser
from app.maps.maps_api import get_location
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
    latlng_and_address = get_location(lieu)
    address = latlng_and_address['address']
    lat_lng = latlng_and_address['location']
    lat = json.dumps(lat_lng['lat'])
    lng = json.dumps(lat_lng['lng'])
    page_id = get_pageid(lat, lng)
    history = get_history(page_id)
    return {'place': lieu, 'latlng': lat_lng, 'history': history, 'address': address}



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


@app.route('/Coord', methods=['POST'])
def coord():
    quest = request.form['question']
    place = parser(quest)
    if place is not False:
        latlng_and_address = get_location(place)
        if latlng_and_address is not False:
            address = latlng_and_address['address']
            lat_lng = latlng_and_address['location']
            lat = json.dumps(lat_lng['lat'])
            lng = json.dumps(lat_lng['lng'])
            page_id = get_pageid(lat, lng)
            if page_id is not False:
                history = get_history(page_id)
                if history is not False:
                    return {
                        "place": place,
                        "latlng": lat_lng,
                        "history": history,
                        "address": address}
                else:
                    return {
                        "error": "no history",
                        "place": place,
                        "latlng": lat_lng,
                        "address": address}
            else:
                return {
                    "error": "no pageid",
                    "place": place,
                    "latlng": lat_lng,
                    "address": address}
        else:
            return {
                "error": "no lat-lng",
                "place": place}
    else:
        return {"error": "no place"}

#/usr/bin/env python
# -*- coding:utf-8 -*-

# from flask import Flask, render_template, request, json
# from app.parser.parser import parser, recup_latlong
# from app import app
#
# app = Flask(__name__)
#
#
# @app.route('/accueil')
# def accueil():
#     return render_template('accueil.html', title='Accueil')
#
#
# @app.route('/getCoords')
# def get_coords():
#     return render_template('coord.html')
#
#
# @app.route('/Coord', methods=['POST'])
# def coord():
#     quest = request.form['question']
#     lieu = parser(quest)
#     lat_lng = recup_latlong(lieu)
#     return json.dumps({'status': 'OK', 'question': quest, 'lieu': lieu, "lat-lng": lat_lng})



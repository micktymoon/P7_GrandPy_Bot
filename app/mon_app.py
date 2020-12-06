#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, json
from app.parser import parser, recup_latlong


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
	a = "blabla"
	return json.dumps({'status': 'OK', 'question': quest, 'test': a})


if __name__ == '__main__':
	app.run()

# endroit = parser("Donne moi l'adresse de OpenClassRooms.")
# print(endroit)
# lat_long = recup_latlong(endroit)
# print(lat_long)
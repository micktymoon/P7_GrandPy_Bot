#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, json



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
	return json.dumps({'status': 'OK', 'question': quest})


if __name__ == '__main__':
	app.run()

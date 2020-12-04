#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def accueil():
	return render_template('accueil.html', title='Accueil')

@app.route('/getCoolds')
def get_coords():
	return '{ "lat": 48.8975156, "lng": 2.3833993 }'


if __name__ == '__main__':
	app.run()

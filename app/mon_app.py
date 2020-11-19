#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def accueil():
	return render_template('accueil.html', title='Accueil')

if __name__ == '__main__':
	app.run()

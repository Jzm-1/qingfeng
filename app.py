from flask import Flask, render_template
from sqlalchemy import db


app = Flask(__name__)

@app.route("/")
def index():
	return render_template('zuhao.html')

@app.route('/wzry')
def wzry():
	data = db.fetchall(sql='select * from wzry')
	return render_template('wzry.html',data=data)

@app.route('/hpjy')
def hpjy():
	data = db.fetchall(sql='select * from hpjy')
	return render_template('hpjy.html',data=data)

@app.route('/cyhx')
def cyhx():
	data = db.fetchall(sql='select * from cyhx')
	return render_template('cyhx.html',data=data)

if __name__ == "__main__":
	app.run()
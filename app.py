from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

@app.route('/datetime')
def sysdatetime():
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y %H:%M")
	templateData = {
		'title' : 'Hello!!'
	,	'time'  : timeString
	}
	return render_template('datetime.html', **templateData)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
	return 'This is the homepage'


@app.route('/tuna')
def tuna():
	return '<img src="/static/smalldiccnicc.png" width=15%/>'




if __name__ == "__main__":
	app.run(debug=True)
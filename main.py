import os
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from scraper import *
from jinja2 import *
from lxml import html
import urllib2
import requests
import json
import datetime
import webbrowser


app = Flask(__name__)

error = 'none'

@app.route('/', methods=['GET', 'POST'])
def index():
    render_template('index.html')

    # If request is posted
    if request.method == 'POST':
        # Take in the input
        data=request.form['IO']
        return scrape(data)

    # Render template while waiting for response
    return render_template('index.html')

def scrape(data):
    clear_GIFS_directory()
    terms = parse_input(data)
    gifs = generate_gifs(terms)
    app.jinja_env.globals.update(gif_list = gifs)
    return render_template('output.html')

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
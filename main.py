from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/where problem')
def index_one():
    return render_template('statia.html')

app.run(debug=True)
from flask import Flask, url_for, redirect, jsonify
import json, os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('hot'))


@app.route('/hot/<file_name>')
def hot_static(file_name):
    return redirect(url_for('static', filename=f'{file_name}'))


@app.route('/hot/')
def hot():
    return jsonify([e for e in os.listdir("static") if e.endswith('.json')])

@app.route('/girls/<file_name>')
def girls_static(file_name):
    return redirect(url_for('static', filename=f'{file_name}'))
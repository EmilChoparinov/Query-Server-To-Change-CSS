from flask import Flask, render_template, request

server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html', red='255', green='255', blue='255')

@server.route('/changeColor', methods=['POST'])
def process():
    return render_template('index.html', red=request.form['red'], green=request.form['green'], blue=request.form['blue'])

server.run(debug=True)
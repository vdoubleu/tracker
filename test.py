# flask app
import os
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

@app.route('/data')
def headers():
    headers = jsonify(dict(request.headers))
    print(request.environ)
    # redirect to google
    return "non";

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

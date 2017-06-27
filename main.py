from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)


@app.route('/')
def index():
    pass

if __name__ == '__main__':
    app.run(debug=True)
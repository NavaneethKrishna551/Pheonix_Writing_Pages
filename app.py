from flask import Flask, request, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_FILE = os.path.join(BASE_DIR, "whosaidhi.txt")

@app.route("/")
def home():
    return render_template("index.html")

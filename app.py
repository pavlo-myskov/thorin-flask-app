import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    with open('data/company.json', "+r", encoding="UTF-8") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact.html")
def contact():
    return render_template("contact.html", page_title="Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Come Work With Us")

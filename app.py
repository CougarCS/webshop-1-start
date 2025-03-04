from flask import Flask, render_template
import requests

app = Flask(__name__)

name = "cody cougar"
uh_id = 0000000


@app.route("/")
def index():
    facts = [
        "I have visited over 4 cities",
        "I got ran over by a Google employee",
        "I run 3 small Etsy stores",
        "I love to bake",
        "My dog is named Moose",
    ]

    return render_template("index.html", student_name=name, facts=facts)


@app.route("/dogs")
def dogs():
    # dog api link: https://dog.ceo/api/breeds/image/random

    return render_template("dogs.html")


if __name__ == "__main__":
    app.run(debug=True)

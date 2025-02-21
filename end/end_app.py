from flask import Flask, render_template
import requests

app = Flask(__name__)

name = "cody cougar"
uh_id = 2135381

@app.route("/")
def index():
    facts = [
        "I have visited over 10 countries",
        "I got ran over by a Google employee",
        "I run 3 small Etsy stores",
        "I love to bake",
        "My dog is named Moose",
    ]

    return render_template("index.html", student_name=name, facts=facts)

@app.route("/dogs")
def dogs():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    dog_url = response.json()["message"]
    return render_template("dogs.html", student_name=name, dog_url=dog_url)


if __name__ == "__main__":
    app.run(debug=True)

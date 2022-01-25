from flask import Flask, render_template
import random
import datetime
import requests


AGIFY_API = "https://api.agify.io"
GENDERIZE_API ="https://api.genderize.io"
app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    random_number = random.randint(0,9)
    now = datetime.date.today().year
    return render_template("index.html", number=random_number, year=now)


@app.route('/guess/<name>')
def web(name):
    params={
        "name": name
    }
    agify = requests.get(url=AGIFY_API, params=params)
    agify.raise_for_status()
    age = agify.json()["age"]
    genderize = requests.get(url=GENDERIZE_API, params=params)
    genderize.raise_for_status()
    gender = genderize.json()["gender"]
    return render_template("age_gender.html", name=name, age=age, gender=gender)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

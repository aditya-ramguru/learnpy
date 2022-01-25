from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", post=all_posts)


@app.route('/post/<int:id_num>')
def get_post(id_num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", _id=id_num, post=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

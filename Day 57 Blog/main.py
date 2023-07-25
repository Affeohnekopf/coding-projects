from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_komplett = requests.get('https://api.npoint.io/e49b9434f27c68589f93')
    blog_komplett = blog_komplett.json()
    return render_template("index.html", blog=blog_komplett)

@app.route('/post/<int:post_id>')
def post(post_id):
    blog_id = post_id
    blog_komplett = requests.get('https://api.npoint.io/e49b9434f27c68589f93')
    blog_komplett = blog_komplett.json()
    return render_template("post.html", id=blog_id, blog=blog_komplett)

if __name__ == "__main__":
    app.run(debug=True)

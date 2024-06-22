from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", blog_posts = get_blog_content())

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def display_post(id):
    return render_template("post.html", id = id, blog_posts = get_blog_content())

def get_blog_content():
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    blog_response = requests.get(blog_url)
    blog_json = blog_response.json()
    return blog_json

if __name__ == "__main__":
    app.run(debug=True)
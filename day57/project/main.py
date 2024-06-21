from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route('/')
def home():
    blog_json = get_json_dump_of_all_blogs()
    return render_template("index.html", blog_posts = blog_json)

@app.route('/post/<int:id>')
def get_blog(id):
    blog_json = get_json_dump_of_all_blogs()
    return render_template("post.html", blog_posts = blog_json, id=id)

def get_json_dump_of_all_blogs():
    blog_url = "https://api.npoint.io/e60b51b6afab7f6e52c6"
    blog_response = requests.get(blog_url)
    blog_json = blog_response.json()
    return blog_json
if __name__ == "__main__":
    app.run(debug=True)

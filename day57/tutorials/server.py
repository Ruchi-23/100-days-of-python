from flask import Flask
from flask import render_template
import random
import datetime
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    num = random.randint(0,10)
    yr = datetime.datetime.now().year
    return render_template("index.html", n = num, year=yr, name="Ruchira")

@app.route('/guess/<name>')
def guess_gender_age(name):
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    json_response = response.json()
    gender = json_response["gender"]
    url2 = f"https://api.agify.io/?name={name}"
    response2 = requests.get(url2)
    json_response2 = response2.json()
    age = json_response2["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route('/personal')
def npointapi():
    personal_response = requests.get('https://api.npoint.io/1fdb04deef67f0570417')
    personal_json = personal_response.json()
    name = personal_json["name"]
    dob = personal_json["birthday"]
    return render_template("npoint.html", name=name, dob=dob)

@app.route("/blog")
def blog_posts():
    blog_url = "https://api.npoint.io/e60b51b6afab7f6e52c6"
    blog_response = requests.get(blog_url)
    blog_json = blog_response.json()
    return render_template("blog.html", blog_posts = blog_json)
if __name__ == "__main__":
    app.run(debug=True)
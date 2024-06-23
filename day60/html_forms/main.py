from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello_page():
    username = request.form['username']
    return render_template("hello.html", user=username)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
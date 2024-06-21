from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/<filename>')
def html_path(filename):
    if filename == "left-sidebar.html":
        return render_template('left-sidebar.html')
    elif filename == "right-sidebar.html":
        return render_template('right-sidebar.html')
    elif filename == "no-sidebar.html":
        return render_template('no-sidebar.html')
    elif filename == "elements.html":
        return render_template('elements.html')

if __name__ == "__main__":
    app.run(debug=True)
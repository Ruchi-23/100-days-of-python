from flask import Flask
from custom_decorators import bold_decorator
from custom_decorators import italics_decorator
from custom_decorators import underline_decorator
app = Flask(__name__)

@app.route('/')
@bold_decorator
@italics_decorator
@underline_decorator
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
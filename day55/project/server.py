from flask import Flask
import random
app = Flask(__name__)
n = 5
@app.route('/')
def guess_word():
    return '<h1>Guess a number between 0 and 9</h1><div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/M16EnP70Vd6abjtsJT/video" width="480"></iframe></div>'

@app.route('/<int:num>')
def low_high_url(num):
    if(num == n):
        return '<h1 style="color:green">You found me!</h1><iframe src="https://giphy.com/embed/uzeNIesA88p9hbkAHs" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/blink-classified-our-little-secret-uzeNIesA88p9hbkAHs">via GIPHY</a></p>'
    elif(num > n):
        return '<h1 style="color:red">Too high, try again!</h1><iframe src="https://giphy.com/embed/Fu3OjBQiCs3s0ZuLY3" width="270" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/moodman-reaction-Fu3OjBQiCs3s0ZuLY3">via GIPHY</a></p>'
    elif(num < n):
        return '<h1 style="color:red">Too low, try again!</h1><iframe src="https://giphy.com/embed/mlvseq9yvZhba" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/funny-cat-mlvseq9yvZhba">via GIPHY</a></p>'

if __name__ == "__main__":
    app.run(debug=True)
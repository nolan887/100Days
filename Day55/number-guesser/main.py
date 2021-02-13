from flask import Flask
import random
app = Flask(__name__)

answer = random.randint(0,9)

def make_plain(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper


@app.route('/<int:number>')
def guessed_page(number):
    if number == answer:
        return "<h1 style='color: green'>CORRECT!</h1>" \
               "<br><img src='https://media.giphy.com/media/8VrtCswiLDNnO/giphy.gif'>"
    elif number > answer:
        return "<h1 style='color: blue'>Incorrect, too high.</h1>" \
               "<br><img src='https://media.giphy.com/media/3fibzY6W6vCYY8sAky/giphy.gif'>"
    else:
        return "<h1 style='color: blue'>Incorrect, too low. You've got to pump it up!</h1>" \
               "<br><img src='https://media.giphy.com/media/7SZwo1ZVPfCGiFEGRx/giphy.gif'>"

@app.route('/')
@make_plain
def guess_screen():
    return 'Guess a number between 0 and 9!' \
           '<br><img src="https://media.giphy.com/media/xTiTnIilwuFFFpf2Cc/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)

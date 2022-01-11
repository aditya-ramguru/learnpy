from flask import Flask
import random

app = Flask(__name__)
@app.route('/')
def introduction():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'

nlist = [0,1,2,3,4,5,6,7,8,9]
random_num = random.choice(nlist)

@app.route('/<int:number>')
def check(number):
    if number == random_num:
        return "<h1 style='color:green'>You found me</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif number > random_num:
        return "<h1 style='color:red'>Too high try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style='color:purple'>Too low try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
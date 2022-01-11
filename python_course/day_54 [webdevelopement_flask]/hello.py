from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
       return f'<b>{function()}</b>'
    return bold


def make_italic(function):
    def italic():
        return f'<em>{function()}</em>'
    return italic


def underline(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


@app.route('/')
def hello_world():
    # rendering html elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media3.giphy.com/media/8vO8M5ct3sWIJ913ho/giphy.gif?cid=ecf05e47af2f313df07600b2efc40d6c4e9fe370094dcde3&rid=giphy.gif&ct=g" ' \
           'width=200</img>'


@app.route('/bye')
@make_bold     # same as make_bold(bye)
@make_italic   # same as make_italic(bye)
@underline
def bye():
    return '<p>bye</p>'


@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'hello there {name} and you {number} years old'


if __name__ == "__main__":
    # run app in debug mode, aito-reload
    app.run(debug=True)


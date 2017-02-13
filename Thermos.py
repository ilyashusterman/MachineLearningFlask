from mimetypes import init

from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}".format(self.firstname[0], self.lastname[0])


@app.route('/test')
def test():
    return 'Thermos test working GET!'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title passed from view to template",
                           text="Text passed from view to template", user=User("ilya", "shusterman"))


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run()  # to get app running in debug is debug=True

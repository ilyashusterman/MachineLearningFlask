from mimetypes import init
from logging import DEBUG
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.logger.setLevel(DEBUG)

images = []


def store_image(image):
    images.append(dict(
        image=image,
        user="ilya",
        date=datetime.utcnow()
    ))


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


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        image = request.form['image']
        file_image = request.files
        store_image(image)
        store_image(file_image)
        app.logger.debug('stored images : ' + image)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)  # to get app running in debug is debug=True

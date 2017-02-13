# from logging import DEBUG
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ImageForm

app = Flask(__name__)
# app.logger.setLevel(DEBUG)
images = []
app.config['SECRET_KEY'] = '\x87\x98g\xc3\xbd\xd8r\x99\xb9\x85p\xc1\xca8p\x94\xe5\xf0\x82\x89\xb6p,\xe1'


def store_image(image,description):
    images.append(dict(
        image=image,
        description=description,
        user="ilya",
        date=datetime.utcnow()
    ))


def new_images(num):
    return sorted(images, key=lambda bm: bm['date'], reverse=True)[:num]


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
    return render_template('index.html', new_images=new_images(5), title="Title passed from view to template",
                           text="Text passed from view to template", user=User("ilya", "shusterman"))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ImageForm(request.form)
    if request.method == 'POST' and form.validate():
        image = form.image
        description = form.description.data
        store_image(image, description)
        #image = request.form['image']
        # file_image = request.files
        # store_image(file_image)
        # app.logger.debug('stored images : ' + image)

        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)  # to get app running in debug is debug=True

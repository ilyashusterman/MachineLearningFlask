from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url
from wtforms import Form, BooleanField, StringField, PasswordField, validators, FileField

class ImageForm(Form):
    image = FileField('image')
    description = StringField('Add an optional description:')


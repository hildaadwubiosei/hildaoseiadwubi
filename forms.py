from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired

class SubmitMessage(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message', validators=[DataRequired()])
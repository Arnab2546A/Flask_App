from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name=StringField("Full Name", validators=[DataRequired()])
    email=StringField("Email", validators=[DataRequired(), Email(message="yaha imaandari chalat hai babu..na toh ghare jaake sutti babu..")])
    password=PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit=SubmitField("Register")
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, DataRequired


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log In")


class MemoryForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Your Memory", validators=[DataRequired()])
    image = FileField(
        "Upload Photo (optional)", validators=[FileAllowed(["jpg", "jpeg", "png"])]
    )
    submit = SubmitField("Share Memory")

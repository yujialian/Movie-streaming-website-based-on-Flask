# _*_ coding: utf-8 _*_
__author__ = 'Yujia Lian'
__date__ = '7/28/17 4:18 PM'

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError
from app.models import User


class RegistForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Please enter user name!")
        ],
        description="User name",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Please enter user name!",
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Please enter password!")
        ],
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Please enter password!",
        }
    )
    repwd = PasswordField(
        label="Confirm password",
        validators=[
            DataRequired("Please confirm password!"),
            EqualTo("pwd", message="The passwords you enter are not identical!")
        ],
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Please confirm password!",
        }
    )
    email = StringField(
        label="Email",
        validators=[
            DataRequired("Please enter email address!"),
            Email("The email format is not valid!")
        ],
        description="Email",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Please enter email address!",
        }
    )
    phone = StringField(
        label="Phone",
        validators=[
            DataRequired("Please enter phone number!"),
            Regexp("^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", message="Wrong phone format!")
        ],
        description="Email",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Please enter phone number!",
        }
    )
    submit = SubmitField(
        'Register',
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("The username you entered already exist!")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("The email you entered already exist!")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("The phone number you entered already exist!")


class LoginForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Please enter user name!")
        ],
        description="User name",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter user name!",
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Please enter password!")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter password!",
        }
    )
    submit = SubmitField(
        'Login',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block"
        }
    )


class UserdetailForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Please enter user name!")
        ],
        description="User name",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter user name!",
        }
    )
    email = StringField(
        label="Email",
        validators=[
            DataRequired("Please enter email address!"),
            Email("The email format is not valid!")
        ],
        description="Email",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter email address!",
        }
    )
    phone = StringField(
        label="Phone",
        validators=[
            DataRequired("Please enter phone number!"),
            Regexp("^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", message="Wrong phone format!")
        ],
        description="Email",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter phone number!",
        }
    )
    face = FileField(
        label="Head",
        validators=[
            DataRequired("Please upload you head image!")
        ],
        description="Head",
    )
    info = TextAreaField(
        label="Description",
        validators={
            DataRequired("Please input movie description!")
        },
        description="Movie description",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        'Save',
        render_kw={
            "class": "btn btn-success"
        }
    )


class Pwd_Form(FlaskForm):
    old_pwd = PasswordField(
        label="Old password",
        validators=[
            DataRequired("Please enter old password!")
        ],
        description="Old password",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter old password!",
        }
    )
    new_pwd = PasswordField(
        label="New password",
        validators=[
            DataRequired("Please enter new password!")
        ],
        description="New password",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter new password!",
        }
    )

    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-success",
        }
    )

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session["user"]
        user = User.query.filter_by(
            name=name
        ).first()
        if not user.check_pwd(pwd):
            raise ValidationError("Password you entered dose not match!")


class CommentForm(FlaskForm):
    content = TextAreaField(
        label="Comments",
        validators={
            DataRequired("Please input movie comments!")
        },
        description="Comments",
        render_kw={
            "id":"input_content"
        }
    )
    submit = SubmitField(
        'Comment',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )

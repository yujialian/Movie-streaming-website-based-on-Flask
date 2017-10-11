# _*_ coding: utf-8 _*_
__author__ = 'Yujia Lian'
__date__ = '7/28/17 4:18 PM'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Admin, Tag, Auth, Role


class LoginForm(FlaskForm):
    """admin login form"""
    account = StringField(
        label="Username",
        validators=[
            DataRequired("Please enter user name!")
        ],
        description="User name",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter user name!",
            # "required": "required"
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
            # "required": "required"
        }
    )

    submit = SubmitField(
        'Login',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("Username is invalid!")


class TagForm(FlaskForm):
    name = StringField(
        label="Tag name",
        validators={
            DataRequired("Please input tag!")
        },
        description="Tag",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "Please input tag name!"
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class MovieForm(FlaskForm):
    title = StringField(
        label="Movie name",
        validators={
            DataRequired("Please input movie name!")
        },
        description="Movie name",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "Please input movie name!"
        }
    )

    url = FileField(
        label="Documents",
        validators={
            DataRequired("Please upload file!")
        },
        description="File",
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

    logo = FileField(
        label="Cover",
        validators={
            DataRequired("Please upload cover!")
        },
        description="Cover",
    )

    star = SelectField(
        label="Grade",
        validators={
            DataRequired("Please select level of grade!")
        },
        coerce=int,
        choices=[(1, "1 star"), (2, "2 star"), (3, "3 star"), (4, "4 star"), (5, "5 star")],
        description="Grade",
        render_kw={
            "class": "form-control",
        }
    )

    tag_id = SelectField(
        label="Tag",
        validators={
            DataRequired("Please select tag!")
        },
        coerce=int,
        choices=[(v.id, v.name) for v in Tag.query.all()],
        description="Tag",
        render_kw={
            "class": "form-control",
        }
    )

    area = StringField(
        label="Area",
        validators={
            DataRequired("Please input area!")
        },
        description="Area",
        render_kw={
            "class": "form-control",
            "placeholder": "Please input area!"
        }
    )

    length = StringField(
        label="Length",
        validators={
            DataRequired("Please input length!")
        },
        description="Length",
        render_kw={
            "class": "form-control",
            "placeholder": "Please input length!"
        }
    )

    release_time = StringField(
        label="Release time",
        validators={
            DataRequired("Please select release time!")
        },
        description="Release time",
        render_kw={
            "class": "form-control",
            "placeholder": "Please select release time!",
            "id": "input_release_time"
        }
    )

    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class PreviewForm(FlaskForm):
    title = StringField(
        label="Preview name",
        validators={
            DataRequired("Please input preview name!")
        },
        description="Preview name",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "Please input movie name!"
        }
    )

    logo = FileField(
        label="Preview cover",
        validators={
            DataRequired("Please upload preview cover file!")
        },
        description="Preview cover",
    )

    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
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
            "class": "btn btn-primary",
        }
    )

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session["admin"]
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(pwd):
            raise ValidationError("Old password dose not match!")


class AuthForm(FlaskForm):
    name = StringField(
        label="Authority name",
        validators={
            DataRequired("Please input authority name!")
        },
        description="Authority name",
        render_kw={
            "class": "form-control",
            "placeholder": "Please input authority name!"
        }
    )
    url = StringField(
        label="Authority address",
        validators={
            DataRequired("Please input authority address!")
        },
        description="Authority address",
        render_kw={
            "class": "form-control",
            "placeholder": "Please input authority address!"
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class RoleForm(FlaskForm):
    name = StringField(
        label="Role name",
        validators={
            DataRequired("Please input role name!")
        },
        description="Role name",
        render_kw={
            "class": "form-control",
            "placeholder": "Please input role name!"
        }
    )
    auths = SelectMultipleField(
        label="Authority list",
        validators={
            DataRequired("Please select authority list!")
        },
        description="Authority list",
        coerce=int,
        choices=[(v.id, v.name) for v in Auth.query.all()],
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class AdminForm(FlaskForm):
    name = StringField(
        label="Admin name",
        validators=[
            DataRequired("Please enter admin name!")
        ],
        description="Admin name",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter admin name!",
        }
    )
    pwd = PasswordField(
        label="Admin password",
        validators=[
            DataRequired("Please enter admin password!")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter admin password!",
        }
    )
    rep_pwd = PasswordField(
        label="Admin confirm password",
        validators=[
            DataRequired("Please confirm admin password!"),
            EqualTo("pwd", message="The passwords you enter are not identical!")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Please confirm admin password!",
        }
    )
    role_id = SelectField(
        label="Assigned role",
        choices=[(v.id, v.name) for v in Role.query.all()],
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )

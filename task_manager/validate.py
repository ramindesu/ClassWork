import re
from datetime import datetime


class ValidationError(Exception):
    pass


username_validate = re.compile(r"^[a-zA-Z0-9]{3,20}$")
password_validate = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"
)
phone_validate = re.compile(r"^\+?\d{10,15}$")
email_validate = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validate_username(username):
    if not username_validate.match(username):
        raise ValidationError(
            "must be string and more than 3 or less than 20 charachaters"
        )
    return username


def validate_password(password):
    if not password_validate.match(password):
        raise ValidationError(
            "musst be more than 8 chars and has numbers a lowercase letter and special charachters"
        )
    return password


def validate_phone(phone):
    if not phone_validate.match(phone):
        raise ValidationError("must be like +9823423543 or 09924232345")
    return phone


def validate_email(email):
    if not email_validate.match(email):
        raise ValidationError("email is not valid")


def validation_title(title):
    if not title:
        raise ValidationError("title cant be empty")

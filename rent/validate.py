import re
class ValidationError(Exception):
    pass
username_validate = re.compile(r"^[a-zA-Z]{3,20}$")
password_validate = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z1-9]){8,}$"
)
phone_validate = re.compile(r"^\+?\d{10,15}$")
email_validate = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_username(username):
    if not username_validate.match(username):
        raise ValidationError("must be letters and upper than 2 charachter")
    return username

def validate_email(email):
    if not email_validate.match(email):
        raise ValidationError("email is not correct")
    return email

def validate_password(password):
    if not password_validate.match(password):
        raise ValidationError("password is not valid")
    


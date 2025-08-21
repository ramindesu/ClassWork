import re 
from datetime import datetime
class ValidationError(Exception):
    pass

username_validate = re.compile(r"^[a-zA-Z0-9]{3,20}$")
password_validate = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$")
phone_validate = re.compile(r"^\+?\d{10,15}$")
email_validate = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
def validate_username(username):
    if not username_validate.match(username):
        raise ValidationError("must be string and more than 3 or less than 20 charachaters")
    return username


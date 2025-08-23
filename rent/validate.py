import re

username_validate = re.compile(r"^[a-zA-Z]{3,20}$")
password_validate = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z1-9]){8,}$"
)
phone_validate = re.compile(r"^\+?\d{10,15}$")
email_validate = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


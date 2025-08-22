import re
user = input("insert the date")
regex_pattern = re.compile(r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$")
def validate_year(input):
    output = "valid date" if regex_pattern.match(input) else "invalid date"
    return output 

print(validate_year(user))
# 2025-01-22
# 2025-13-10
# 2025-02-30
import re

password = input("Enter a password: ")
if (len(password) >= 6 and
    re.search("[a-z]", password) and
    re.search("[A-Z]", password) and
    re.search("[0-9]", password) and
    re.search("[$#@]", password)):
    print("Password is valid")
else:
    print("Password is invalid")

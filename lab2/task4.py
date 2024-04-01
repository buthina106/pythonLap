
# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email
# or not
import re

def validate_name(name):
    return len(name.strip()) > 0 and name.isalpha()

def validate_email(email):
    return re.match(r'^[\w\.\+\-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', email.strip()) is not None


def get_name():
    while True:
        name = input("Enter your name: ").strip()
        if validate_name(name):
            return name
        else:
            print("Invalid name! Please enter a valid name.")

def get_email():
    while True:
        email = input("Enter your email: ").strip()
        if validate_email(email):
            return email
        else:
            print("Invalid email! Please enter a valid email.")

name = get_name()
email = get_email()
print(f"Name: {name}\nEmail: {email}")




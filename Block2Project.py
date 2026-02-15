"""
WARNINGS
This tool is for educational use only and should not be used to ensure or confirm that a password is
secure and strong. This tool should not be used to store or confirm passwords for sensitive or personal information or
for any external use.
"""
# importing a standard for regular expressions
import re


def main():
    # bool to check if the password is strong
    strong_password = False

    # loop that continues until a strong password is received
    while not strong_password:

        # assuming that the password is strong at first and setting it to true
        strong_password = True

        # prompting the user to enter their password
        user_input = input("Enter a password: ")

        # checking for an upper-case letter and setting strong password to false if none found
        if not re.findall(r'[A-Z]+', user_input):
            print("You need at least one upper-case letter.")
            strong_password = False

        # checking for a number and setting strong password to false if none found
        if not re.findall(r'[0-9]+', user_input):
            print("You need at least one number.")
            strong_password = False

        # checking for a lower-case letter and setting strong password to false if none found
        if not re.findall(r'[a-z]+', user_input):
            print("You need at least one lower-case letter.")
            strong_password = False

        # checking for a special character (no spaces) and setting strong password to false if none found
        if not re.findall(r'[@\+\?\(\)!\[\]#\$%\^&\*\-\=]', user_input):
            print("You need to have at least one special character ( @+?()![]#$%^&*-= ).")
            strong_password = False

        # checking for no spaces in the password
        if re.findall(r'\s+', user_input):
            print("You cannot have any spaces in your password.")
            strong_password = False

        # checking the length of the password and setting strong password to false if none found
        if len(user_input) < 13:
            print("Your password needs to be 13+ characters.")
            strong_password = False

    # if all checks pass then the password is strong
    print("You have a strong password :) !")


if __name__ == "__main__":
    main()

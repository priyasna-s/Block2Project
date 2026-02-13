#importing a standard for regular expressions
import re


def main():
    # bool to check if the password is strong and for no white space
    strong_password = False
    does_not_have_space = False

    # loop that continues until a strong password is received
    while not strong_password and not does_not_have_space:

        # prompting the user to enter their password
        user_input = input("Enter a password: ")

        # checking for an upper-case letter
        if not re.findall(r'[A-Z]+', user_input):
            print("You need at least one upper-case letter.")

        # checking for a number
        if not re.findall(r'[0-9]+', user_input):
            print("You need at least one number.")

        # checking for a lower-case letter
        if not re.findall(r'[a-z]+', user_input):
            print("You need at least one lower-case letter.")

        # checking for a space in the password
        if re.findall(r'\s+', user_input):
            print("You cannot have any spaces in your password.")
            does_not_have_space = True

        # checking for a special character
        if not re.findall(r'\W+', user_input):
            print("You need to have at least one special character ( @+?()![]#$%^&*-= )")

        # checking the length of the password
        if len(user_input) < 13 and not re.findall(r'\s+', user_input):
            print("Your password needs to be 13+ characters")
        else:
            if not does_not_have_space:
                strong_password = True
                print("You have a strong password :) !")


if __name__ == "__main__":
    main()

import random
import string


def get_user_input():
    while True:
        try:
            length_of_password = int(input("Enter the desired length of the password: "))
            if length_of_password <= 0:
                print("Length must be a positive integer:")
            else:
                return length_of_password
        except ValueError:
            print("Invalid input. Please enter a valid length in the form of integers:")


class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length):
        password = ''.join(random.choice(self.characters) for _ in range(length))
        return password

    def main(self):
        length = get_user_input()
        password = self.generate_password(length)
        print("Generated Password:", password)


if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.main()

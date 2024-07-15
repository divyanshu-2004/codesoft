import string
import random

def generate_password(length):
    c = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(c) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
                password = generate_password(length)
                print(f"Generated Password: {password}")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
main()

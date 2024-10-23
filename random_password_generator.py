import random
import string

def print_welcome_message():
    print("Welcome to the PyPassword Generator!")

def get_password_requirements():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    return nr_letters, nr_symbols, nr_numbers

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '!#$%&()*+?@^_'

    password_list = []
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    return ''.join(password_list)

def print_password_strength(password):
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_symbols = any(c in '!#$%&()*+?@^_' for c in password)
    has_numbers = any(c.isdigit() for c in password)

    if length >= 12 and has_letters and has_symbols and has_numbers:
        strength = "Very Strong"
    elif length >= 8 and has_letters and (has_symbols or has_numbers):
        strength = "Strong"
    elif length >= 6:
        strength = "Moderate"
    else:
        strength = "Weak"

    print(f"Password Strength: {strength}")

print_welcome_message()
while True:
    nr_letters, nr_symbols, nr_numbers = get_password_requirements()
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"\nYour generated password is: {password}")
    print_password_strength(password)

    regenerate = input("\nWould you like to generate another password? Type Yes or No: ").lower()
    if regenerate != "yes":
        break

print("\nThank you for using PyPassword Generator. Stay secure!")

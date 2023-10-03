# random password generator
import string
import random


def generate_password(length=12, include_nums=True, include_symbols=True):
    source = string.ascii_letters
    if include_nums:
        source += string.digits
    if include_symbols:
        source += string.punctuation

    password = ''.join(random.choice(source) for _ in range(length))
    return password


def check_password_strength(password):
    strength = 0
    comment = 'Password lacks: '
    strength_category = ['Weak', 'Medium', 'Strong']

    # should be more than 12 characters
    if len(password) >= 12:
        strength += 1

    has_digit = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)

    # if password contains everything increase strength by 1
    if has_digit and has_symbols:
        strength += 1

    if not has_digit:
        comment += 'Numbers, '
    if not has_symbols:
        comment += 'Special character, '

    print(comment)
    return strength_category[strength]


if __name__ == '__main__':
    length = int(input("Enter length for password: "))
    nums = input("Include numbers (y/n): ").lower() == 'y'
    syms = input("Include symbols (y/n): ").lower() == 'y'
    password = generate_password(length, nums, syms)
    print(f"\nGenerated Password: {password}")

    choice = input("Check password's Strength? (y/n): ").lower() == 'y'
    if choice:
        strength = check_password_strength(password)
        print(f"Remark: {strength} strength password")

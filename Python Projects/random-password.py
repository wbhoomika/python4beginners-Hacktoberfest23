import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    """
    Generate a random password with the specified length and character options.
    :param length: The length of the password.
    :param use_digits: Include digits in the password.
    :param use_special_chars: Include special characters in the password.
    :return: A random password.
    """
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        return "Password length should be at least 1."
    
    if not use_digits and not use_special_chars:
        return "Password must include digits and/or special characters for security."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_digits, use_special_chars)
    print(f"Generated Password: {password}")
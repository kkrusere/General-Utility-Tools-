import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets based on complexity requirements
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets based on complexity requirements
    characters = lowercase_letters + uppercase_letters + digits + special_chars

    # Check if at least one character set is chosen
    if not characters:
        raise ValueError("You must select at least one character set.")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        use_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_digits, use_special_chars)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

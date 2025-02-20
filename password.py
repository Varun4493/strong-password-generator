import random
import string
import os

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True, exclude_ambiguous=True, avoid_repeats=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special = string.punctuation if include_special else ""
    
    ambiguous = "lI1O0"
    if exclude_ambiguous:
        lowercase = ''.join(c for c in lowercase if c not in ambiguous)
        uppercase = ''.join(c for c in uppercase if c not in ambiguous)
        numbers = ''.join(c for c in numbers if c not in ambiguous)
        special = ''.join(c for c in special if c not in ambiguous)

    all_characters = lowercase + uppercase + numbers + special
    if not all_characters:
        return "Error: No character set selected!"

    password = []
    while len(password) < length:
        char = random.choice(all_characters)
        if avoid_repeats and char in password:
            continue
        password.append(char)

    return ''.join(password)

def evaluate_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    strength_score = sum([has_upper, has_lower, has_digit, has_special])
    if length >= 12 and strength_score == 4:
        return "Strong"
    elif length >= 8 and strength_score >= 3:
        return "Medium"
    else:
        return "Weak"

def save_password(label, password):
    if not os.path.exists("passwords.txt"):
        with open("passwords.txt", "w") as f:
            f.write("Saved Passwords:\n")

    with open("passwords.txt", "a") as f:
        f.write(f"{label}: {password}\n")

    print(f"Password saved as '{label}' in 'passwords.txt'.")

def main():
    while True:
        print("\n=== Strong Password Generator ===")
        print("1. Generate a Password")
        print("2. Generate Multiple Passwords")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_special = input("Include special characters? (y/n): ").lower() == 'y'
            exclude_ambiguous = input("Exclude ambiguous characters? (y/n): ").lower() == 'y'
            avoid_repeats = input("Avoid repeated characters? (y/n): ").lower() == 'y'

            password = generate_password(length, include_uppercase, include_numbers, include_special, exclude_ambiguous, avoid_repeats)
            print(f"Generated Password: {password}")
            print(f"Password Strength: {evaluate_password_strength(password)}")

            save_option = input("Save this password? (y/n): ").lower()
            if save_option == 'y':
                label = input("Enter a label for this password: ")
                save_password(label, password)

        elif choice == "2":
            count = int(input("How many passwords do you want to generate? "))
            length = int(input("Enter password length: "))
            include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_special = input("Include special characters? (y/n): ").lower() == 'y'
            exclude_ambiguous = input("Exclude ambiguous characters? (y/n): ").lower() == 'y'
            avoid_repeats = input("Avoid repeated characters? (y/n): ").lower() == 'y'

            for i in range(count):
                password = generate_password(length, include_uppercase, include_numbers, include_special, exclude_ambiguous, avoid_repeats)
                print(f"Password {i + 1}: {password}")
                print(f"Strength: {evaluate_password_strength(password)}")

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()

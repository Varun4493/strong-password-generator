# strong-password-generatorStrong Password Generator

A Python-based Strong Password Generator that allows users to generate secure passwords with customizable options, evaluate their strength, and save them for future use. Perfect for personal and professional security needs.

Features

Generate strong, random passwords of any length.

Customize password options:

Include uppercase letters

Include numbers

Include special characters

Exclude ambiguous characters (e.g., l, I, 1, O, 0)

Avoid repeated characters


Evaluate password strength: Weak, Medium, Strong

Save generated passwords with labels to a local file (passwords.txt)

Option to generate multiple passwords at once

Simple and interactive command-line interface


Installation

1. Clone this repository:



git clone https://github.com/yourusername/strong-password-generator.git

2. Navigate to the project folder:



cd strong-password-generator

3. Run the Python script:



python password_generator.py

> Note: Requires Python 3.x



Usage

When you run the script, you will be presented with a menu:

1. Generate a Password – Customize options and generate a single password.


2. Generate Multiple Passwords – Generate several passwords with chosen settings.


3. Exit – Quit the program.



You will also be prompted to save passwords with a custom label to passwords.txt.

Example

=== Strong Password Generator ===
1. Generate a Password
2. Generate Multiple Passwords
3. Exit
Choose an option: 1

Enter password length: 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y
Exclude ambiguous characters? (y/n): y
Avoid repeated characters? (y/n): y

Generated Password: Ab9$kT7&uQz!
Password Strength: Strong
Save this password? (y/n): y
Enter a label for this password: MyEmail
Password saved as 'MyEmail' in 'passwords.txt'.

Contributing

Contributions are welcome! If you want to add features or improve the code:

1. Fork the repository.


2. Create a new branch (git checkout -b feature-name).


3. Make your changes.


4. Commit your changes (git commit -m "Add feature").


5. Push to the branch (git push origin feature-name).


6. Open a Pull Request.

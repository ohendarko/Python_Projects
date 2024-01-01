#!/usr/bin/python3
import sys
import pyperclip
import json

# Function to save passwords to a file
def save_passwords(passwords, filename='passwords.json'):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

    existing_data.update(passwords)

    with open(filename, 'w') as file:
        json.dump(existing_data, file)

# Function to load passwords from a file
def load_passwords(filename='passwords.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):

        return {}
# Initialize PASSWORDS at the beginning of the script
PASSWORDS = load_passwords()

while True:
    if len(sys.argv) < 2:
        print('Usage: pass.py [account]')
        sys.exit()

    account = sys.argv[1]

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for {} copied to clipboard.'.format(account))
        print('Exiting program.')
        break
    else:
        print(f"There is no account named {account}")
        print(f"Would you like to add/update a password for {account}?")
        answer = input("Y/n: ").strip()

        if answer == 'Y':
            while True:
                new_pass = input(f"Enter password for {account}: ")

                if new_pass:
                    confirmpass = input("Confirm password: ")
                    if new_pass == confirmpass:
                        PASSWORDS[account] = new_pass
                        break
                    elif new_pass != confirmpass:
                        print("Passwords do not match")
                else:
                    print("Password cannot be empty. Please enter a valid password.")
            save_passwords(PASSWORDS)
            print(f"Password for {account} added/updated successfully.")
        elif answer == 'n':
            print('Exiting...')
            sys.exit()
        else:
            print('Command not recognized')
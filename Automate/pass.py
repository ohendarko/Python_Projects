#!/usr/bin/python3
"""
Adapted from AUTOMATE THE BORING STUFF WITH PYTHON
By Al Sweigart
Page 136-138

Original Code:
===============================================
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}
import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
print('There is no account named ' + account)
===============================================

Issues and What can be improved upon:
==================================================
1. Passwords are predifined and can be only be added as part of the code.
What if there was a part of the code that allowed you to update
from the running instance of the program without actually opening up the module
to update the dictionary with the password.

Added/Modified:
=============
a. If password not found, initiate an addition of password for unknown account.
b. Moved password dictionary to a separate json file. Program searches
from this file instead of prestated dict in code.
c. Program saves new password to json file. Can be retrieved anytime.

PENDING features:
==========================================
i. Remove password
ii. Change password

REQUIRES basic knowledge in:
===============================================
1. Flow control; if, while, else loops
2. Dictionaries data structure
3. Functions
4. Command line arguments
5. Modules: json, pyperclip, sys
6. File i/o
7. Print formatting
"""
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
    print('''Welcome to password manager.
Please take note!
All accounts are saved and will be saved in lowercase.''')
    print()
    account = input("What account are you interested in?: ").strip().lower()

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
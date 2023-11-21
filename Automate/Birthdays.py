"""This module contains a function birthday() that
allows you to access birthdays by keying in names.
If name is not part of the birthdays DICTIONARY,
you can add to it.
Requires basic knowledge in:
1. Flow control; if, while, else loops
2. Dictionaries data structure
3. Functions
4. Print formatting
Adapted from AUTOMATE THE BORING STUFF WITH PYTHON by Al Sweigart,
page 106, 107"""


# birthday dictionary
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


def birthday():
    while True: # continue looping
        name = input("Enter a name (blank to quit) : ")  # prompt user to enter a name and store it in variable: name
        if name == "":  # if name is empty
            break       # exit loop
        if name in birthdays:  # if name you entered is an Exact match with a KEY in the birthdays DICTIONARY
            print("{} is the birthday of {}".format(birthdays[name], name))
        else:  # edge case where exact match is not found
            print('I do not have birthday information for {}'.format(name))
            bday = input("What is their birthday?\n: ")
            birthdays[name] = bday
            print("Birthday database update with {}".format(name))


def main():
    birthday()
    print("You quit the program\n"
          "Would you like to restart?\n"
          "Y/n")
    response = input("Y/n: ")
    if response == 'Y':
        birthday()
    elif response == 'n':
        exit(code=1)
    else:
        print("Command {} not recognized".format(response))
    for k, v in birthdays.items():
        print("{}:{}".format(k, v))

main()

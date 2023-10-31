# Building a calculator
print()
print("Warning!\nYou are now running a calculator\n "
      "Use spaces when neccessary")
digit1, opr, digit2 = input("Perform any calculation: ").split()
digit1 = int(digit1)
digit2 = int(digit2)
if opr == '+':
    result = digit1 + digit2
    print("{} + {} = {}".format(digit1, digit2, result))
elif opr == '-':
    result = digit1 - digit2
    print("{} - {} = {}".format(digit1, digit2, result))
elif opr == '*':
    result = digit1 * digit2
    print("{} * {} = {}".format(digit1, digit2, result))
elif opr == '/':
    result = digit1 / digit2
    print("{} / {} = {}".format(digit1, digit2, result))
elif opr == '%':
    result = digit1 % digit2
    print("{} % {} = {}".format(digit1, digit2, result))
elif opr == '**' or opr == '^':
    result = digit1 ** digit2
    print("{} exponent {} = {}".format(digit1, digit2, result))
else:
    print(f"Operator '{opr}' not supported in this calculator.\n"
          "Kindly contact support for assistance.\n"
          "Supported operators: + - * / ** ^ %\n"
          "If you believe you shouldn't see this message,\n"
          "contact admin for bug support")
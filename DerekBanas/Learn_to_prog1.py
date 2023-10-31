# Asking for 2 values
num1, num2 = input("Enter 2 numbers: ").split()

# Convert strings into integers
num1 = int(num1)
num2 = int(num2)

# Add values
sum = num1 + num2

# Subtract
difference = num1 - num2

# Multiply
product = num1 * num2

# Divide
quotient = num1 / num2

# Modulos
remainder = num1 % num2

# print results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} x {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

# miles to kms
print()
miles = input("Enter the value in miles: ")
kiloms = int(miles) * 1.60934
print("{} miles equals {} kilometers".format(miles, kiloms))

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
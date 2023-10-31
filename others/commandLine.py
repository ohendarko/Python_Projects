import sys

# n = len(sys.argv)
# print(n)

# for x in range(1, n):
#    print(sys.argv[x])
arg = sys.argv[1]

if arg == "test":
    print("This is a test")
elif arg == "mom":
    print("Your mom is a 10/10")
else:
    print("the argument is invalid")
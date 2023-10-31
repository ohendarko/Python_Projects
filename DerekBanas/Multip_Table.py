import random
import math
multi = [[0]*10 for i in range(10)]
for i in range(1, 10):
    for m in range(1, 10):
        multi[i][m] = i * m

for p in range(1, 10):
    for q in range(1, 10):
       print(multi[p][q], end=", ")
    print()

print("#############################")
# Create the multidimensional list
multTable = [[0] * 10 for i in range(10)]

# Increment with the outer for
for i in range(1, 10):

    # Increment with the inner for
    for j in range(1, 10):

        # Assign the value to the cell
        multTable[i][j] = i * j

# Output the data
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=", ")
    print()
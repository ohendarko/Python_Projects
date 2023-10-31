import random
import math

# You can remove comments to change output

numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

# numList.sort()

# numList.reverse()

# numList.insert(5, 10)

# numList.remove(10)

# numList.pop(2)

for k in numList:
    print (k, end=", ")
print()
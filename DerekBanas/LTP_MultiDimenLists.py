import random
import math

# 1 Creating a 10x10 list
print("1: Creating a 10x10 list")
multiDList = [[0]* 10 for i in range(10)]
multiDList[0][1] = 10
print(multiDList[0][1])
print()

# 2
print("#2")
listTable = [[0]* 4 for i in range(10)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()
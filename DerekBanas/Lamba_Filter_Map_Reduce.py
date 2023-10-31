print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
from functools import reduce
print(reduce((lambda x, y: x + y), range(1, 6)))
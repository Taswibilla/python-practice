#lambda
square = lambda x: x * x
print(square(4))   
#map
nums = [1, 2, 3, 4]

result = list(map(lambda x: x*2, nums))
print(result)   
#filter
nums = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)   
#reduce
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, nums)
print(result)   
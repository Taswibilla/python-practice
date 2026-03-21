#generator
def gen():
    for i in range(10):
        yield i
g = gen()
for i in range(10):
    print(next(g))
#iterator
nums = [10, 20, 30]

it = iter(nums)  
print(next(it))   
print(next(it))   
print(next(it))   
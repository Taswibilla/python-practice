import numpy as np

# 1. Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("Array a:", a)
print("Array b:", b)

# zeros, ones, arange, linspace
print("\nZeros:\n", np.zeros((2,3)))
print("\nOnes:\n", np.ones((2,2)))
print("\nArange:", np.arange(0,10,2))
print("\nLinspace:", np.linspace(0,1,5))


# 2. Array properties
print("\nShape:", a.shape)
print("Size:", a.size)
print("Data type:", a.dtype)


# 3. Mathematical operations
print("\nAddition:", a + b)
print("Multiplication:", a * b)
print("Square root:", np.sqrt(a))
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))


# 4. Indexing & slicing
print("\nFirst element:", a[0])
print("Slice (1 to 3):", a[1:4])


# 5. 2D array operations
c = np.array([[1,2,3],[4,5,6]])
print("\n2D Array:\n", c)
print("Element at (0,1):", c[0,1])


# 6. Reshaping
d = np.array([1,2,3,4,5,6])
print("\nReshaped (2x3):\n", d.reshape(2,3))


# 7. Random functions
print("\nRandom values:", np.random.rand(3))
print("Random integers:", np.random.randint(1,10,3))


# 8. Useful functions
e = np.array([10,5,20,3])
print("\nMax:", np.max(e))
print("Min:", np.min(e))
print("Argmax (index of max):", np.argmax(e))
print("Sorted:", np.sort(e))
data = [2, 4, 6, 8]

# Step 1: mean
mean = sum(data) / len(data)

# Step 2: MAD
mad = sum(abs(x - mean) for x in data) / len(data)

print("Mean:", mean)
print("MAD:", mad)

#using numpy
import numpy as np

data = np.array([2, 4, 6, 8])

mad = np.mean(np.abs(data - np.mean(data)))

print(mad)

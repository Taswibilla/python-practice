import numpy as np
# 1. Create matrices and vectors
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
v1 = np.array([1, 2])
v2 = np.array([3, 4])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Vector v1:", v1)
print("Vector v2:", v2)

# 2. Matrix addition
C = A + B
print("\nA + B =\n", C)

# 3. Scalar multiplication
k = 2
D = k * A
print("\n2 * A =\n", D)

# 4. Matrix multiplication
E = A @ B  # or np.dot(A, B)
print("\nA @ B =\n", E)

# 5. Transpose
A_T = A.T
print("\nTranspose of A:\n", A_T)

# 6. Determinant
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

# 7. Inverse (if determinant != 0)
if det_A != 0:
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:\n", A_inv)
    # Verify A * A_inv = I
    print("\nA @ A_inv =\n", A @ A_inv)

# 8. Dot product (vector)
dot_product = np.dot(v1, v2)
print("\nDot product of v1 and v2:", dot_product)
import numpy as np

# Create two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# A. Matrix Multiplication (Dot Product)
# Use @ for cleaner syntax or np.dot()
mat_mul = A @ B  
# Result: [[19, 22], [43, 50]]

# B. Transpose
# Flips the matrix over its diagonal (swaps rows and columns)
transpose_A = A.T
# Result: [[1, 3], [2, 4]]

# C. Determinant
# Requires the linalg (linear algebra) module
det_A = np.linalg.det(A)
# Result: -2.0 (approx)

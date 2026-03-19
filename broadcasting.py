import numpy as np

# Sample Data
matrix = np.array([[10, 20, 30], 
                   [40, 50, 60]])  # Shape (2, 3)
vector = np.array([1, 2, 3])       # Shape (3,)
scalar = 2                         # Shape ()

# A. Add 1D array to a 2D array
add_res = matrix + vector
# Result: [[11, 22, 33], [41, 52, 63]]

# B. Multiply matrix by a scalar
scalar_res = matrix * scalar
# Result: [[20, 40, 60], [80, 100, 120]]

# C. Multiply matrix by a vector (Element-wise)
element_mul = matrix * vector
# Result: [[10, 40, 90], [40, 100, 180]]

# D. Matrix-Vector Multiplication (Dot Product)
dot_res = matrix @ vector  # or np.dot(matrix, vector)
# Result: [140, 320]

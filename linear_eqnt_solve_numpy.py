import numpy as np

# Coefficients (Matrix A)
A = np.array([[2, 3], 
              [5, 4]])

# Constants (Vector B)
B = np.array([8, 13])

# Solve for x
# This computes the solution vector [x, y]
solution = np.linalg.solve(A, B)

# Results
print(f"Solution: x = {solution[0]}, y = {solution[1]}")
# Output: x = 1.0, y = 2.0

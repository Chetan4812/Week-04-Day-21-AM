import numpy as np

# Initialize two arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Element-wise addition
add_res = a + b           # [11, 22, 33, 44]

# Element-wise subtraction
sub_res = a - b           # [9, 18, 27, 36]

# Element-wise multiplication
mul_res = a * b           # [10, 40, 90, 160]


data = np.array([2, 4, 4, 4, 5, 5, 7, 9])

# Compute mean (average)
mean_val = np.mean(data)  # 5.0

# Compute variance
var_val = np.var(data)    # 4.0

# Compute standard deviation
std_val = np.std(data)    # 2.0

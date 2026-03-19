import numpy as np

# Sample array with mixed values
data = np.array([-2, -1, 0, 1, 2, 3, 4, 5])

# A. Compute Square and Cube
squared = np.square(data)  # or data ** 2
cubed = np.power(data, 3)  # or data ** 3

# B. Replace Negative Values with 0 (Boolean Masking)
# This modifies 'data' in place or creates a copy
data[data < 0] = 0 

# C. Normalize the Array (Min-Max Scaling)
# Formula: (x - min) / (max - min)
d_min, d_max = data.min(), data.max()
normalized = (data - d_min) / (d_max - d_min)

# Results
print(f"Squared: {squared}")
print(f"Cubed:   {cubed}")
print(f"Zeroed:  {data}")
print(f"Normalized: {normalized}")

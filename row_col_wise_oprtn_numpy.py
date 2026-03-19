import numpy as np

# Create a sample 5x5 dataset
data = np.array([
    [12, 45, 67, 23, 89],
    [34, 11, 90, 54, 21],
    [78, 33, 12, 67, 44],
    [10, 99, 23, 56, 82],
    [65, 43, 21, 88, 15]
])

# A. Find top 5 maximum values
# flatten() makes it 1D, sort() puts max at the end, [-5:] slices them
top_5 = np.sort(data.flatten())[-5:]

# B. Compute row-wise and column-wise sums
row_sums = np.sum(data, axis=1)  # Across columns
col_sums = np.sum(data, axis=0)  # Across rows

# C. Identify indices of values greater than a threshold
threshold = 80
# returns (row_indices, col_indices)
indices = np.where(data > threshold)

# Results
print(f"Top 5 Values: {top_5}")
print(f"Row Sums: {row_sums}")
print(f"Col Sums: {col_sums}")
print(f"Indices > {threshold}: {list(zip(indices[0], indices[1]))}")

import numpy as np

# 1. Create NumPy arrays of different dimensions (1D, 2D, 3D)
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# 2. Perform indexing and slicing operations
# Accessing a single element
val_1d = arr_1d[2]           # Returns 30 (indexing starts at 0)
val_2d = arr_2d[1, 2]        # Returns 6 (row 1, column 2)
val_3d = arr_3d[1, 0, 1]     # Returns 6 (depth 1, row 0, column 1)

# Slicing a range of elements
slice_1d = arr_1d[1:4]       # Returns [20, 30, 40] (index 1 to 3)

# 3. Extract specific rows, columns, and subarrays
row_1 = arr_2d[1, :]         # Extracts the second row: [4, 5, 6]
col_2 = arr_2d[:, 2]         # Extracts the third column: [3, 6, 9]
subarray = arr_2d[0:2, 1:3]  # Extracts a 2x2 subarray from the top-right: [[2, 3], [5, 6]]

# Displaying Results
print("1D Array:", arr_1d)
print("2D Array:\n", arr_2d)
print("3D Array:\n", arr_3d)
print("-" * 20)
print("1D Slice [1:4]:", slice_1d)
print("Row index 1 of 2D:", row_1)
print("Col index 2 of 2D:", col_2)
print("2x2 Subarray:\n", subarray)

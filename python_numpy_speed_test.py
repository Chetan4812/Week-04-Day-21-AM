import numpy as np
import time

# Create 1 million elements
size = 1_000_000
arr_np = np.arange(size)
arr_list = list(range(size))

# 1. Python Loop Performance
start_time = time.time()
python_sum = 0
for x in arr_list:
    python_sum += x
python_time = time.time() - start_time

# 2. NumPy Performance (Vectorised)
start_time = time.time()
numpy_sum = np.sum(arr_np)
numpy_time = time.time() - start_time

print(f"Python loop: {python_time:.6f}s")
print(f"NumPy sum:   {numpy_time:.6f}s")
print(f"NumPy is {python_time / numpy_time:.1f}x faster")

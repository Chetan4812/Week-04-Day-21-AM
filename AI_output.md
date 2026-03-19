### NumPy Performance

NumPy's performance comes from **vectorisation**, which is the ability to perform operations on entire arrays at once, and **broadcasting**, which allows those operations to happen even when arrays have different shapes.

#### 1. Vectorisation
Vectorisation replaces explicit Python loops with optimized, low-level C code. Instead of processing one element at a time in the Python interpreter, NumPy processes entire blocks of data simultaneously, often resulting in speeds 50–300x faster than standard loops.

> *Source: GeeksforGeeks*


```pyhton
import numpy as np
import time

data = np.arange(1_000_000)

# Slow: Python Loop
start = time.time()
loop_res = [x**2 for x in data]
print(f"Loop time: {time.time() - start:.4f}s")

# Fast: Vectorisation
start = time.time()
vect_res = data**2
print(f"Vectorised time: {time.time() - start:.4f}s")

```


## 2. Broadcasting

Broadcasting is a set of rules that allow element-wise operations between arrays of different shapes. It virtually "stretches" the smaller array to match the larger one **without actually copying the data**, making it highly memory-efficient.

### Rules for Compatibility:
Working from the rightmost (trailing) dimension backward, dimensions are compatible if they are:

1. Equal.
2. One of them is 1.

### Practical Example: Normalizing a Dataset
A common task is subtracting the mean of each column from every row in a matrix.

```pythom
# Matrix (4x3) and its column means (3,)
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
col_means = matrix.mean(axis=0)  # Shape (3,) -> [55, 65, 75]

# Broadcasting: (4, 3) - (3,) works because the trailing dimensions match (3 == 3)
centered_data = matrix - col_means

```


### Key Differences


| Feature | Vectorisation | Broadcasting |
| :--- | :--- | :--- |
| **Purpose** | Speeding up operations by removing loops. | Handling operations between different-shaped arrays. |
| **Mechanics** | Runs operations in optimized C/Fortran. | "Stretches" smaller dimensions to match larger ones. |
| **Memory** | Uses contiguous memory blocks for speed. | Avoids data replication to save memory. |








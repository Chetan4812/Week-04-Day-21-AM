# Week-04-Day-21-AM

# Part A — Concept Application (40%)

### 1. Create NumPy arrays of different dimensions (1D, 2D, 3D)
*   Perform indexing and slicing operations
*   Extract specific rows, columns, and subarrays <br>
[Solution](numpy_arrays_operations.py)

### 2. Implement basic operations using NumPy (without loops)
*   Element-wise addition, subtraction, multiplication
*   Compute mean, variance, and standard deviation <br>
[Solution](elemnt_wise_numpy_oprtns.py)

### 3. Demonstrate broadcasting
*   Add a 1D array to a 2D array
*   Multiply a matrix by a scalar and a vector
*   Explain how broadcasting works in each case <br>
[Solution](broadcasting.py)

## Explanation
For broadcasting to occur, NumPy compares shapes from right to left (trailing dimensions). Two dimensions are compatible if they are equal or if one of them is 1. 

**1D Array to 2D Array (+):**
* The matrix has shape (2, 3) and the vector has shape (3,).
* NumPy prepends a 1 to the vector's shape, making it (1, 3).
* The vector is then "stretched" vertically across the 2 rows to match the (2, 3) shape of the matrix.

**Matrix by a Scalar (*):**
* The scalar (0D) is treated as having a shape of (1, 1).
* It is broadcast across all rows and columns of the (2, 3) matrix, effectively multiplying every single element by the scalar value.

**Matrix by a Vector (Element-wise *):**
* Similar to addition, the (3,) vector is broadcast to (2, 3).
* Multiplication happens element-by-element between the original matrix and the "stretched" version of the vector.

**Matrix-Vector Multiplication (@):**
* This is not broadcasting; it is a standard linear algebra operation.
* The @ operator (or `np.dot`) calculates the dot product where the number of columns in the matrix must match the number of elements in the vector.


### 4. Implement vectorised operations
*   Compute square and cube of all elements
*   Replace all negative values with 0
*   Normalize an array (scale values between 0 and 1) <br>
[Solution](normlz_sqr_cube.py)

### 5. Given a dataset (NumPy array)
*   Find top 5 maximum values
*   Compute row-wise and column-wise sums
*   Identify indices of values greater than a threshold <br>
[Solution](row_col_wise_oprtn_numpy.py)

---
## Part B — Stretch Problem (30%)

### 1. Implement matrix operations using NumPy
*   Matrix multiplication
*   Transpose
*   Determinant <br>
[Solution](matrix_oprtns_numpy.py)

### 2. Solve a system of linear equations using NumPy <br>
[Solution](linear_eqnt_solve_numpy.py)

### 3. Compare performance
*   Compute sum of large array using Python loop vs NumPy
*   Report time difference and explain <br>
[Solution](python_numpy_speed_test.py)

---

## Part C — Interview Ready (20%)

**Q1 — What is NumPy broadcasting? Why is it useful?**

Broadcasting is a mechanism that allows NumPy to perform arithmetic operations on arrays with different shapes. It "stretches" the smaller array across the larger one so they have compatible shapes for element-wise calculations. 

### Why it’s useful:
*   **Memory Efficiency:** It doesn't actually create multiple copies of the smaller array in memory; it just acts as if it did during the calculation.
*   **Code Simplicity:** You can add a single value (scalar) or a 1D vector to a whole matrix without writing complex nested loops. [1, 2]


**Q2 (Coding) — Implement: normalize(X)**
*   Scale values between 0 and 1 using NumPy <br>
[Solution](scale_value_numpy.py)

**Q3 — What is the difference between vectorisation and loops? Why is NumPy faster?**

### The Difference:
*   **Loops (Python):** Process one element at a time. For every single element, Python must check the data type, find the correct operation, and update the iterator.
*   **Vectorisation (NumPy):** Expresses operations on entire arrays at once. It offloads the work to highly optimized, pre-compiled C and Fortran code. [3]

### Why NumPy Wins:
*   **Homogeneous Types:** Every element in a NumPy array is the same type (e.g., int64), so NumPy doesn't waste time checking types mid-calculation. [4]
*   **Contiguous Memory:** Arrays are stored in a single physical block of memory. This allows the CPU to use SIMD (Single Instruction, Multiple Data) to process multiple numbers in one clock cycle. [5]
*   **Low Overhead:** It skips the "overhead" of the Python interpreter for every step of the calculation. [3, 4]


---

## Part D — AI-Augmented Task (10%)

### 1. Prompt AI:
"Explain NumPy broadcasting and vectorisation with practical Python examples."

### 2. Document prompt and output

[AI Output](AI_output.md) for the above given prompt

### 3. Evaluate:
*   Are examples correct?
*   Is code efficient and runnable?

### Accuracy of Examples

*   **Broadcasting Logic:** The explanation of "stretching" dimensions from right to left is the standard way to understand NumPy's shape compatibility rules.
*   **Vectorisation Comparison:** The million-element square operation is the classic benchmark for demonstrating the speed difference between Python's overhead and C-level execution.


### Efficiency Analysis

*   **Memory Usage:** Using `data**2` (vectorised) is significantly more memory-efficient than a list comprehension, as it allocates a single contiguous block of memory rather than a list of individual Python integer objects.
*   **Normalization:** The `matrix - col_means` example uses broadcasting perfectly. It avoids the need to manually tile or repeat the `col_means` array, which would waste RAM.
*   **Modern Syntax:** Using `time.time()` for profiling is appropriate for high-level comparisons, and the f-string formatting makes the output readable.


### Runnability

The code snippets are self-contained. As long as `numpy` is installed (`pip install numpy`), you can copy-paste them into a `.py` file or a Jupyter cell and they will execute without error.

> **One minor optimization note:**
> In the normalization example, if you were working with a 3D array and wanted to subtract the mean of the first dimension, you would need to use `np.newaxis` or `.reshape()` to align the dimensions correctly, as broadcasting only automatically aligns trailing (right-most) dimensions.














---











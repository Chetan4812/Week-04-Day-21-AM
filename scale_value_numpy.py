import numpy as np

def normalize(X):
    # Formula: (x - min) / (max - min)
    x_min = np.min(X)
    x_max = np.max(X)
    
    # Check to avoid division by zero if all elements are the same
    if x_max == x_min:
        return np.zeros_like(X)
        
    return (X - x_min) / (x_max - x_min)

# Example usage:
data = np.array([10, 20, 30, 40, 50])
print(normalize(data)) 
# Output: [0.   0.25 0.5  0.75 1.  ]

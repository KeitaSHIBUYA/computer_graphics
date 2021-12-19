import numpy as np


x = np.array([[2, 1],
              [4, 1],
              [9, 1]])

y = np.array([[3],
              [7],
              [11]])

result = np.linalg.inv(x.T @ x) @ x.T @ y

print(result)

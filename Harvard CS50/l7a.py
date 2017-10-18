# My notes from lecture 7 (Machine learning), part 1

import numpy as np                  # for scientific computing
import matplotlib.pyplot as plt     # for generating plots

def dist(x, y):
    """Takes two points and returns the distance between them."""
    return np.sqrt(np.sum((x - y) ** 2))

X_train = np.array([[1, 1], [2, 2.5], [3, 1.2], [5.5, 6.3], [6, 9], [7, 6]])
X_test = np.array([3, 4])
Y_train = ["red", "red", "red", "blue", "blue", "blue"]

print(X_train[:, 0])
print(X_train[:, 1])

plt.figure()
plt.scatter(X_train[:, 0], X_train[:, 1], s = 170, color = Y_train[:])
plt.scatter(X_test[0], X_test[1], s = 170, color = "green")
plt.show()

num = len(X_train) # Number of points in X_train
distance = np.zeros(num)  # NumPy arrange of zeros
for i in range(num):
    distance[i] = dist(X_train[i], X_test)
print(distance)

min_index = np.argmin(distance) # Index with the smallest distance
print(Y_train[min_index])

# My notes from lecture 7 (Machine learning), part 2

import numpy as np                  # for scientific computing
import matplotlib.pyplot as plt     # for generating plots
from sklearn import datasets        # important data analysis lib

def dist(x, y):
    """Takes two points and returns the distance between them."""
    return np.sqrt(np.sum((x - y) ** 2))
    
digits = datasets.load_digits()

plt.figure()
plt.imshow(digits.images[345], cmap = plt.cm.gray_r, interpolation = "nearest")
plt.show()

X_train = digits.data[0:1000]       #changing the sample size changes the quality of the guess and the number of errors made.
Y_train = digits.target[0:1000]

num = len(X_train)
no_errors = 0 # number of errors
distance = np.zeros(num)
for j in range(1697, 1797):
    X_test = digits.data[j]
    for i in range(num):
        distance[i] = dist(X_train[i], X_test)
    min_index = np.argmin(distance)
    if Y_train[min_index] != digits.target[j]:
        no_errors += 1
print(no_errors)

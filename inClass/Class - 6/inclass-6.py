import numpy as np
import matplotlib .pyplot as plt

X = list(range(10))
Y = [1,3,2,5,7,8,8,9,10,12]

X = np.array(X)
Y = np.array(Y)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

numerator = (X - X_mean) * (Y - Y_mean)
numerator = np.sum(numerator)

denominator = (X - X_mean) * (X - X_mean)
denominator = np.sum(denominator)

slope = numerator / denominator
print('Slope', slope)
constant = Y_mean - slope * X_mean
print('Constant',   constant)

Y_op = slope * X + constant
print(Y_op)

plt.plot(X, Y_op)
plt.scatter(X, Y)
plt.show()

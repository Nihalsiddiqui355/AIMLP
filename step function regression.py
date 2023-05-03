import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


breakpoints = [-2, -1, 0, 1, 2]


X = np.array([-3, -2.5, -1.5, -1, 0, 1, 2, 2.5, 3]).reshape(-1, 1)


features = np.zeros((len(X), len(breakpoints) - 1))
for i in range(len(breakpoints) - 1):
    features[:, i] = np.where((X >= breakpoints[i]) & (X < breakpoints[i+1]), 1, 0).flatten()


y = np.array([1, 1.5, 1.5, 2, 2.5, 3, 3, 3.5, 4])


model = LinearRegression().fit(features, y)


print(model.coef_)
print(model.intercept_)


X_plot = np.linspace(-3, 3, 100).reshape(-1, 1)


features_plot = np.zeros((len(X_plot), len(breakpoints) - 1))
for i in range(len(breakpoints) - 1):
    features_plot[:, i] = np.where((X_plot >= breakpoints[i]) & (X_plot < breakpoints[i+1]), 1, 0).flatten()


y_plot = model.predict(features_plot)


plt.plot(X_plot, y_plot, label='Step Function Regression')


plt.scatter(X, y, label='Data Points')


plt.xlabel('X')
plt.ylabel('y')
plt.legend()


plt.show()

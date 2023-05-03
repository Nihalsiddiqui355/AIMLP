import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.read_csv("D:/RAJ/MY EDU/PG/PART 1/AIML/Position_Salaries.csv") 
X = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2].values


from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree = 2) 
X_poly = poly_reg.fit_transform(X) 
poly_reg.fit(X_poly, y) 
lin_reg_2 = LinearRegression() 
lin_reg_2.fit(X_poly, y)
y_poly_pred = lin_reg_2.predict(X_poly)

rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
r2 = r2_score(y,y_poly_pred)
print(rmse)
print(r2)


X_grid = np.arange(min(X), max(X), 0.1) 
X_grid = X_grid.reshape((len(X_grid), 1)) 
plt.scatter(X, y, color = 'red') 
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue') 
plt.title('Truth or Bluff (Polynomial Regression)') 
plt.xlabel('Position level') 
plt.ylabel('Salary') 
plt.show()

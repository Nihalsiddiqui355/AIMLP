import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
boston=datasets.load_boston() 
print(boston.data.shape)
print(boston.feature_names)
print(boston.target.shape)
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df.head(10)
boston_df['MEDV'] = boston.target
boston_df.describe()
boston_df.isnull().sum()
#boston_df.describe()
X_rooms = boston_df.RM
y_price = boston_df.MEDV
X_rooms = np.array(X_rooms).reshape(-1,1)
y_price = np.array(y_price).reshape(-1,1)
print(X_rooms.shape)
print(y_price.shape)
X_train_1, X_test_1, Y_train_1, Y_test_1 = train_test_split(X_rooms, y_price, test_size = 0.25, 
random_state=5)
print(X_train_1.shape)
print(X_test_1.shape)
print(Y_train_1.shape)
print(Y_test_1.shape)
reg_1 = LinearRegression()
reg_1.fit(X_train_1, Y_train_1)
y_train_predict_1 = reg_1.predict(X_train_1)
rmse = (np.sqrt(mean_squared_error(Y_train_1, y_train_predict_1)))
r2 = round(reg_1.score(X_train_1, Y_train_1),2)
print("The model performance for training set")
print("--------------------------------------")
print('RMSE is ',rmse)
print('R2 score is {}'.format(r2))
print("\n")
# model evaluation for test set
y_pred_1 = reg_1.predict(X_test_1)
rmse = (np.sqrt(mean_squared_error(Y_test_1, y_pred_1)))
r2 = round(reg_1.score(X_test_1, Y_test_1),2)
print("The model performance for testing set")
print("--------------------------------------")
print("Root Mean Squared Error: {}".format(rmse))
print("R^2: {}".format(r2))
print("\n")
#prediction_space = np.linspace(min(X_rooms), max(X_rooms)).reshape(-1,1) 
plt.scatter(X_rooms,y_price)
plt.plot(X_rooms,reg_1.predict(X_rooms),color='red',linewidth=3)
plt.ylabel('value of house/1000($)')
plt.xlabel('number of rooms')
plt.show()

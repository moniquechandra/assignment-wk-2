import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error

# a) Copy the following code 
np.random.seed(42)

x = np.random.uniform(0, 10, 200)
y = 2*x**2 - 5*x + 3 + np.random.normal(0, 10, 200)

# b) Split the data: Divide the dataset into a training set and a test set. 
trainValues = {"x": x[:80], "y": y[:80]}
testValues = {"x": x[80:], "y": y[80:]}

data_train = pd.DataFrame(trainValues)
data_test = pd.DataFrame(testValues)

# c) Plot the data and determine which relationship exists between the variables
plt.scatter(data_train["x"], data_train["y"])
plt.title("train data")
plt.show()
plt.scatter(data_test["x"], data_test["y"])
plt.title("test_data")
plt.show()

# According to the graphs, the relationship of the variables seems non-linear
# (also y involves a quadratic term: x**2),
# wW can conclude a polynomial linear regression model of degree 2 would fit the model the best, which is:
# a type of multiple regression analysis using polynomial terms.

# d) Train the model: fit the model to the training data
train_x = data_train["x"]
train_xsq = pd.DataFrame(data_train["x"]**2)
train_x_poly = pd.concat([train_x, train_xsq], axis= 1)

test_x = data_test["x"]
test_xsq = pd.DataFrame(data_test["x"]**2)
test_x_poly = pd.concat([test_x, test_xsq], axis= 1)

X = sm.add_constant(train_x_poly)
X_test = sm.add_constant(test_x_poly)

model = sm.OLS(data_train["y"], X)
results = model.fit()
pred_train_y = results.predict(X)
pred_test_y = results.predict(X_test)

# e) Evaluated the trained model by the R^2 and the MSE
r_squared_train = results.rsquared
r_squared_test = r2_score(data_test["y"], pred_test_y)
mse = mean_squared_error(data_test["y"], pred_test_y) 
rmse = mean_squared_error(data_test["y"], pred_test_y, squared=False) 

print(f"r_squared_train = {r_squared_train}, r_squared_test = {r_squared_test}, MSE = {mse}, RMSE = {rmse}")

# Refined and iterated!
# r_squared_train = 0.9563082036993829, r_squared_test = 0.9585208497542722,
# MSE = 90.76633960215689, RMSE = 9.527137009729465

# Shows that the model fits the testing set as well,
# and we are confident that we can use the model to predict future values!

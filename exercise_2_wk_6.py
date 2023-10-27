import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv('winequality-red.csv', delimiter=';', dtype=float)

# c) Handle any missing values or outliers
sum_null_data = df.isnull().any(axis = 1).sum()
if sum_null_data > 0:
    raise ValueError

df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

# d) Visualize the distributions of the wine quality ratings and
# the relationships between the attributes and the quality.

plt.hist(df['quality'], bins=20, color='red', alpha=0.5)
plt.show()



# No relationship between the attribute(s) and the quality.

#
# X = df['sum_of_attributes']  # Features (all columns except 'quality')
# y = df['quality']

# Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# plt.scatter(X_train, y_train)
# plt.show()
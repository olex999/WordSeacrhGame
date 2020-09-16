import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data = pd.read_csv("D:\\LEARNING\\DATA SCINECE\\wine\\winequality-red.csv");

# print(data.head())

# print(data.info())

# print(data.describe())

# print(data['fixed acidity'].median())

# a = data['fixed acidity'].plot(kind='density', figsize=(14,6))
# a.axvline(data['fixed acidity'].mean(), color='red')
# a.axvline(data['fixed acidity'].median(), color='blue')
# plt.show()

# x = data.iloc[:,:-1].values
# y = data.iloc[:,-1].values
#
# selected = SelectKBest(score_func=chi2).fit_transform(x,y)
# print(selected)

print(data[:1])
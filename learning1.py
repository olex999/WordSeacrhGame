import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
sns.set_style('darkgrid')

data = pd.read_csv("D:\LEARNING\DATA SCINECE\wine\winequality-red.csv")

#find a null data

# print(data.isnull().sum())

bins =(2,6.5,8)
lables = ['bad', 'good']
data["quality"] = pd.cut(x = data['quality'], bins = bins)

data['quality'].value_counts()

labaelencoder_y = LabelEncoder()
data['quality'] = labaelencoder_y.fit_transform(data['quality'])

# print(data.head())

cor = data.corr()

#for show some graphic of number
# fig, ax = plt.subplots(figsize=(10,8))
# sns.heatmap(cor, cmap='coolwarm', annot=True, fmt=".2f")
#
# plt.xticks(range(len(cor.columns)), cor.columns)
#
# plt.yticks(range(len(cor.columns)), cor.columns)
#
# plt.show()

# f, axes = plt.subplots(1,2,figsize=(14,4))
#
# sns.distplot(data['fixed acidity'], ax = axes[0])
# axes[0].set_xlabel('Fixed Acidity', fontsize=14)
# axes[0].set_ylabel('Count', fontsize=14)
# axes[0].yaxis.tick_left()
#
# sns.violinplot(x = 'quality', y = 'fixed acidity', data = data, hue = 'quality',ax = axes[1])
# axes[1].set_xlabel('Quality', fontsize=14)
# axes[1].set_ylabel('Fixed Acidity', fontsize=14)
# axes[1].yaxis.set_label_position("right")
# axes[1].yaxis.tick_right()
#
# plt.show()

X = data.drop('quality', axis= 1).values
Y = data['quality'].values.reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.2, random_state= 42)

sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.fit_transform(X_test)

classifier_lr = LogisticRegression(C=1, fit_intercept=True, max_iter=1000, penalty = 'l2', solver='liblinear')
classifier_lr.fit(X_train_scaled, Y_train.ravel())

cv_lr = cross_val_score(estimator = classifier_lr, X = X_train_scaled, y = Y_train.ravel(), cv = 108)
print("CV: ",cv_lr.mean())





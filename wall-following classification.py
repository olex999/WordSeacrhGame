import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

csv_data = pd.read_csv("D:\KULIAH\SMT6\BIGDATA\TGSAKHIR\sensor_readings_24.csv")

# print(csv_data.isnull().sum())

x = csv_data.iloc[:, :-1].values
y = csv_data.iloc[:, -1].values

n_data = len(x)
n_feature = len(x[0,:])

# z = np.zeros(n_data)
# for i in range(0, n_data):
#

score = []

f=4
n_neighbors = 3

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
Imputer = imputer.fit(x[:, 1:])
x[:, 1:] = Imputer.transform(x[:, 1:])

x_new = SelectKBest(score_func=chi2, k=f).fit_transform(x, y)
print(x_new)
# mengukur score setiap feature
a = csv_data.iloc[:, :-1]
b = csv_data.iloc[:, -1]
score_f = SelectKBest(score_func=chi2, k=24)
fit = score_f.fit(a, b)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(a.columns)
featureScore = pd.concat([dfcolumns, dfscores], axis=1)
featureScore.columns = ['specs', 'score']
feature_sc = featureScore.nlargest(24, 'score')

x_train, x_test, y_train, y_test = train_test_split(x_new, y, test_size=0.3, random_state=0)

sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)

knn = KNeighborsClassifier(n_neighbors,
                            weights='uniform',
                            algorithm='auto',
                            metric='manhattan')

knn.fit(x_train, y_train)

x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max),
                    np.arange(y_min, y_max))
print(xx)
print(yy)
y_pred = knn.predict(x_test)
hasil = metrics.accuracy_score(y_test, y_pred)

print(hasil)







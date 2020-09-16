import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

csv_data = pd.read_csv("D:\KULIAH\SMT6\BIGDATA\TGSAKHIR\sensor_readings_24.csv")

x = csv_data.iloc[:, :-1].values
y = csv_data.iloc[:, -1].values

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
Imputer = imputer.fit(x[:, 1:])
x[:, 1:] = Imputer.transform(x[:, 1:])

cor_list = []
for i in x.columns.tolist():
    cor = np.corrcoef(x[i], y)[0,1]
    cor_list.append(cor)
cor_list = [0 if np.isnan(i) else i for i in cor_list]
cor_feature = x.iloc[:,np.argsort(np.abs(cor_list))[-100:]].columns.tolist()
print(cor_feature)
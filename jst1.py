import pandas as pd
import numpy as np

n = 0.3

def standardize_data(df):
    for col in df.columns:
        datatype = df[col].dtypes

        if (datatype == 'float64') or (datatype == 'int64'):
            std = df[col].std()
            mean = df[col].mean()
            df[col] = (df[col] - mean) / std

    return df
def find_bobot(data_uji, feature, target ):
    bobot = []
    hasil = []
    benar = 0

    for i in range(feature):
        bobot_s = np.random.uniform()
        bobot.append(bobot_s)
    print(bobot)
    for i in data_uji.index:
        y = bobot[0]*1 + data_uji['Recency (months)'][i]*bobot[1] + data_uji['Frequency (times)'][i]*bobot[2] + data_uji['Monetary (c.c. blood)'][i]*bobot[3] + data_uji['Time (months)'][i]*bobot[4]

        if y >= 0:
            hasil.append(1)
        else:
            hasil.append(0)

        if hasil[i] != target[i]:
            bobot[0] = bobot[0] + (n*(target[i]-hasil[i])*1)
            bobot[1] = bobot[1] + (n*(target[i]-hasil[i])*data_uji['Recency (months)'][i])
            bobot[2] = bobot[2] + (n*(target[i]-hasil[i])*data_uji['Frequency (times)'][i])
            bobot[3] = bobot[3] + (n * (target[i] - hasil[i]) * data_uji['Monetary (c.c. blood)'][i])
            bobot[4] = bobot[4] + (n * (target[i] - hasil[i]) * data_uji['Time (months)'][i])
        else:
            benar+=1
    return hasil

data = pd.read_excel("D:\\KULIAH\\SMT6\\PENGENALAN POLA\\tgs7\\transfusion_data.xlsx", sheet_name='testing')
data_uji = data[['Recency (months)','Frequency (times)','Monetary (c.c. blood)','Time (months)']]
target = data['whether he/she donated blood in March 2007']

dt = standardize_data(data_uji)
feature = len(data_uji.columns) + 1

ws = find_bobot(data_uji, feature, target)

correct = 0
wrong = 0

for i in range(len(data_uji.index)):
    result_outcome = ws

    if(result_outcome[i] == target[i]):
        correct +=1
    else:
        wrong +=1

print("Correct: "+str(correct))
print("wrong: "+str(wrong))
print("Akurasi: "+str(round(100*(correct/(correct+wrong))))+"%")
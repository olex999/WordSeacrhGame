import pandas as pd
import numpy as np

n = 0.2

def standardize_df(df):
    for col in df[['Recency (months)','Frequency (times)','Monetary (c.c. blood)','Time (months)']]:
        datatype = df[col].dtypes

        if (datatype == 'float64') or (datatype == 'int64'):
            std = df[col].std()
            mean = df[col].mean()
            df[col] = (df[col] - mean) / std

    return df


def update_weights(weights, d, point):
    point[len(point) - 1] = 1

    for i in range(len(weights)):
        weights[i] = n * d * point[i]

    return weights


def predict_outcome(weights, point):
    point[len(point) - 1] = 1
    result = np.dot(weights, point)

    if result > 0:
        return 1
    else:
        return -1

def find_best_hyperplane(weights, repetitions, df):
    for k in range(repetitions):
        for i, row in df.iterrows():
            outcome = row['whether he/she donated blood in March 2007']
            point = row.values
            predicted_outcome = predict_outcome(weights, point)
            if predicted_outcome != outcome:
                weights = update_weights(weights, outcome, point)

    return weights

df = pd.read_excel("D:\\KULIAH\\SMT6\\PENGENALAN POLA\\tgs7\\transfusion_data.xlsx", sheet_name='training')
print(df)
ds = df.loc[:, ('No')]
print(ds)
df = standardize_df(ds)
traindf = pd.concat([df.iloc[:300], df.iloc[400:500]]).sample(frac = 1).reset_index(drop = True)
testdf = pd.concat([df.iloc[300:400], df.iloc[500:]]).sample(frac = 1).reset_index(drop = True)

# print(traindf)
# print(testdf)
# ws = [0]*len(df.columns)
# print(ws)
# ws = find_best_hyperplane(ws, 15, traindf)
# print(ws)
#
# correct = 0
# wrong = 0
#
# for i in range(len(testdf.index)):
#     algorithm_outcome = predict_outcome(ws, testdf.iloc[i].values)
#     real_outcome = testdf.iloc[i]['whether he/she donated blood in March 2007']
#
#     if (algorithm_outcome == real_outcome):
#         correct += 1
#     else:
#         wrong += 1
#
#
# print('Total: '+str(correct+wrong))
# print('Correct: '+str(correct))
# print('Wrong: '+str(wrong)+'\n')
# print('Accuracy: '+str(round(100*(correct/(correct+wrong))))+'%')
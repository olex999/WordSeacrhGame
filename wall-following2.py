import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
csv_data = pd.read_csv("D:\KULIAH\SMT6\BIGDATA\TGSAKHIR\sensor_readings_24.csv", delimiter=',', dtype=np.str)

raw_data = csv_data.iloc(csv_data[:,:24], dtype=np.float).values
raw_data = pd.concat([raw_data, pd.DataFrame(csv_data[:, 24], columns=['Label'])], axis=1)

# fig = plt.figure(figsize=(15,5))
# ax = sns.countplot(x='Label',data=csv_data,alpha=0.5)
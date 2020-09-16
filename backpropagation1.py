import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt


csv_data = pd.read_excel("D:\\KULIAH\\SMT6\\PENGENALAN POLA\\tgs7\\transfusion_data.xlsx",sheet_name='testing')
data = csv_data[['Recency (months)','Frequency (times)','Monetary (c.c. blood)','Time (months)']]
target = csv_data['whether he/she donated blood in March 2007']
x = np.array(data)
x = x.astype(float)
n_data = len(x[:,0])
n_feature = len(x[0,:])

rasio_data_latih = 0.7
n_input = n_feature
n_hidden = 3
n_output = 1
n_epoch = 240
alfa = 0.2

n_data_latih = int(n_data * rasio_data_latih)
data_latih = x[:n_data_latih,:]

data_uji = x[n_data_latih:,:]
n_data_uji = len(data_uji[:,0])

#normalisasi data
for i in range(n_feature ):
    data_latih[:,i] = 0.1 + ((data_latih[:,i] - min(data_latih[:,i]))/ (max(data_latih[:,i]) - min(data_latih[:,i]))) * 0.8

for i in range(n_feature):
    data_uji[:,i] = 0.1 + ((data_uji[:,i] - min(data_uji[:,i]))/ (max(data_uji[:,i]) - min(data_uji[:,i]))) * 0.8
target_latih = []
target_uji = []
for i in range(n_data_latih):
    target_latih.append(target[i])

for i  in range(n_data_latih,n_data):
    target_uji.append(target[i])

#inisialisasi bobot
v = np.random.rand(n_hidden,n_input) #* 2 - 1
b1 = np.random.rand(n_hidden) #* 2 - 1
w = np.random.rand(n_output, n_hidden) #* 2 - 1
b2 = np.random.rand(n_output) #* 2 - 1
# v = np.array(v_new)
# b1 = np.array(b1_new)
# w = np.array(w_new)
# b2 = np.array(b2_new)
print(v)
print(b1)
print(w)
print(b2)

itr = 0

MSE = np.zeros(n_epoch +1)
while(itr <= n_epoch):


    for idx_data in range(0, n_data_latih):
        label = data_latih[idx_data,0]
        feature = data_latih[idx_data,0:]
        target = target_latih[idx_data]

        #hitung nilai pada hidden layer
        z = np.zeros(n_hidden)
        for i in range(0, n_hidden):
            z_in = b1[i] + np.sum(feature * v[i])
            z[i] = 1/(1 + math.exp(-z_in))

        # hitung nilai pada output layer
        y = np.zeros(n_output)
        for i in range(0,n_output):
            y_in = np.sum(z * w[i]) + b2[i]
            y[i] = 1/(1 + math.exp(-y_in))

        # hitung Jumlah error
        error = target - y
        sum_error = sum(error**2)

        # hitung faktor koreksi pada output layer
        f_output = np.zeros(n_output)
        for i in range(0,n_output):
            f_output[i] = error * (y[i] * (1 - y[i]))

        # hitung perbaikan bobot antara output dan hidden layer
        delta_w = np.zeros(shape=(n_output,n_hidden))
        for i in range(0, n_output):
            delta_w[i,:] = alfa * f_output[i] * z

        # hitung perbaikan bobot BIAS (b2) antara output dan hidden layer
        delta_b2 = np.zeros(n_output)
        for i in range(0,n_output):
            delta_b2[i] = alfa * f_output[i] * 1

        # hitung faktor koreksi pada hidden layer
        f_hidden = np.zeros(n_hidden)
        for i in range(0,n_hidden):
            f_net = np.sum(delta_b2*w[:,i])

            f_hidden[i] = f_net * (z[i] * (1 - z[i]))

        # hitung perbaikan bobot antara hidden dan input layer
        delta_v = np.zeros(shape=(n_hidden,n_input))
        for i in range(n_hidden):
            delta_v = alfa * f_hidden[i] * feature

        # hitung perbaikan bobot antara hidden dan input layer
        delta_b1 = np.zeros(n_hidden)
        for i in range(n_hidden):
            delta_b1 = alfa * f_hidden[i]

        # update semua bobot
        v = v + delta_v
        b1 = b1 + delta_b1
        w = w + delta_w
        b2 = b2 + delta_b2

    MSE[itr] = sum_error / n_data_latih
    print("Epoch ke-"+str(itr)+"   error: "+str(MSE[itr]))
    itr +=1
# print(v)
# print(b1)
# print(w)
# print(b2)

print("Mean Squared Error: "+str(MSE[n_epoch]))

output_benar = 0
for idx_data in range(0, n_data_uji):
    label = data_uji[idx_data, 0]
    feature = data_uji[idx_data, 0:]
    target = target_uji[idx_data]
    # hitung nilai pada hidden layer
    z = np.zeros(n_hidden)
    for i in range(0, n_hidden):
        net = np.sum(feature * v[i]) + b1[i]
        z[i] = 1 / (1 + math.exp(-net))

    # hitung nilai pada output layer
    y = np.zeros(n_output)
    f_output = np.zeros(n_output)
    for i in range(0, n_output):
        net = np.sum(z * w[i]) + b2[i]
        y[i] = 1 / (1 + math.exp(-net))

        # pembulatan y[i] ke 0 atau 1
        if (y[i] >= 0.5):
            y[i] = 1
        else:
            y[i] = 0

    # bandingkan output MLP dengan label dengan teknik ONE HOT ENCODING
    if (y == target):
        output_benar += 1
    # end for

# hitung Akurasi MLP
akurasi = output_benar / n_data_uji
print("Akurasi MLP training: " + str(akurasi))

plt.title("Mean Squared Error hasil training")
plt.plot(MSE)
plt.autoscale(enable=True, axis='both', tight=None)
plt.show(block=True)

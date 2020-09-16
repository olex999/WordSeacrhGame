import math
import sys
# sys.setrecursionlimit(1000000)
data = [0,0,0,1,1,0,1,1]
target = [0,1,1,1]

laju_belajar = 0.01
n = 1
aV01 = 1.718946
aV11 = -1.263178
aV21 = -1.083092
aW01 = -0.54118
aW11 = 0.54396
J_error = 0.1


def MeanSuareError(V01,V11,V21,W01,W11):
    iterasi = 1
    z_in = []
    y_in = []
    z_i = []
    y_i = []
    j,k = 0,1

    for i in range(4):
        z = V01 + ((data[j] * V11) + (data[k] * V21))
        z_ij = 1 / (1 + (1/(math.exp(z*n))))
        y = W01 + (z_ij * W11)
        y_ij = 1 / (1 + (1/(math.exp(y*n))))
        z_in.append(z)
        y_in.append(y)
        z_i.append(z_ij)
        y_i.append(y_ij)
        j+=2
        k+=2

    if Error(y_i) > J_error:
        iterasi+=1
        bobot_new(z_in,y_in,z_i,y_i)
        MeanSuareError(aV01,aV11,aV21,aW01,aW11)
    else:
        print(iterasi)


def Error(y_i):
    error = 0
    er = 0
    for i in range(len(target)):
        er = (target[i]-y_i[i])**2
        error += er
    return error*0.25

def bobot_new(z_in, y_in,z_i,y_i):
    a, b, c, d, e = aV01, aV11, aV21, aW01, aW11
    j,k = 1,2
    for i in range(len(target)):

        sw,sv = 0,0

        sw = (target[i]-y_i[i]) * ((n*y_in[i])*(1-y_in[i]))
        delta_w11 = laju_belajar*sw*z_i[i]
        delta_w01 = laju_belajar*sw

        sv = delta_w01*e
        sv = float(sv)
        sv = sv* ((n*z_in[i])*(1-z_in[i]))
        delta_v11 = laju_belajar*sv*data[j]
        delta_v21 = laju_belajar*sv*data[k]
        delta_v01 = laju_belajar*sv

        a = a+delta_v01
        b = b+delta_v11
        c = c+delta_v21
        d = d+delta_w01
        e = e+delta_w11
    MeanSuareError(a,b,c,d,e)







    # print(aV01)
    # print(aV11)
    # print(aV21)
    # print(aW01)
    # print(aW11)



# print(aV01)
MeanSuareError(aV01,aV11,aV21,aW01,aW11)
# print(hasil)
# ahasil = Error(hasil)
# print(ahasil)
# print(aV01)

# a = [1,2,3,4,5]
# print(a[len(a)-1:])
# a.append(6)
# print(a[len(a)-1:])

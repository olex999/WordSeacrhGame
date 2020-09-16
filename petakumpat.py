import numpy as np
import pandas as pd

dataPetak = pd.read_csv('D:\LEARNING\PETAKUMPET\macammacamtakjil.csv')
petak = np.array(dataPetak)

print("Word Search by Bena Kribo \n(Macam-Macam Takjil Edition)")
kata = ['BUBURSUMSUM','MARJAN', 'CINCAUSUSU','MENDOAN','ESBUAH','RISOLES','GORENGAN','SIRUP','KOLAKPISANG','TEHMANIS','KURMA','TIMUNSURI']

for i in range(len(kata)):
    print(i+1,".",kata[i])
print("=======================")
kata = input("Input The Word: ")
print("=======================\n")
cari = kata.upper()

length = len(petak) -1
length_cari = len(cari) -1
jawab = []
column = []
rows = []
goal = 0
i = 0
j = 0
f = 0
a  = len(cari)

def DiagonalKiriAtas(k, l, length):
    i = k
    j = l
    a = length
    for x in range(a):
        if((petak[(i-x), (j-x)]) == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j - x)
            rows.append(i- x)
        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break
    return f


def LurusAtas(k, l, length):
    a = length
    i = k
    j = l
    for x in range(a):
        if (petak[(i - x), j] == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j)
            rows.append(i - x)

        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break
    return f

def DiagonalKananAtas(k, l, length):
    i = k
    j = l
    a = length
    for x in range(a):
        if(petak[(i-x), (j+x)] == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j + x)
            rows.append(i- x)
        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break
    return f


def LurusKiri(k, l, length):
    i = k
    j = l
    a = length
    for x in range(a):
        if (petak[i, (j - x)] == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j - x)
            rows.append(i)
        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()

            break
    return f

def LurusKanan(i, j, a):
    for x in range(a):
        if (petak[i, (j + x)] == cari[x]):
            f =1
            jawab.append(cari[x])
            column.append(j+x)
            rows.append(i)
        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break
    return f

def DiagonalKananBawah(i, j, a):
    f = 0
    for x in range(a):
        if(petak[(i+x), (j+x)] == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j + x)
            rows.append(i+x)
        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break
    return f

def DiagonalKiriBawah(i, j, a):
    for x in range(a):
        if((petak[(i+x), (j-x)]) == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j - x)
            rows.append(i+x)
        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break
    return f


def LurusBawah(k, l, length):
    a = length
    i = k
    j = l
    f = 0
    for x in range(a):
        if (petak[(i + x), j] == cari[x]):
            f = 1
            jawab.append(cari[x])
            column.append(j)
            rows.append(i+x)

        else:
            f = 0
            jawab.clear()
            column.clear()
            rows.clear()
            break

    return f

while (goal != 1):
    if (j <= length and i <= length):
        if (petak[i, j] == cari[0]):
            if ((j + length_cari) <= length):
                goal = LurusKanan(i, j, a)
                if goal == 1:
                    print("Lurus Kanan")
                    break
            if (((i - length_cari) <= length) and ((j + length_cari) <= length)):
                goal = DiagonalKananAtas(i, j, a)
                if goal == 1:
                    print("Diagonal Kanan Atas")
                    break
            if ((i - length_cari) >= length_cari):
                goal = LurusAtas(i, j, a)
                if goal == 1:
                    print("Lurus Atas")
                    break
            if (((i - length_cari) >= length_cari) and ((j - length_cari) >= length_cari)):
                goal = DiagonalKiriAtas(i, j, a)
                if goal == 1:
                    print("Diagonal Kiri Atas")
                    break
            if ((j - length_cari) >= length_cari):
                goal = LurusKiri(i, j, a)
                if goal == 1:
                    print("Lurus Kiri")
                    break
            if (((i + length_cari) <= length) and ((j - length_cari) <= length)):
                goal = DiagonalKiriBawah(i, j, a)
                if goal == 1:
                    print("Diagonal Kiri Bawah")
                    break
            if ((i + length_cari) <= length):
                goal = LurusBawah(i, j, a)
                if goal == 1:
                    print("Lurus Bawah")
                    break
            if (((i + length_cari) <= length) and ((j + length_cari) <= length)):
                goal = DiagonalKananBawah(i, j, a)
                if goal == 1:
                    print("Diagonal Kanan Bawah")
                    break
            j +=1
        else:
            j += 1
    else:
        j=0
        i+=1

print(jawab)
print("koordinat kolom: ",column)
print("koordinat baris: ",rows)
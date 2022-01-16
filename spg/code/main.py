import numpy as np
import spg
import matplotlib.pyplot as plt
import os

path = os.getcwd()
path = os.path.join(path,"spg/code/data.txt")
#print(path)
f = open(path,"r")   #设置文件对象
data = f.readlines()  #直接将文件中按行读到list里，效果与方法2一样
f.close()             #关闭文件

N = int(data[0][0]) #number of transistor
M = int(data[1][0]) #number of net
pmos_net = []
for i in range(2,2+int(N/2)) :
    c = []
    c.append(int(data[i][0]))
    c.append(int(data[i][2]))
    c.append(data[i][4])
    pmos_net.append(c)

nmos_net = []
for i in range(2+int(N/2),2+N) :
    c = []
    c.append(int(data[i][0]))
    c.append(int(data[i][2]))
    c.append(data[i][4])
    nmos_net.append(c)
outcome, expression = spg.Spg(N,M,pmos_net,nmos_net)
print(outcome)
print(expression)
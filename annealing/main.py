import numpy as np
import annealing
import matplotlib.pyplot as plt
import os

path = os.getcwd()
path = os.path.join(path,"annealing/data.txt")
#print(path)
f = open(path,"r")   #设置文件对象
data = f.readlines()  #直接将文件中按行读到list里，效果与方法2一样
f.close()             #关闭文件

L = int(data[0][0])
W = int(data[1][0])
M = int(data[2][0]) #number of cell
N = int(data[3][0]) #number of net

grid = np.zeros([L,W])
connections = []

for i in range(5,5+N) :
    c = []
    c.append(int(data[i][0]))
    j = 2;
    while(data[i][j] != "\n" ) :
        if(data[i][j] != " "):
            c.append(int(data[i][j]))
        j = j + 1
    connections.append(c)

#print(connections)
# print(grid)
grid, cost,storedcost,mincost,mingrid,storedp = annealing.Annealing(L, W, M, N, grid, connections)

print("final grid\n",grid)
print("final cost",cost)
print("mingrid\n",mingrid)
print("mincost",mincost)


plt.plot(storedcost, c = 'blue',label = "cost")
plt.title("Cost through times")
plt.xlabel('times')
plt.ylabel('Cost')
plt.show()


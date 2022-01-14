from hashlib import algorithms_available
import random
import math
import numpy as np
import copy

def Initialize(L, W, M,grid):
    pos = []    #position list
    for element in range(1,M+1):
        assigned = False
        while(not assigned):
            i = np.random.randint(L)
            j = np.random.randint(W)
            if(grid[i][j]==0):
                grid[i][j] = element
                assigned = True
                pos.append([i,j])
    return grid,pos

def Cost(pos, connections,size):
    cost = 0
    max_x = 0
    max_y = 0
    min_x = size
    min_y = size
    for i in connections:
        for j in i:
            #print(j)
            [x,y] = pos[j-1]
            if(x>max_x):
                max_x = x
            if(x<min_x):
                min_x = x
            if(y>max_y):
                max_y = y
            if(y<min_y):
                min_y = y
        cost = cost + max_x +max_y - min_x - min_y
    return cost
def NeighborState (pos,grid,M):
    # We will follow these two protocols, each 50% of time
	# 1. swap positions of any two elements
	# 2. Move any element to a new position in the grid
    tempGrid = copy.deepcopy(grid)
    temppos = copy.deepcopy(pos)
    if(np.random.random()<0.5):
        element1 = np.random.randint(0, M)
        element2 = np.random.randint(0, M)
                # to ensure element2 != element1 
        while(element2==element1):
            element2 = np.random.randint(0, M)
        [x1,y1] = temppos[element1]
        [x2,y2] = temppos[element2]
        tempGrid[x1][y1] = element2+1
        tempGrid[x2][y2] = element1+1
        temppos[element1] = [x2,y2]
        temppos[element2] = [x1,y1]
    else:
        element1 = np.random.randint(0, M)
        [x1,y1] = temppos[element1]
        # find an empty place
        empty = np.where(tempGrid == 0)
        num = empty[0].size
        ran = np.random.randint(0, num)
        x2 = empty[0][ran]
        y2 = empty[1][ran]
        tempGrid[x1][y1] = 0
        tempGrid[x2][y2] = element1	+1	
        temppos[element1] = [x2,y2]
    return temppos,tempGrid

def Annealing(L, W, M, N, grid, connections):
    grid,pos = Initialize(L, W, M,grid)
    # print(pos)
    size = max(L,W)
    cost = Cost(pos, connections,size)
    print("initial grid\n",grid)
    print("initial cost",cost)
    
    storedcost = [cost]
    mincost = 100
    mingrid = copy.deepcopy(grid)
    storedp = []
    # start the algorithm
    T = 10000
    threshold = 0.01
    alpha = 0.99
    while(T>threshold):
        temppos,tempgrid = NeighborState(pos,grid,M)
        tempcost = Cost(temppos, connections,size)
        delta = tempcost - cost
        if(delta < 0):
            grid = tempgrid
            pos = temppos
            cost = tempcost
        else:
            p = np.exp(-delta / T)
            if(np.random.random()<p):
                grid = tempgrid
                pos = temppos
                cost = tempcost
        if(tempcost<mincost):
            mincost = tempcost
            mingrid = tempgrid
        T = T*alpha
        # print(cost)
        storedcost.append(cost)
        p = np.exp(-delta / T)
        storedp.append(p)

    return grid, cost,storedcost,mincost,mingrid,storedp
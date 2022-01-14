import numpy as np
import matplotlib.pyplot as plt

T = 10000
tem = [T]

for i in range (0,1500):
    T = T*0.99
    tem.append(T)

plt.plot(tem, c = "red",label = "T")
plt.title("Temperature through times")
plt.xlabel('times')
plt.ylabel('T')
plt.show()

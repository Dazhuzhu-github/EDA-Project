import numpy as np
import matplotlib.pyplot as plt
from treelib import Tree, Node
# T = 10000
# tem = [T]

# for i in range (0,1500):
#     T = T*0.99
#     tem.append(T)

# plt.plot(tem, c = "red",label = "T")
# plt.title("Temperature through times")
# plt.xlabel('times')
# plt.ylabel('T')
# plt.show()
from treelib import Tree

tree = Tree()
tree.create_node(1, 1)  # 根节点
tree.create_node(2, 2, parent=1)
tree.create_node(3, 3, parent=1)
tree.create_node(7, 7, parent=2)
tree.create_node(6, 6, parent=2)
tree.create_node(5, 5, parent=3)
tree.create_node(4, 4, parent=3)
tree.show()  # 可能和创建顺序不同

print([tree[node].tag for node in tree.expand_tree(mode=Tree.DEPTH, sorting=False)])  # 前序遍历：根 → 左 → 右
# [1, 2, 7, 6, 3, 5, 4]

print([tree[node].tag for node in tree.expand_tree(mode=Tree.WIDTH, sorting=False)])  # 层序遍历：逐层从左到右
# [1, 2, 3, 7, 6, 5, 4]

print([tree[node].tag for node in tree.expand_tree(mode=Tree.ZIGZAG, sorting=False)])  # 锯齿层序遍历：从左到右再从右到左
# [1, 3, 2, 7, 6, 5, 4]

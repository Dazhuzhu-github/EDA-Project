from treelib import Tree, Node

def BuildTree(net):
    # build the tree 
    # # let 11 = 并联
    # bing = 11
    # # let 22 = 串联
    # chuan = 22
    tree = Tree()
    flag = 0
    for i in net:
        if(flag == 0):
            if(i[0]== 1 or i[0]==2):
                tree.create_node(identifier = i[0], data = i[2])
                tree.create_node(identifier = i[1], parent = i[0],data = i[2])
                flag = 1
        else:
            tree.create_node(identifier = i[1], parent = i[0], data = i[2])
    tree.show()
    return tree

def Expression(pmos_tree):
    expression = ""
    # 使用前序遍历
    expression = [pmos_tree[node].tag for node in pmos_tree.expand_tree(mode=Tree.DEPTH, sorting=False)]
    return expression
 
def Spg(N,M,pmos_net,nmos_net):
    outcome = True
    expression = ""
    nmos_tree = BuildTree(nmos_net)
    pmos_tree = BuildTree(pmos_net)
    # judge the tree
    if(nmos_tree.to_dict() != pmos_tree.to_dict()):
        outcome = False
    # expression
    if (outcome == True):
        expression = Expression(pmos_tree)

    return outcome, expression

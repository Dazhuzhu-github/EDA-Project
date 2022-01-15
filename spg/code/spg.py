from treelib import Tree, Node

def BuildTree():
    # build the tree 
    tree = Tree()
    tree.show()
    print(tree.identifier)
    return tree


def Spg(N,M,net):
    outcome = True
    expression = ""
    nmos_tree = BuildTree(net)
    pmos_tree = BuildTree(net)
    # judge the tree
    return outcome, expression

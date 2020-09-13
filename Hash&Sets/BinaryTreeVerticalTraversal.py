class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def vert(node, mini, maxi, pos):
    if node is None:
        return 
    if pos<mini[0]:
        mini[0] = pos
    if pos>maxi[0]:
        maxi[0] = pos
    vert(node.left, mini, maxi, pos-1)
    vert(node.right, mini, maxi, pos+1)

def printVert(node, i, pos):
    if node == None:
        return
    if i==pos:
        print(node.data, end = " ")
    printVert(node.left, i, pos-1)
    printVert(node.right, i,pos+1)

def findVert(root):
    mini = [0]
    maxi = [0]
    vert(root, mini, maxi, 0)
    for i in range(mini[0], maxi[0]+1):
        printVert(root, i, 0)
        print("")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 
findVert(root)
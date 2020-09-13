from collections import defaultdict
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def vert(node, m, pos):
    if node is None:
        return 
    m[pos].append(node.data)
    vert(node.left, m, pos-1)
    vert(node.right, m, pos+1)


def findVert(root):
    m = defaultdict(list)
    vert(root, m, 0)
    for i, j in enumerate(sorted(m)):
        for k in m[j]:
            print(k, end =" ")
        print("")

    # for i in range(mini[0], maxi[0]+1):
    #     printVert(root, i, 0)
    #     print("")



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
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertfront(self, val):
        cur = Node(val)
        cur.next = self.head
        self.head = cur
    def sortn(self, n):
        temp = self.head
        small = LinkedList()
        large = LinkedList()
        while temp:
            p = temp.data
            print(type(p))
            if temp.data<n:

                small.insertfront(temp.data)
            else:
                large.insertfront(temp.data)
            temp = temp.next
        temp = small.head
        while temp.next:
            temp = temp.next
        temp.next = large.head
        small.printL()

l = LinkedList()
l.insertfront(2)
l.insertfront(5)
l.insertfront(4)
l.insertfront(3)
l.insertfront(6)
l.insertfront(1)
l.printL()
l.sortn(4)
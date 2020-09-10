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
    def findMid(self):
        mainptr = self.head
        tempptr = self.head
        while tempptr and tempptr.next:
            mainptr = mainptr.next
            tempptr = tempptr.next.next
        print(mainptr.data)
        return
l = LinkedList()
# l.insertfront(6)
l.insertfront(5)
l.insertfront(4)
l.insertfront(3)
l.insertfront(2)
l.insertfront(1)
l.printL()
l.findMid()
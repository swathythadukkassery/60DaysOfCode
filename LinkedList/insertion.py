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
    def insertend(self, val):
        cur = Node(val)
        temp = self.head
        if temp == None:
            self.head = cur
        else:
            while(temp.next!=None):
                temp = temp.next
            temp.next = cur
    def insertMid(self, val, dat):
        cur = Node(dat)
        temp = self.head
        while temp and temp.data!=val:
            temp = temp.next
        if temp == None:
            print("np")
        else:
            temp2 = temp.next
            temp.next = cur
            
l = LinkedList()
l.head = Node(1)
sec = Node(2)
l.head.next = sec
third = Node(3)
sec.next = third
l.insertfront(4)
l.insertend(5)
l.insertMid(1, 9)
l.printL()
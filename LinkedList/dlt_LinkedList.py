class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printL(self):
        temp = self.head
        print(temp)
        if temp==None:
            return
        while(temp):
            print(temp.data)
            temp = temp.next
    def dltlist(self):
        temp = self.head
        while temp:
            nxt = temp.next
            del temp.data
            temp = nxt
        self.head = None
        

l = LinkedList()
l.head = Node(1)
sec = Node(2)
l.head.next = sec
third = Node(3)
sec.next = third
f = Node(4)
third.next = f

l.printL()
l.dltlist()
l.printL()       
        

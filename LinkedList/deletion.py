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
    def dltKey(self, key):
        temp = self.head
        if temp.data == key:
            self.head = temp.next
        else:
            while(temp.next and temp.next.data != key):
                temp = temp.next
            if temp.next!=None and temp.next.data == key:
                temp.next = temp.next.next
            else:
                print("NP")
    def dltKeyPos(self, pos):
        temp = self.head
        if temp == None:
            print("Np")
        elif pos == 1:
            self.head = temp.next
        else:
            for i in range(pos-2):
                temp = temp.next
                if temp == None:
                    return
            temp.next = temp.next.next

l = LinkedList()
l.head = Node(1)
sec = Node(2)
l.head.next = sec
third = Node(3)
sec.next = third
f = Node(4)
third.next = f
l.dltKey(1)
l.printL()
l.dltKeyPos(3)
l.printL()       
        

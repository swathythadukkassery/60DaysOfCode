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
l = LinkedList()
l.head = Node(1)
sec = Node(2)
l.head.next = sec
third = Node(3)
sec.next = third
l.printL()
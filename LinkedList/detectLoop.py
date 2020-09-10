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
    def detectLoop(self):
        s=set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next



l = LinkedList()
# l.insertfront(6)
l.insertfront(5)
l.insertfront(4)
l.insertfront(3)
l.insertfront(2)
l.insertfront(1)
l.printL()
res = l.detectLoop()
if res == True:
    print("Loop exist")
else:
    print("There is no loop")
l.head.next.next.next = l.head # created a loop
res = l.detectLoop()
if res == True:
    print("Loop exist")
else:
    print("There is no loop")
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
            

l = LinkedList()
l.insertfront(7)
# l.insertfront(1)
l.insertfront(6)
m = LinkedList()
m.insertfront(5)
m.insertfront(9)
m.insertfront(2)
l.printL()
m.printL()
count = 0
res = 0
cur = 0
c = 0
templ = l.head
tempm = m.head
while templ and tempm:

    cur = count + templ.data + tempm.data
    count = 0
    if templ.next == None or templ == None:
        res+= pow(10,c)*cur
    elif cur >9:
        count = int(cur/10)
        res+= pow(10,c)*(cur%10)
    else:
        res+= pow(10,c)*cur
    c+=1
    
    templ = templ.next
    tempm = tempm.next
while templ:
    res+= pow(10,c)*templ.data
    templ = templ.next
    c+=1
while tempm:
    res+= pow(10,c)*tempm.data
    tempm = tempm.next
    c+=1
print(res)

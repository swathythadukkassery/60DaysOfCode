class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    def push(self, val):
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1.append(val)
        while self.q2:
            self.q1.append(self.q2.pop(0))
        print(self.q1)
    def pop(self):
        self.q1.pop(0)
        print(self.q1)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
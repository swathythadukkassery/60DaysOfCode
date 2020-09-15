class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def en(self, val):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(val)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        print(self.stack1)
    def de(self):
        if self.stack1:
            self.stack1.pop()
        print(self.stack1)
q = Queue()
q.en(1)
q.en(2)
q.en(3)
q.de()
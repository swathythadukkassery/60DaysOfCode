class Stacks:
    def __init__(self, n):
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n
        self.size = n
    def push1(self, val):
        if self.top1 < self.top2-1:
            self.top1+=1
            self.arr[self.top1] = val
            print(self.arr)
        else:
            print("Stack Overflow")
    def push2(self, val):
        if self.top1 < self.top2-1:
            self.top2-=1
            self.arr[self.top2] = val
            print(self.arr)
        else:
            print("Stack Overflow")
    def pop1(self):
        if self.top1!=-1:
            self.arr.pop(self.top1)
            self.top1-=1
            print(self.arr)
        else:
            print("Stack underflow")
    def pop2(self):
        if self.top2!=n:
            self.arr.pop(self.top2)
            self.top2+=1
            print(self.arr)
        else:
            print("Stack underflow")

ss = Stacks(5)
ss.push1(1)
ss.push2(2)
ss.push1(3)
ss.push2(4)
ss.push1(5)
ss.pop1()
ss.push2(6)
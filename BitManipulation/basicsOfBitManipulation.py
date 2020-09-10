# index=int(input())
# num=int(input())
# # test
# mask = 1<<index
# print(mask)
# print(num & mask)

class BasicBits():
    def __init__(self, num):
        self.num = num
    def setBit(self,index_set):    
        mask_set=1<<index_set
        print(self.num | mask_set)

    def getBit(self, index_get):
        mask_get = 1<<index_get
        print(self.num & mask_get, "io")

    def clearBit(self, index_clear):
        mask_clear=~(1<<index_clear)
        print(self.num & mask_clear)

    def toggleBit(self, index_toggle):
        mask_set = 1<<index_toggle
        print(self.num ^ mask_set)

    def checkSingleBit(self):
        if self.num!=0:  
            if self.num & self.num-1 == 0:
                print(True)
            else:
                print(False)

n=int(input())
b1= BasicBits(n)
p=int(input())
b1.setBit(p)
b1.getBit(p)
b1.clearBit(p)
b1.toggleBit(p)
b1.checkSingleBit()

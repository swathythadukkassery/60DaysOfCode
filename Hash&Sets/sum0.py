NumList = list(map(int, input().split()))
mydict = {}
cursum = 0
maxlen = 0
for i in range(len(NumList)):
    if NumList[i] == 0 and maxlen == 0:
        maxlen = 1
    cursum+=NumList[i]
    if cursum==0:
        maxlen = i+1
    if cursum in mydict:
        maxlen = max(maxlen, i-mydict[cursum])
    else:
        mydict[cursum] = i
print(maxlen)
    
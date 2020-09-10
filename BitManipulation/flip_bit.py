num=int(input())
if ~num==0:
    print(8*sizeof())
else:
    curlen=0
    maxlen=0
    prevlen=0
    while num!=0:
        if num & 1 == 1:
            
            curlen += 1
        else:
            prevlen = 0 if num&2==0 else curlen
            curlen=0
        num>>=1
        maxlen = max(curlen+prevlen, maxlen)
print(maxlen+1)
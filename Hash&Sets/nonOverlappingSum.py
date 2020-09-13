from collections import defaultdict
set1 = list(map(int, input().split()))
set2 = list(map(int, input().split()))
count = defaultdict(lambda :0)
res = 0
for i in range(len(set1)):
    
    count[set1[i]]+=1
    res+=set1[i]
for i in range(len(set2)):
    if count[set2[i]]:
        res-=set2[i]
        count[set2[i]]-=1
    else:
        res+=set2[i]
print(res)
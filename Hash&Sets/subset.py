from collections import Counter
mainArr = list(map(int, input().split()))
subArray = list(map(int, input().split()))
c = Counter(mainArr)
flag = 1
for i in subArray:
    if c[i]>0:
        c[i]-=1
    else:
        print("NO")
        flag = 0
        break
if flag == 1:
    print("Yes")
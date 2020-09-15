from collections import defaultdict
arr = list(map(int, input().split()))
pos = defaultdict(list)
maxi = 0
m = arr[0]
for i in range(len(arr)):
    if arr[i] in pos:
        pos[arr[i]][0]+=1
        pos[arr[i]][1]=i
        if pos[arr[i]][0]>maxi:
            maxi = pos[arr[i]][0]
            m = arr[i]
    else:
        pos[arr[i]] = [1,i,i]
print(arr[pos[m][2]:pos[m][1]+1])

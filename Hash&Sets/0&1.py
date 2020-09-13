li = list(map(int, input().split()))
m = max(li) + 2
d = dict.fromkeys(li, 0)
eq, low, grt = 1, 1, 1
for i in range(len(li)):
    if li[i] in d:
        eq = 1 + d[li[i]]
    if li[i]-1 in d:
        low = 1 + d[li[i]-1]
    if li[i]+1 in d:
        grt = 1 + d[li[i]+1]
    d[li[i]] = max(eq, low, grt)
    eq, low, grt = 1, 1, 1

print (max(d.values()))
        

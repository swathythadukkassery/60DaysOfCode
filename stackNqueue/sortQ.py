
q1 = list(map(int, input().split()))
s1 = []
res_q = []
expected = 1
top = -1
flag = 0
while q1:
    if q1 and q1[0] == expected:
        res_q.append(q1.pop(0))
        expected += 1
    else:
        if top==-1:
            top+=1
            s1.append(q1.pop(0))
        elif s1[top]>=q1[0]:
            top+=1
            s1.append(q1.pop(0))
        else:
            flag = -1
            break
while s1:
    res_q.append(s1.pop(-1))
if flag == -1:
    print("NP")
else:
    print(res_q)
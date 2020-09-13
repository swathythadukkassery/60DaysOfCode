l = list(map(int, input().split()))
product = int(input())
s = set()
flag = 1
for i in range(len(l)):
    if l[i]==0:
        if product==0:
            print("True")
            flag = 0
            break
    else:
        if product%l[i]==0:
            if product//l[i] in s:
                print("True")
                flag = 0
                break
        s.add(l[i])
if flag == 1:
    print("False")
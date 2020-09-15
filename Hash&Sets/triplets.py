li = list(map(int, input().split()))
product = int(input())
flag = 0
for i in range(len(li)):
    if li[i]!= 0 and product%li[i] == 0:
        for j in range(i+1, len(li)):
            if li[j]!= 0 and product%(li[j]*li[i]) == 0:
                if product//(li[j]*li[i]) in li:
                    n = li.index(product//(li[j]*li[i]))
                    if n>i and n>j:
                        flag = 1
                        print(li[i], li[j], li[n])
if flag == 0:
    print(0)
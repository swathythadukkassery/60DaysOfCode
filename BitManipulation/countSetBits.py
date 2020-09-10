a = int(input())
b = int(input())
c = a^b
count = 0
while c:
    count+=1
    c&=(c-1)
print(count)
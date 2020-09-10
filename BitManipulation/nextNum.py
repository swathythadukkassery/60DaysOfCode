# Given a positive number, find the next smallest and next largest numbers with same number of 1's

n=int(input())
c0 = 0
c1 = 0
c = n
while c&1 == 0 and c!=0 :
    c0+=1
    c>>=1
while c&1 != 0:
    c1+=1
    c>>=1
p = c1+c0
if p == 31 or p == 0:
    print("NP")
else:
    n|=(1<<p)
    mask = ~0
    mask<<=p
    n&=mask
    n|=(1<<c1-1)-1
print("next number :",n)
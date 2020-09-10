n=float(input())
bin="."
if n>=0 and n<=1:
    while n>0:
        if len(bin)>=32:
            print("errors")
            break
        r=n*2
        if r>=1:
            bin+='1'
            n=r-1
        else:
            bin+='0'
            n=r
    if len(bin)<32:
        print(bin)
else:
    print("error")
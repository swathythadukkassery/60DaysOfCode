def patternmatch(mainstr,pattern,mapd,n,m,i,j):
    if i==n and j==m:
        return True
    if i==n or j==m:
        return False
    ch=pattern[j]
    if ch in mapd:
        
        temp=mapd[ch]
        siz=len(temp)
        
        if temp==mainstr[i:i+siz]:
            return patternmatch(mainstr,pattern,mapd,n,m,i+siz,j+1)
        return False
    for leng in range(1,n+1-i):
        
        mapd[ch]=mainstr[i:i+leng]
       
        if patternmatch(mainstr,pattern,mapd,n,m,i+leng,j+1):
            return True
        mapd.pop(ch)
    return False



def fun(mainstr,pattern):
    if len(mainstr)<len(pattern):
        return False
    mapd={}
    if(patternmatch(mainstr,pattern,mapd,len(mainstr),len(pattern),0,0)==True):
        for i in pattern:
            print(i," :",mapd[i])
        return True
    else:
        return False



mainstr=input()
pattern=input()
if(fun(mainstr,pattern)==False):
    print('NP')
    
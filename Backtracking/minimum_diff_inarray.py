def find(l,s,result,pos,end,final):
    if pos==end:    
        if sum(result)<=s:
            if sum(result)>sum(final): 
                final=result[:]
    
        return final
    for i in l:
        if i not in result:    
            result.append(i)          
            pos+=1
            final=find(l,s,result,pos,end,final)   
            pos-=1
            result.pop(-1)   
    return final

l=list(map(int,input().split()))
n=len(l)
end=n//2
s=sum(l)//2
result=[]
final=[]
fin=find(l,s,result,0,end,final)
print(fin)
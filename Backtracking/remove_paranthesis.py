from collections import deque

def isPara(ch):
    return ch=='(' or ch==')'

def isValid(str):
    ctr=0
    for i in range(len(str)):
        # if(str=='()()()'):
        #     print(ctr)
        if(str[i]=='('):
            ctr+=1
        elif(str[i]==')'):
            ctr-=1
        if ctr<0:
            return False
    return ctr==0


def find(str):
    if len(str)==0:
        return
    p=0
    q=[]
    visit=set()
    q.append(str)
    visit.add(str)
    level=0
    while(len(q)!=0):
        p+=1
        str=q[0]
        q.pop(0)
        # print(str)
        if(isValid(str)==True):
            # print(str,'i')
            
            print(str)
            
            level=True
        if level:
            continue

        for i in range(len(str)):
            if isPara(str[i]):
                temp=str[0:i]+str[i+1:]
                if temp not in visit:
                    
                    visit.add(temp)
                    q.append(temp)

                    # print(q,p)
     


str=input()
find(str)
res=False
def diag(q,n,row,col):
    for i in range(col): 
        if q[row][i] == 1: 
            return False
    for i,j in zip(range(row,-1,-1),
                range(col,-1,-1)):
        if q[i][j]==1:
            return False
    for i,j in zip(range(row,n),
                range(col,-1,-1)):
        if q[i][j]==1:
            return False
    return True

def find(n,q,col):
    
    if col ==n:
        print(q)
        return True
    res=False
    for j in range(n):
        if diag(q,n,j,col)==True:
            q[j][col]=1
            res= find(n,q,col+1) or res
                
        q[j][col] = 0
    return res


def solve(n):
    q=[[0 for x in range(n)] for x in range(n)]
    if find(n,q,0)== True:
        print(q)
    else:
        print(q)


solve(int(input()))
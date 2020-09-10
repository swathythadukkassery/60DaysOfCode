N=9

def isValid(matrix,r,c):
    if r>=0 and r<N and c>=0 and c<N:
        return True
    return False
def findpath(matrix,r,c,path,count):
    
    addrow=[1,-1,0,0]
    addcol=[0,0,1,-1]
    if matrix[r][c]==0:
        print(path)
        return True
    
    for i in range(4):
        if addcol[i]==0:
            if addrow[i]==1:
                newrow=r+matrix[r][c]
                newcol=c
            else:
                newrow=r-matrix[r][c]
                newcol=c

        else:
            if addcol[i]==1:
                newrow=r
                newcol=c+matrix[r][c]
            else:
                newrow=r
                newcol=c-matrix[r][c]
        if isValid(matrix,newrow,newcol):
            if [newrow,newcol] not in path:
                path.append([newrow,newcol])
                if findpath(matrix,newrow,newcol,path,count):
                    return True
                else:
                    path.pop(-1)
    return False
        
def maze(matrix,r,c):
    path=[]
    count=0
    res=findpath(matrix,0,0,[[0,0]],count)
    path=[]
    if(res==True):
        count+=1
    
    res=findpath(matrix,0,c-1,[[0,c-1]],count)
    path=[]
    if(res==True):
        count+=1
    path=[]
    res=findpath(matrix,r-1,0,[[r-1,0]],count)
    if(res==True):
        count+=1
   
   
    path=[]
    
    
    res=findpath(matrix,r-1,c-1,[[r-1,c-1]],count)
    if(res==True):
        count+=1
    if count==0:
        print('NP')
    else:
        print(count)

matrix=(
        [3, 5, 4, 4, 7, 3, 4, 6, 3 ], 
        [6, 7, 5, 6, 6, 2, 6, 6, 2 ], 
        [3, 3, 4, 3, 2, 5, 4, 7, 2 ], 
        [6, 5, 5, 1, 2, 3, 6, 5, 6 ], 
        [3, 3, 4, 3, 0, 1, 4, 3, 4 ], 
        [3, 5, 4, 3, 2, 2, 3, 3, 5 ], 
        [3, 5, 4, 3, 2, 6, 4, 4, 3 ], 
        [3, 5, 1, 3, 7, 5, 3, 6, 4 ], 
        [6, 2, 4, 3, 4, 5, 4, 5, 1 ] 
    )
    
R=9
C=9

maze(matrix,R,C)

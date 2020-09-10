from queue import PriorityQueue
import random
def valid(board,rownew,colnew,n):
    if(rownew>=0 and rownew<n) and(colnew>=0 and colnew<n) and board[rownew][colnew]==0:
        return True
    
    return False
n=int(input())
drow = [-2, -1, 1, 2, -2, -1, 1, 2]
dcol = [1, 2, 2, 1, -1, -2, -2, -1]
row=random.randint(0,n)
col=random.randint(0,n)
board=[[0 for i in range(n)]for i in range(n)]



for i in range(n*n):
    board[row][col]=i+1
    pq=PriorityQueue()
    for j in range(n):
        newrow=row+drow[j]
        newcol=col+dcol[j]
        if(valid(board,newrow,newcol,n)):
            
            count=0
            for k in range(n):
                temprow=newrow+drow[k]
                tempcol=newcol+dcol[k]
                if(valid(board,temprow,tempcol,n)):
                    
                    count+=1
            pq.put((count,j))
            

    if pq.empty()!=True:
        
        pos=pq.get()
        
        row=row+drow[pos[1]]
        col=col+dcol[pos[1]]
        
    else:
        break
print(board)

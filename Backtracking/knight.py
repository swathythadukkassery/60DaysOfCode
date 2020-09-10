def possible(board,rownew,colnew,n):
    if(rownew>=0 and rownew<n) and(colnew>=0 and colnew<n) and board[rownew][colnew]==0:
        return True
    
    return False

def find(board,n,move,row,col):
    rowInc=[2,1,-1,-2,-2,-1,1,2]
    colInc=[1,2,2,1,-1,-2,-2,-1]
    if move==(n**2):
        for i in range(n):
            print(board[i])
        return True
    else:
        for i in range(n):
            
            rownew=row+rowInc[i]
            colnew=col+colInc[i]
            if possible(board,rownew,colnew,n):
                move+=1
                board[rownew][colnew]=move
                if(find(board,n,move,rownew,colnew)):
                    return True
                move-=1
                board[rownew][colnew]=0
      
        return False

def start(n):
    board=[[0 for x in range(n)]for y in range(n)]
    move=1
    board[0][0]=1
    if find(board,n,move,0,0)==True:
        print(board)
    else:
        print("np")



n=int(input())
start(n)
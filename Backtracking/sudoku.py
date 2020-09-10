class Grids:
    def __init__(self,n):
        self.n=n
        self.sudoku=[[0 for i in range(self.n)] for j in range(self.n)]
    def finish(self,l):
        for i in range(self.n):
            for j in range(self.n):
                if self.sudoku[i][j]==0:
                    l[0]=i
                    l[1]=j
                    return False
        return True
    def validrow(self,r,i):
        for k in range(9):
            if(self.sudoku[r][k]==i):
                return False
        return True
    def validcol(self,c,i):
        for k in range(9):
            if(self.sudoku[k][c]==i):
                return False
        return True
    def validbox(self, row, col, num): 
        startrow, startcol = 3 *(row//3), 3 *(col//3) 
        for x in range(startrow, startrow+3):
            for y in range(startcol, startcol+3):
                if self.sudoku[x][y] == num:
                        return False
        return True
       
    def find(self):
        l=[0,0]
        if self.finish(l)==True:
            print(self.sudoku)
            return True
        r=l[0]
        c=l[1]
        for i in range(1,10):
            if (self.validrow(r,i) and self.validcol(c,i) and self.validbox(r,c,i)):
                self.sudoku[r][c]=i
                if(self.find()):
                    return True
                self.sudoku[r][c]=0
        return False




grid =Grids(9)
      
    # assigning values to the grid 
grid.sudoku =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]] 
res=grid.find()
if res==False:
    print("NP")
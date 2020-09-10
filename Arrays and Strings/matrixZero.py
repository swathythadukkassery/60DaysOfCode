class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=[]
        c=[]
        for i in range(len(matrix)):
            if 0 not in matrix[i]:
                continue
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:                 
                    c.append(j)
            matrix[i]=[0]*len(matrix[0])
        j=0
        while j<len(c):
            for k in range(len(matrix)):
                matrix[k][c[j]]=0
            j+=1
        print(r,c)
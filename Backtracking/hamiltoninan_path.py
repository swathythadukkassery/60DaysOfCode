class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for i in range(vertices)] for i in range(vertices)]
    def valid(self,i,path,pos):
        if self.graph[path[pos-1]][i]==0:
            return False
        if i in path:
            return False
        return True

    def ham(self,path,pos):
        if self.v==pos:
            if self.graph[path[pos-1]][path[0]]==1:
                print(path)
                return True
            return False
        for i in range(self.v):
            if self.valid(i,path,pos)==True:
                path.append(i)
                if self.ham(path,pos+1)==True:
                    return True
                path.pop(-1)
            
        return False
        


g=Graph(5)
g.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],  
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],  
        [0, 1, 1, 0, 0], ] 
path=[]
path.append(0)
pos=1
res=g.ham(path,pos)
if res==False:
    print('NP')
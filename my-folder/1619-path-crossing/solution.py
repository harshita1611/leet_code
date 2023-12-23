class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s={(0,0)}
        x_cor,y_cor=0,0
        for i in path:
            if i=='N':
                y_cor+=1
            if i=='S':
                y_cor-=1
            if i=='E':
                x_cor+=1
            if i=='W':
                x_cor-=1
            if (x_cor,y_cor) in s :
                    return True
            else : 
                s.add((x_cor,y_cor))
        return False

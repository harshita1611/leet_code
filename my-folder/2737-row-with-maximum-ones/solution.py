class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        max_count=0
        row_num=0
        for i in range(n):
            curr_one=0
            for j in range(m):
                if mat[i][j]==1:
                    curr_one+=1
            
            if curr_one>max_count:
                max_count=curr_one
                row_num=i
        
        return [row_num,max_count]
            

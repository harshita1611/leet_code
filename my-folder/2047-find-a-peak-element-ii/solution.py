class Solution:
    def max_index(self,matrix,mid):
        index=-1
        value=-1
        for row in range(len(matrix)):
            if matrix[row][mid]>value:
                value=matrix[row][mid]
                index=row
        return index

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low=0
        high=len(mat[0])

        while (low<=high):
            mid=(low+high)//2
            g=self.max_index(mat,mid)
            if mid-1>=0:
                left=mat[g][mid-1]
            else:
                left=-1
            if mid+1 < len(mat[0]):
                right=mat[g][mid+1]
            else:
                right=-1
            if (mat[g][mid]>left and mat[g][mid]>right):
                return [g,mid]
            elif mat[g][mid]<left:
                high=mid-1
            else:
                low=mid+1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        low = 0 
        high = (row*col) -1
        while low <= high  :
            mid=(low+high)//2
            ans = matrix[mid // col][mid % col]
            if target == ans:
                return True
            if target < ans:
                high=mid-1
            else :
                low=mid+1
        return False

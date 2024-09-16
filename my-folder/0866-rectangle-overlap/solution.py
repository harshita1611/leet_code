class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        firstx1,firsty1,firstx2,firsty2=rec1
        secondx1,secondy1,secondx2,secondy2=rec2
        if (firstx2<=secondx1)or(firstx1>=secondx2):
            return False
        
        if (firsty2<=secondy1)or(firsty1>=secondy2):
            return False
        
        return True

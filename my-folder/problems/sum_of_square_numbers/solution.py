class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(math.sqrt(c))

        while left<=right:
            if (int(left*left) + int(right*right))==int(c) :
                return True
            elif (int(left*left) + int(right*right))<int(c) :
                left+=1
            else:
                right-=1
        return False
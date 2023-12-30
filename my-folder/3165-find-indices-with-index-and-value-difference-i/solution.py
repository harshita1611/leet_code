class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                if (abs(j-i)>=indexDifference and abs(nums[j]-nums[i])>=valueDifference):
                    return [i,j]
        return [-1,-1]

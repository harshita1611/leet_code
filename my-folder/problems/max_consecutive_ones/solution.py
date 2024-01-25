class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi,count=0,0
        for i in nums:
            if i==0:
                count=0
            else:
                count+=1
                maxi=max(maxi,count)
        return maxi
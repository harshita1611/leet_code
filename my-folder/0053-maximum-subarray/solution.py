class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0 
        maxSum = nums[0]
        n= len(nums)
        for i in range(n) :
            currSum += nums[i]
            maxSum = max(maxSum , currSum)
            
            if currSum < 0 :
                currSum = 0 
        return maxSum

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 :
            return nums[0]
        if n==2 :
            return max(nums[0],nums[1])
        dp=[0]*(n+1)
        dp[0]=nums[0]
        dp[1] = nums[1]
        
        dp[2] = max(nums[1], nums[2]+nums[0])
        for i in range(3,n) :
            dp[i] = max(dp[i-2] + nums[i] , dp[i-3] +nums[i])
        return max(dp[n-1], dp[n-2]) 
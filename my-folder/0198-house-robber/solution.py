class Solution:
    def rob(self, nums: List[int]) -> int:
        def tabulation(n, nums, dp):
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                pick = nums[i]
                if i>1:
                    pick+=dp[i-2]
                notpick = 0+dp[i-1]
                dp[i] = max(pick, notpick)

            return dp[len(nums)-1]

        dp = [0]*(len(nums)+1)
        return tabulation(len(nums)-1, nums, dp)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        dp=[defaultdict(int) for _ in range(n)]
        #dp[i][diff] => end with index i and difference being diff
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=1+dp[j][diff]
                res+=1+dp[j][diff]
        return res-((n*(n-1))//2)
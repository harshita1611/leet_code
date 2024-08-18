class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        seen=[False]*(n+1)
        for i in nums:
            if 0<=i<=n:
                seen[i]=True
        for i in range(1,n+1):
            if not seen[i]:
                return i
        return n+1

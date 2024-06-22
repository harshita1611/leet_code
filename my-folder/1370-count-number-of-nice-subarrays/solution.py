class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]%=2
        
        prefix=[0]*(n+1)
        prefix[0]=1

        s=0
        ans=0

        for i in nums:
            s+=i
            if s>=k:
                ans+=prefix[s-k]
            prefix[s]+=1

        return ans

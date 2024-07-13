class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=0
        ans=0
        currsum=0

        while right<len(nums):
            currsum+=nums[right]
            while nums[right] * (right-left+1)>currsum+k:
                currsum-=nums[left]
                left+=1
            ans= max(ans,right-left+1)
            right+=1
        
        return ans

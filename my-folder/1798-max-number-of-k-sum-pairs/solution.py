class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        left=0
        right=n-1
        count=0
        while left < right :
            currentsum=nums[left]+nums[right]
            if currentsum==k : 
                count+=1
                left+=1
                right-=1
            elif currentsum<k :
                left+=1
            else :
                right-=1
        return count

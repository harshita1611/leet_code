class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high=len(nums)-1
        mini=nums[-1]
        while low<high :
            mid=(low+high)//2
            if mini < nums[mid]:
                mini=min(mini,nums[mid])
                low=mid+1 
            else :
                mini=min(mini,nums[mid])
                high=mid
        return mini
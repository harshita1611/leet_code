class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=-1
        y=-1
        n=len(nums)
        for i in range(n) : 
            if nums[i]==target : 
                x=i
                break
        for j in range(n-1,-1,-1) : 
            if nums[j]==target : 
                y=j
                break
        return x,y
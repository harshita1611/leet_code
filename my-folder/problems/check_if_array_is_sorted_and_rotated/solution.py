class Solution:
    def check(self, nums: List[int]) -> bool:
        n= len(nums)
        count=0
        for i in range(1,n):
            if nums[i]< nums[i-1]:
                count+=1
            if count >1 :
                return False
        if nums[-1] <= nums[0] or count ==0 :
            return True
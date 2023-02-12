class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=0
        for i in set(nums):
            count+=1
        if count==len(nums):
            return False
        else:
            return True

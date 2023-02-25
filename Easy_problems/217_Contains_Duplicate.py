class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count=0
        for i in set(nums):
            count+=1
        if count==len(nums):
            return False
        else:
            return True

obj = Solution()
print(obj.containsDuplicate([1,2,3,4]))
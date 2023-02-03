class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in nums :
            counter = nums.count(i)
            if counter>1 :
                nums.remove(i)
        return nums



obj = Solution()
print(obj.removeDuplicates([1,1,1,1]))
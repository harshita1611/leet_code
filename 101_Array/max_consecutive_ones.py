class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        arr1=[]
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            arr1.append(count)
            if nums[i] == 0:
                count = 0
                continue
        print (max(arr1))

obj = Solution()
obj.findMaxConsecutiveOnes([1,1,0,1,1,1])
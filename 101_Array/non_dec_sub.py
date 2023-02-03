class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        arr = []
        arr2=[]
        nums.sort()
        for i in range(len(nums)-1) :
            for j in range(i , len(nums)-1) :
                if nums[j + 1] > nums[j]:
                    arr.append(nums[j])
            arr2.append(arr)
        return arr2

obj = Solution()
print(obj.findSubsequences([4,6,7,7]))
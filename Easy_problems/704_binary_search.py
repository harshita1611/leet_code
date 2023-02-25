class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high = len(nums)
        while low<=high:
            mid = int((low + high) / 2)
            ans = nums[mid]
            if target == ans:
                return mid
            if target < ans:
                high=mid-1
            else :
                low=mid+1
        return -1
obj=Solution()
print(obj.search([-1,0,3,5,9,12],9))
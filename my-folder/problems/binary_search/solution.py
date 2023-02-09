class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high = len(nums)-1
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
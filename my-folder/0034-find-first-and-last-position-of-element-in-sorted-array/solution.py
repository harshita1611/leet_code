class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def from_left(nums,target):
            low ,high = 0 , len(nums)-1
            while low<= high :
                mid=(low+high)//2
                if nums[mid]<target :
                    low = mid + 1 
                else :
                    high = mid-1
            return low
        def from_right(nums,target):
            low ,high = 0 , len(nums)-1
            while low<= high :
                mid=(low+high)//2
                if nums[mid]<=target :
                    low = mid + 1 
                else :
                    high = mid-1
            return high
        left = from_left(nums,target)
        right= from_right(nums,target)

        if left <= right :
            return [left,right]
        else :
            return [-1,-1]

import math

class Solution:
    def sumbydiv(self,arr,div):
        totalSum=0
        n=len(arr)
        for i in range(n):
            totalSum+=math.ceil(arr[i]/div)
        return totalSum
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)

        if n  >threshold:
            return -1

        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.sumbydiv(nums,mid) <= threshold:
                high=mid-1
            else:
                low=mid+1
        
        return low

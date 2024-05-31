class Solution:
    def countPartitions(self,nums,maxSum):
        n=len(nums)
        partitions=1
        subarraySum=0
        for i in range(n):
            if subarraySum+ nums[i]<= maxSum:
                subarraySum+=nums[i]
            else:
                partitions+=1
                subarraySum=nums[i]
        return partitions

    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)//2
            partitions=self.countPartitions(nums,mid)
            if partitions > k:
                low=mid+1
            else:
                high=mid-1
        return low

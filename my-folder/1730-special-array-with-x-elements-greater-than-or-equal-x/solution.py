class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def lowerbound(nums,target):
            low=0
            high=len(nums)-1
            ans=len(nums)
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        
        nums.sort()
        # print(nums)
        lili=max(nums)
        for i in range(1,lili+1):
            res=lowerbound(nums,i)
            # print(res)
            if len(nums)-res==i:
                return i
        return -1

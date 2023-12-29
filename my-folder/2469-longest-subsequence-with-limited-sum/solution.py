class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        def upperbound(nums, target):
            low = 0
            high = len(nums)-1
            ans = len(nums)
            while low <= high:
                mid = (low+high)//2
                if nums[mid] > target:
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            return ans

        prefix = [0]*(len(nums))
        if len(nums) != 0:
            prefix[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]+nums[i]
            
        print(prefix)
        
        res = []
        for i in queries:
            ans = upperbound(prefix, i)
            res.append(ans)

        return res


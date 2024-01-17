class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        n=len(nums)
        for i in range(n):
            ans=target-nums[i]
            if ans in hashmap.keys():
                return [hashmap[ans],i]
            else:
                hashmap[nums[i]]=i